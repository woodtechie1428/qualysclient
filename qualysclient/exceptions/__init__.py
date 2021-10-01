class QualysClientError(Exception):
    """Base Exception class for Qualys Client"""


class ParameterValidationError(QualysClientError):
    """When Parameter validation fails"""

    def __init__(
        self,
        msg="Qualys API parameter validation failed",
        qualys_error_text: str = None,
    ):
        self.qualys_error_text = qualys_error_text
        self.message = msg
        super().__init__(self.message)


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


class LoginError(QualysClientError):
    """When login failures occur"""
