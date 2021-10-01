import qualysclient
from typing import List


class InputParameter:
    def __init__(self, param_name: str, is_required: bool = False, **kwargs):
        self.param_name = param_name
        self.is_required = is_required
        self.description = kwargs.get("description")

    def __str__(self):
        _ = f"{self.param_name} :: {self.is_required}"
        if self.description:
            _ = _ + " :: " + self.description
        return _


InputParameters = List[InputParameter]


class APIAction:
    def __init__(
        self,
        action_name,
        api_endpoint: str,
        input_params: InputParameters,
        http_method="POST",
    ):
        self.action_name = action_name
        self.api_endpoint: str = api_endpoint
        self.input_parameters = [InputParameter(**ip) for ip in input_params]
        self.http_method = http_method

    def add_summary(self, summary: str):
        self.summary: str = summary

    @property
    def action_name(self):
        return self.__action_name

    @action_name.setter
    def action_name(self, action_name):
        if isinstance(action_name, str):
            self.__action_name = action_name
        else:
            raise Exception("action_name must be of type str")

    @property
    def input_parameters(self):
        return self.__input_parameters

    @input_parameters.setter
    def input_parameters(self, input_params: InputParameters):
        self.__input_parameters = input_params

    def __str__(self):
        _ = f"API Action Name: {self.action_name}\n"
        _ = _ + f"\tAPI Endpoint: {self.api_endpoint}\n"
        _ = _ + f"\tHTTP Method: {self.http_method}\n"
        _ = (
            _
            + "\tInput Parameters: \n\t\t"
            + "\n\t\t".join([str(ip) for ip in self.input_parameters])
        )
        return _

    def get_valid_input_parameters(self):
        return [input_param.param_name for input_param in self.input_parameters]

    def get_required_input_parameters(self):
        return [
            input_param.param_name
            for input_param in self.input_parameters
            if input_param.is_required is True
        ]

    def get_optional_input_parameters(self):
        return [
            input_param.param_name
            for input_param in self.input_parameters
            if input_param.is_required is False
        ]

    def check_parameter(self, param_name):
        if param_name in self.get_valid_input_parameters():
            return True
        else:
            return False

    def validate_submitted_parameters(self, **input_params):
        for input_param_name in input_params.keys():
            if not self.check_parameter(input_param_name):
                raise qualysclient.exceptions.InvalidParameterError(
                    input_param_name, self.action_name
                )
                return False
        return True

    def validate_submitted_required_parameters(self, **input_params):
        required_params = self.get_required_input_parameters()
        for required_param in required_params:
            if required_param not in input_params.keys():
                raise qualysclient.exceptions.RequiredParameterMissingError(
                    missing_required_param_name=required_param,
                    api_action=self.action_name,
                )
        return True
