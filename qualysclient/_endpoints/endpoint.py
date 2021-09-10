
from typing import List


class InputParameter:

    def __init__(self, param_name:str, is_required:bool):
        self.param_name = param_name
        self.is_required = is_required

    def __str__(self):
        _ = f'{self.param_name} :: {self.is_required}'
        return _

InputParameters = List[InputParameter]

class APIAction:

    def __init__(self, action_name, api_endpoint:str, input_params:InputParameters):
        self.action_name = action_name
        self.api_endpoint:str = api_endpoint
        self.input_parameters = [InputParameter(param_name=pn, is_required=rb) for pn, rb in input_params]
        
    def add_summary(self, summary:str):
        self.summary:str = summary

    @property
    def action_name(self):
        return self.__action_name

    @action_name.setter
    def action_name(self, action_name):
        if (isinstance(action_name, str)):
            self.__action_name = action_name
        else:
            raise Exception('action_name must be of type str')

    @property
    def input_parameters(self):
        return self.__input_parameters

    @input_parameters.setter
    def input_parameters(self, input_params:InputParameters):
        self.__input_parameters = input_params

    def __str__(self):
        _ = f'API Action Name: {self.action_name}\n'
        _ = _ + f'\tAPI Endpoint: {self.api_endpoint}\n'
        _ = _ + '\tInput Parameters: \n\t\t'+"\n\t\t".join([str(ip) for ip in self.input_parameters])
        return _
        



'''
get_report_list()
    uses APIAction get_report_list
    find by lookup of term "api_action_list" in some list
    /api/2.0/fo/report/


'''