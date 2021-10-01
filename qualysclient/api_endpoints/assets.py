from requests import Response
from qualysclient._util import _api_request

from qualysclient._api_endpoint import APIEndpoint

# from . import APIEndpoint


class Assets(APIEndpoint):
    """methods for interacting with the Assets endpoint"""

    def list_ip(self, **kwargs) -> Response:
        """List IP addresses in the user account. By default, all hosts in the user account are included.

        Optional input parameters support filtering the list by IP addresses and host tracking method.

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "list_ip"
        return _api_request(self, api_action, **kwargs)

    def add_ips(self, **kwargs) -> Response:
        """Add IP addresses to the user's subscription.

        Once added they are available for scanning and reporting.

        Args:
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "add_ips"
        return _api_request(self, api_action, **kwargs)

    def update_ips(self, ips: str, **kwargs) -> Response:
        """Update IP addresses in the user's subscription.

        Args:
            ips (str): (Required) The hosts within the subscription you want to update. IPs must be specified by using the “ips” parameter (using the POST method)
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object

        Example:
            ips=10.10.10.200,10.10.23.40
        """
        api_action = "update_ips"
        kwargs["ips"] = ips
        return _api_request(self, api_action, **kwargs)

    def host_list(self, truncation_limit=10, **kwargs):
        """
        Download a list of scanned hosts in the user’s account

        By default, all scanned hosts in the user account are included and basic information about each host is provided. Hosts in the XML output are sorted by host ID in ascending order.

        The output of the Host List API is paginated. By default, a maximum of 1,000 host records are returned per request. You can customize the page size (i.e. the number of host records) by using the parameter “truncation_limit=10000” for instance. In this case the results will be return with pages of 10,000 host records.

        Args:
            truncation_limit (int, optional): Specifies the maximum number of host records processed per request. Defaults to 10.
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "host_list"
        if kwargs.get("truncation_limit") is None:
            kwargs["truncation_limit"] = truncation_limit
        return _api_request(self, api_action, **kwargs)

    def host_list_detection(self, truncation_limit=10, **kwargs):
        """
        Download a list of hosts with the hosts latest vulnerability data, based on the host based scan data available in the user’s account.

        This data brings a lot of value to customers because they provide the latest complete vulnerability status for the hosts (NEW, ACTIVE, FIXED, REOPENED) and history information.

        Args:
            truncation_limit (int, optional): Specifies the maximum number of host records processed per request. Defaults to 10.
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "host_list_detection"
        if kwargs.get("truncation_limit") is None:
            kwargs[
                "truncation_limit"
            ] = truncation_limit  # TODO #11 needs pagination support
        return _api_request(self, api_action, **kwargs)

    def excluded_host_list(self, **kwargs):
        """
        Show the excluded host list for the user's account.

        Hosts in your excluded host list will not be scanned.

        Args:
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "update_ips"
        return _api_request(self, api_action, **kwargs)

    def excluded_host_change_history(self, **kwargs):
        """
        View change history for excluded hosts in the user’s subscription.

        History record IDs in the XML output are listed in decreasing order.

        Args:
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "excluded_host_change_history"
        return _api_request(self, api_action, **kwargs)
