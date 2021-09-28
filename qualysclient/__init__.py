import requests

from qualysclient.defaults import AUTH_URI


from qualysclient._util import _api_request


class QualysClient:
    """
    a simple client for interacting with the Qualys API
    """

    def __init__(self, username=None, password=None):
        # TODO throw exception for missing creds
        self.username = username
        self.password = password
        self.s = requests.Session()
        self.s.headers.update({"X-Requested-With": "Qualys Client - Python"})

        if username:
            self.login(username=username, password=password)

    def __enter__(self, username=None, password=None):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        import traceback

        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        self.logout()
        del self

    def login(self, username, password):
        """
        Authenticate to Qualys API

        :param username: Qualys Username
        :type username: str
        :param password: Qualys Password
        :type password: str
        """
        if isinstance(username, str) is False or isinstance(password, str) is False:
            raise Exception("username and password is required and must be of type str")

        payload = {"action": "login", "username": username, "password": password}
        r = self.s.post(AUTH_URI, payload)
        if r.status_code != 200:
            print(
                "Status:",
                r.status_code,
                "Headers:",
                r.headers,
                "Error Response:",
                r.content,
            )

        return self

    def logout(self):
        """
        Log out of authenticated sessionn
        """
        payload = {"action": "logout"}
        r = self.s.post(AUTH_URI, data=payload)
        if r.status_code != 200:
            print(
                "\nStatus:",
                r.status_code,
                "\nHeaders:",
                r.headers,
                "\nError Response:",
                r.content,
            )

    # REPORTS
    def list_reports(self, **kwargs):
        """
        View a list of reports in the user’s account when Report Share feature is enabled.
        The report list output includes all report types, including scorecard reports.

        :param id: Report ID
        :type id: int
        :return: (response.status_code, response.content)
        :rtype: (int, Response)
        """

        api_action = "list_reports"
        return _api_request(self, api_action, **kwargs)

    def launch_report(self, **kwargs) -> requests.Response:
        """
        Launch a report in the user's account. The Report Share feature must be enabled in the
        user's subscription. When a report is launched with Report Share, the report is run in the
        background, and the report generation processing does not timeout until the report has
        completed.

        Keyword Args:
            template_id (int):  (Required) The template ID of the report you want to launch.

        Returns:
            requests.Response: raw requests.Response object
        """
        api_action = "launch_report"
        return _api_request(self, api_action, **kwargs)

    def launch_scorecard(self, **kwargs) -> requests.Response:
        """
        Launch a vulnerability scorecard report in the user’s Report Share. It is not possible to
        launch any compliance scorecard reports or WAS scorecard reports using this API at this time.
        When a scorecard report is launched, the report is run in the background, and the report
        generation processing does not timeout until the report has completed.

        Returns:
            requests.Response: raw requests.Response object
        """
        api_action = "launch_scorecard"
        return _api_request(self, api_action, **kwargs)

    def cancel_running_report(self, **kwargs):
        api_action = "cancel_running_report"
        return _api_request(self, api_action, **kwargs)

    def download_saved_report(self, **kwargs):
        api_action = "download_saved_report"
        return _api_request(self, api_action, **kwargs)

    # ASSET

    def list_ip(self, **kwargs):
        api_action = "list_ip"
        return _api_request(self, api_action, **kwargs)

    def add_ips(self, **kwargs):
        api_action = "add_ips"
        return _api_request(self, api_action, **kwargs)

    def update_ips(self, **kwargs):
        api_action = "update_ips"
        return _api_request(self, api_action, **kwargs)

    def host_list(self, truncation_limit=10, **kwargs):
        api_action = "host_list"
        if kwargs.get("truncation_limit") is None:
            kwargs["truncation_limit"] = truncation_limit
        return _api_request(self, api_action, **kwargs)

    def host_list_detection(self, truncation_limit=10, **kwargs):
        api_action = "host_list_detection"
        if kwargs.get("truncation_limit") is None:
            kwargs["truncation_limit"] = truncation_limit
        return _api_request(self, api_action, **kwargs)

    def excluded_host_list(self, **kwargs):
        api_action = "update_ips"
        return _api_request(self, api_action, **kwargs)

    def excluded_host_change_history(self, **kwargs):
        api_action = "update_ips"
        return _api_request(self, api_action, **kwargs)

    # COMPLIANCE

    def compliance_control_list(self, **kwargs):
        api_action = "compliance_control_list"
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_list(self, **kwargs):
        api_action = "compliance_policy_list"
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_export(self, **kwargs):
        api_action = "compliance_policy_export"
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_import(self, **kwargs):
        api_action = "compliance_policy_import"
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_merge(self, **kwargs):
        api_action = "compliance_policy_merge"
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_add_asset_group_ids(self, **kwargs):
        api_action = "compliance_policy_add_asset_group_ids"
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_set_asset_group_ids(self, **kwargs):
        api_action = "compliance_policy_set_asset_group_ids"
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_add_asset_groups(self, **kwargs):
        api_action = "compliance_policy_add_asset_groups"
        return _api_request(self, api_action, **kwargs)

    def compliance_posture_list(self, **kwargs):
        api_action = "compliance_posture_list"
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_list(self, **kwargs):
        api_action = "compliance_exception_list"
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_request(self, **kwargs):
        api_action = "compliance_exception_request"
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_update(self, **kwargs):
        api_action = "compliance_exception_update"
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_delete(self, **kwargs):
        api_action = "compliance_exception_delete"
        return _api_request(self, api_action, **kwargs)
