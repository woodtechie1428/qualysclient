from qualysclient._endpoints import api_actions as API_ACTIONS
from qualysclient._endpoints.endpoint import APIAction
from qualysclient.defaults import AUTH_URI, BASE_URI
import requests

def _validate_parameters(api_action, **kwargs):
        if api_action is None:
            raise Exception("No api_action provided")
        if API_ACTIONS.get(api_action, None) is None:
            raise Exception("Invalid api_action specified")
        validated = True
        print (f"Validating arguments submitted for {api_action}: \n")

        for k,v in kwargs.items():
            print (f"\t{k:15} \t.....\t", end="")
            try:
                if k in API_ACTIONS.get(api_action).get_valid_input_parameters():
                    print ("VALID", flush=True)
                else:
                    print ("INVALID", flush=True)
                    validated = False
            except AttributeError:
                return False

        #validate all required params included
        print (f"Validating requirements parameters for {api_action} were included: \n")
        for required_param in API_ACTIONS.get(api_action).get_required_input_parameters():
            print (f"\t{required_param:15} \t.....\t", end="")
            if required_param not in kwargs.keys():
                print ("MISSING", flush=True)
            else:
                print ("VALID", flush=True)
        
        return validated


def _api_request(caller, api_action, **kwargs):
    if (_validate_parameters(api_action, **kwargs)):
        _ref:APIAction = API_ACTIONS.get(api_action)
        http_method = _ref.http_method
        api_endpoint = _ref.api_endpoint
        api_url = BASE_URI+api_endpoint
        input_params = kwargs
        return _perform_request(caller, api_url, input_params, http_method)
    else:
        raise Exception("Parameter Validation failed")

def _perform_request(caller, api_url, input_params, http_method = 'POST'):
    try:
        if (http_method == 'POST'):
            api_response = caller.s.post(
                url = api_url,
                data = input_params,
                timeout = 180
            )
            api_response.raise_for_status()
        else:
            api_response = caller.s.get(
                url = api_url,
                params = input_params,
                timeout = 180
            )
            api_response.raise_for_status()
            return api_response
    except requests.exceptions.HTTPError as http_error:
        return api_response
    except requests.ConnectionError as connection_error:
        pass
    except requests.URLRequired as url_required_error:
        pass
    except requests.TooManyRedirects as too_many_redirects_error:
        pass
    except requests.exceptions.Timeout as e:
        print ("Request Timed out")
        raise requests.exceptions.Timeout
    except requests.exceptions.SSLError as e:
        print ("SSL Error")
        raise requests.exceptions.SSLError
    except requests.RequestException as request_exception_error:
        pass
    