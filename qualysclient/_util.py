import logging
import qualysclient
from qualysclient._endpoints import api_actions as API_ACTIONS
from qualysclient._endpoints.endpoint import APIAction
from qualysclient.defaults import BASE_URI, REQUEST_TIMEOUT, MAX_RETRIES
from qualysclient.exceptions import (
    RequiredParameterMissingError,
    InvalidParameterError,
    ParameterValidationError,
)
import requests


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


def _api_request(caller, api_action: str, **kwargs) -> requests.Response:
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


def _perform_request(
    caller, api_url, input_params, http_method="POST"
) -> requests.Response:
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
        except requests.exceptions.HTTPError as http_error:
            # handle non 200 status codes here
            logger.error("HTTP Exception caught")
            logger.error(http_error.response.status_code)
            return api_response
        except requests.URLRequired:
            logger.exception("caught URLRequired Exception")
            raise
        except requests.TooManyRedirects:
            logger.exception("caught TooManyRedirects Exception")
            raise
        except requests.exceptions.Timeout:
            logger.error(f"{i}: Request Timed out caught")
            if i == MAX_RETRIES - 1:
                raise
            else:
                continue
        except requests.exceptions.SSLError:
            logger.error("SSL Error Exception caught")
            raise
        except requests.ConnectionError:
            logger.exception("Caught Connection Error Exception")
            raise
        except requests.RequestException:
            logger.exception("Caught ambiguous RequestException")
            raise
