from requests import Response
from qualysclient._util import _api_request


# class Reports:
#     """methods to interacts with the reports endpoint"""


def list_reports(self, **kwargs) -> Response:
    """View a list of reports in the user’s account when Report Share feature is enabled.

    The report list output includes all report types, including scorecard reports.

    Args:
        **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

    Returns:
        :class:`~requests.Response`: Qualys API response contained within request.Response object
    """

    api_action = "list_reports"
    return _api_request(self, api_action, **kwargs)


def launch_report(self, template_id: int, **kwargs) -> Response:
    """Launch a report in the user's account.
    Launch a report in the user's account. The Report Share feature must be enabled in the
    user's subscription. When a report is launched with Report Share, the report is run in the
    background, and the report generation processing does not timeout until the report has
    completed.

    Args:
        template_id (int):  (Required) The template ID of the report you want to launch.
        **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

    Returns:
        :class:`~requests.Response`: Qualys API response contained within request.Response object
    """
    api_action = "launch_report"
    kwargs["template_id"] = template_id
    return _api_request(self, api_action, **kwargs)


def launch_scorecard(self, name: str, **kwargs) -> Response:
    """Launch a vulnerability scorecard report in the user’s Report Share.

    Launch a vulnerability scorecard report in the user’s Report Share. It is not possible to
    launch any compliance scorecard reports or WAS scorecard reports using this API at this time.
    When a scorecard report is launched, the report is run in the background, and the report
    generation processing does not timeout until the report has completed.

    Args:
        name (str):  (Required) Specifies the scorecard name for the vulnerability scorecard report that you want to launch. This name corresponds to a service-provided scorecard or a user-created scorecard. For a service-provided scorecard, specify one of these names:

            - Asset Group Vulnerability Report
            - Ignored Vulnerabilities Report
            - Most Prevalent Vulnerabilities Report
            - Most Vulnerable Hosts Report
            - Patch Report

        **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_
    Returns:
        :class:`~requests.Response`: Qualys API response contained within request.Response object
    """
    api_action = "launch_scorecard"
    return _api_request(self, api_action, **kwargs)


def cancel_running_report(self, id: int, **kwargs) -> Response:
    """Cancel a running report in the user’s account.

    Args:
        id (int): Specifies the report ID of a running report that you want to cancel. The status of the report must be “running”.
        **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

    Raises:
        `ParameterValidationError`: When Parameter Validation fails

    Returns:
        :class:`~requests.Response`: Qualys API response contained within request.Response object
    """
    api_action = "cancel_running_report"
    return _api_request(self, api_action, **kwargs)


def download_saved_report(self, id: int, **kwargs) -> Response:
    """Download a saved report in the user’s account

    You can download all report types (map, scan, patch, authentication, scorecard, remediation, compliance). This option is available when the Report Share feature is enabled in the user’s subscription.

    Args:
        id (int):  (Required) Specifies the report ID of a saved report that you want to download. The status of the report must be “finished”
        **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

    Returns:
        :class:`~requests.Response`: Qualys API response contained within request.Response object
    """
    api_action = "download_saved_report"
    kwargs["id"] = id
    return _api_request(self, api_action, **kwargs)
