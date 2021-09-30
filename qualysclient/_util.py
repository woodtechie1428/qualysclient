import logging
from typing import Tuple
from requests.exceptions import (
    HTTPError,
    Timeout,
    TooManyRedirects,
    ConnectionError,
    RequestException,
    URLRequired,
    SSLError,
)
from requests import Response
from lxml import etree

from qualysclient._endpoints import api_actions as API_ACTIONS
from qualysclient.models import APIAction
from qualysclient._defaults import BASE_URI, REQUEST_TIMEOUT, MAX_RETRIES
from qualysclient.exceptions import (
    RequiredParameterMissingError,
    InvalidParameterError,
    ParameterValidationError,
    LoginError,
)


logger = logging.getLogger(__name__)


def _validate_parameters(api_action, **kwargs) -> bool:
    """Validates parameters submitted as key-value args against specified api_action

    Args:
        api_action (str): short name for api action

    Raises:
        ParameterValidationError: Generic Exception for Parameter Validation Errors
        InvalidParameterError: when submitted parameter is not valid for given api_action
        RequiredParameterMissingError: when required parameters for given api_action are not included in the args

    Returns:
        bool: True if all validation's pass without exceptions
    """
    if api_action is None:
        raise ParameterValidationError("No api_action specified")
    if API_ACTIONS.get(api_action, None) is None:
        raise ParameterValidationError("Invalid api_action specified")
    validated = False
    logger.debug(f"Validating parameters submitted for {api_action}: \n")

    try:
        if (API_ACTIONS.get(api_action)).validate_submitted_parameters(**kwargs):
            validated = True
    except InvalidParameterError:
        logger.exception("Failed parameter validation")
        raise

    logger.debug(f"Validating required parameters submitted for {api_action}: \n")
    try:
        if API_ACTIONS.get(api_action).validate_submitted_required_parameters(**kwargs):
            validated = True
    except RequiredParameterMissingError:
        logger.exception("Failed parameter validation - required parameter missing")
        raise

    return validated


def _api_request(caller, api_action: str, **kwargs) -> Response:
    """service method to validate and prepare api request call

    Args:
        caller (qualysclient.QualysClient): authenticated QualysClient instance
        api_action (str): short name for api action

    Raises:
        ParameterValidationError

    Returns:
        requests.Response: Raw response object
    """
    try:
        if _validate_parameters(api_action, **kwargs):
            _ref: APIAction = API_ACTIONS.get(api_action)
            http_method = _ref.http_method
            api_endpoint = _ref.api_endpoint
            api_url = BASE_URI + api_endpoint
            input_params = kwargs
            return _perform_request(caller, api_url, input_params, http_method)
    except ParameterValidationError:
        logger.exception("Exception while validating parameters")
        raise


def _perform_request(caller, api_url, input_params, http_method="POST") -> Response:
    for i in range(MAX_RETRIES):
        try:
            if http_method == "POST":
                api_response = caller.s.post(
                    url=api_url, data=input_params, timeout=REQUEST_TIMEOUT
                )
                api_response.raise_for_status()
                return api_response
            else:
                api_response = caller.s.get(
                    url=api_url, params=input_params, timeout=REQUEST_TIMEOUT
                )
                api_response.raise_for_status()
                return api_response
        except HTTPError as http_error:
            # handle non 200 status codes here
            http_error_code = http_error.response.status_code
            logger.error("HTTP Error caught: %s", http_error_code)
            (
                qualys_error_code,
                qualys_error_code_description,
            ) = extract_qualys_error_codes(api_response)

            if http_error_code == 409:
                # get X-headers

                if qualys_error_code == 1960:
                    # handle concurrency error code 1960
                    pass
                elif qualys_error_code == 1965:
                    # handle rate limit error code 1965
                    pass
                elif qualys_error_code in [2003, 2011]:
                    # handle code 2003
                    # handle code 2011
                    pass
            elif http_error_code == 400:
                # bad request
                # codes 1901, 1903, 1904, 1905, 1907 ,1908, 1922, 999
                pass
            elif http_error_code == 401:
                # bad login/password
                # codes 2000
                logger.error(
                    "http_error_code: %s qualys_error_code: %s qualys_error_code_description: %s",
                    http_error_code,
                    qualys_error_code,
                    qualys_error_code_description,
                )
                raise LoginError
            elif http_error_code == 403:
                # forbidden
                # codes 2002,  2012
                pass
            elif http_error_code == 501:
                # internal error
                # codes 999
                pass
            elif http_error_code == 503:
                # maintenance
                # codes 1999
                pass
            return api_response
        except URLRequired:
            logger.exception("caught URLRequired Exception")
            raise
        except TooManyRedirects:
            logger.exception("caught TooManyRedirects Exception")
            raise
        except Timeout:
            logger.error(f"{i}: Request Timed out caught")
            if i == MAX_RETRIES - 1:
                raise
            else:
                continue
        except SSLError:
            logger.error("SSL Error Exception caught")
            raise
        except ConnectionError:
            logger.exception("Caught Connection Error Exception")
            raise
        except RequestException:
            logger.exception("Caught ambiguous RequestException")
            raise


def extract_qualys_error_codes(api_response: Response) -> Tuple[int, str]:
    xml = etree.fromstring(api_response.content)
    qualys_error_code = xml.find("./RESPONSE/CODE").text
    qualys_error_code_description = xml.find("./RESPONSE/TEXT").text

    return (qualys_error_code, qualys_error_code_description)
