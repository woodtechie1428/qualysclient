class ParameterValidationError(Exception):
    """When Parameter validation fails"""


class RequiredParameterMissingError(ParameterValidationError):
    """When Required Parameters are missing based on provided api_aciton"""

    def __init__(self, missing_required_param_name: str, api_action: str) -> None:
        self.missing_required_param_name = missing_required_param_name
        self.api_action = api_action
        self.message = (
            f"'{missing_required_param_name}' is a required parameter for {api_action}"
        )
        super().__init__(self.message)


class InvalidParameterError(ParameterValidationError):
    """Exception raised when invalid parameters are specified for a given api_action"""

    def __init__(self, invalid_param_name: str, api_action: str) -> None:
        self.invalid_param_name = invalid_param_name
        self.api_action = api_action
        self.message = (
            f"'{invalid_param_name}' is not a valid parameter for {api_action}"
        )
        super().__init__(self.message)
