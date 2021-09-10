from qualysclient._endpoints import api_actions as API_ACTIONS
from qualysclient._endpoints.endpoint import APIAction
from qualysclient.defaults import AUTH_URI, BASE_URI
import requests

def _validate_parameters(api_action, **kwargs):
        validated = True
        print (f"Validating arguments submitted for {api_action}: \n")

        for k,v in kwargs.items():
            print (f"\t{k:15} \t.....\t", end="")
            if k in API_ACTIONS.get(api_action).get_valid_input_parameters():
                print ("VALID", flush=True)
            else:
                print ("INVALID", flush=True)
                validated = False


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

def _perform_request(caller, api_url, input_params, http_method = 'GET'):
    api_response = requests.request(
        method=http_method, 
        url=api_url, 
        params=input_params,
        headers=caller.s.headers,
        cookies=caller.s.cookies)
    return api_response.status_code, api_response.content