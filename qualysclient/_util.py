import logging

logger = logging.getLogger(__name__)
from qualysclient._endpoints import api_actions as API_ACTIONS
from qualysclient._endpoints.endpoint import APIAction
from qualysclient.defaults import BASE_URI, REQUEST_TIMEOUT, MAX_RETRIES
import requests


def _validate_parameters(api_action, **kwargs):
    if api_action is None:
        raise Exception("No api_action provided")
    if API_ACTIONS.get(api_action, None) is None:
        raise Exception("Invalid api_action specified")
    validated = True
    logger.debug(f"Validating arguments submitted for {api_action}: \n")

    for k, v in kwargs.items():
        logger.debug(f"\t{k:15} \t.....\t", end="")
        try:
            if k in API_ACTIONS.get(api_action).get_valid_input_parameters():
                logger.debug("VALID", flush=True)
            else:
                logger.debug("INVALID", flush=True)
                validated = False
        except AttributeError:
            return False

    # validate all required params included
    print(f"Validating requirements parameters for {api_action} were included: \n")
    for required_param in API_ACTIONS.get(api_action).get_required_input_parameters():
        logger.debug(f"\t{required_param:15} \t.....\t", end="")
        if required_param not in kwargs.keys():
            logger.debug("MISSING", flush=True)
        else:
            logger.debug("VALID", flush=True)

    return validated


def _api_request(caller, api_action, **kwargs):
    if _validate_parameters(api_action, **kwargs):
        _ref: APIAction = API_ACTIONS.get(api_action)
        http_method = _ref.http_method
        api_endpoint = _ref.api_endpoint
        api_url = BASE_URI + api_endpoint
        input_params = kwargs
        return _perform_request(caller, api_url, input_params, http_method)
    else:
        raise Exception("Parameter Validation failed")


def _perform_request(caller, api_url, input_params, http_method="POST"):
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
        except requests.URLRequired as url_required_error:
            logger.exception("caught URLRequired Exception")
            raise
        except requests.TooManyRedirects as too_many_redirects_error:
            logger.exception("caught TooManyRedirects Exception")
            raise
        except requests.exceptions.Timeout as e:
            logger.error(f"{i}: Request Timed out caught")
            if i == MAX_RETRIES - 1:
                raise
            else:
                continue
        except requests.exceptions.SSLError as e:
            logger.error("SSL Error Exception caught")
            raise
        except requests.ConnectionError as connection_error:
            logger.exception("Caught Connection Error Exception")
            raise
        except requests.RequestException as request_exception_error:
            logger.exception("Caught ambiguous RequestException")
            raise
