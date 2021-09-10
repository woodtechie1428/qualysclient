
from typing import List


class APIEndpoint:

    def __init__(self):
        self.endpoint
        self.http_methods 
        self.summary
        self.action:APIAction
        self.input_params

class InputParameter:

    def __init__(self, param_name:str, is_required:bool):
        self.param_name = param_name
        self.is_required = is_required

class APIAction:

    def __init__(self, action_name, api_endpoint:APIEndpoint, input_params:List[InputParameter]):
        self.action_name = action_name
        self.api_endpoint = api_endpoint
        self.input_parameters = input_params
        



'''
get_report_list()
    uses APIAction get_report_list
    find by lookup of term "api_action_list" in some list
    /api/2.0/fo/report/


'''