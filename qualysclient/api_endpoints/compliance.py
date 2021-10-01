from requests import Response
from qualysclient._util import _api_request
from io import FileIO

from qualysclient._api_endpoint import APIEndpoint

# from . import APIEndpoint


class Compliance(APIEndpoint):
    """Methods for interacting with the Compliance endpoint"""

    def compliance_control_list(self, **kwargs) -> Response:
        """
        View a list of compliance controls which are visible to the user.

        Controls in the XML output are sorted by control ID in ascending order. Optional input parameters support filtering the list.

        Args:
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_
        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_control_list"
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_list(self, **kwargs):
        """
        View a list of compliance policies visible to the user.

        Policies in the XML output are sorted by compliance policy ID in ascending order. Optional input parameters support filtering the policy list output.

        Args:
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_
        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_policy_list"
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_export(self, id: int, **kwargs) -> Response:
        """Export compliance policies from your account to an XML file.

        Service provided controls are exported and you can choose to also export user defined controls. The output also
        includes an appendix with human readable look-ups for control descriptions, giving you
        explanation on the various aspects of control description and evaluation.

        Args:
            id (int): The ID of the policy you want to export
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`:
        """
        api_action = "compliance_policy_export"
        kwargs["id"] = id
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_import(
        self, xml_file: FileIO, title: str, **kwargs
    ) -> Response:
        """Import a compliance policy, defined in an XML file, into your account.

        We’ll include all the service-provided controls from your XML file. You have the option to also include userdefined controls.

        Args:
            xml_file (FileIO): The file containing the policy details.
            title (str): The title of the new policy.
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_policy_import"
        kwargs["title"] = title
        kwargs["xml_file"] = xml_file
        # TODO _api_request doesnt handle uploading files yet
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_merge(
        self, id: int, merge_policy_id: int, **kwargs
    ) -> Response:
        """Merge (combine) 2 or more compliance policies using Qualys Policy Compliance (PC).

        Args:
            id (int): The ID of the policy that will be updated with merged content (let’s call this Policy A).
            merge_policy_id (int): Tell us the policy with the content that will be merged into Policy A (let’s call this Policy B).
            **kwargs : supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_policy_merge"
        kwargs["id"] = id
        kwargs["merge_policy_id"] = merge_policy_id
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_add_asset_group_ids(
        self, id: int, asset_group_ids: str, **kwargs
    ):
        """
        Add asset group IDs to policy

        Args:
            id (int): Policy ID for the policy you want to update
            asset_group_ids (str): Asset groups IDs for the asset groups you want to add to the policy specified in “id”. Multiple IDs are comma separated. Each asset group must have at least 1 assigned IP address.
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_policy_add_asset_group_ids"
        kwargs["id"] = id
        kwargs["asset_group_ids"] = asset_group_ids
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_remove_asset_group_ids(
        self, id: int, asset_group_ids: str, **kwargs
    ):
        """
        Remove asset group IDs from policy

        Args:
            id (int): Policy ID for the policy you want to update
            asset_group_ids (str): Asset groups IDs for the asset groups you want to delete to the policy specified in “id”. Multiple IDs are comma separated. Each asset group must have at least 1 assigned IP address.
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_policy_remove_asset_group_ids"
        kwargs["id"] = id
        kwargs["asset_group_ids"] = asset_group_ids
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_set_asset_group_ids(
        self, id: int, asset_group_ids: str, **kwargs
    ):
        """
        Set asset group IDs for policy

        Use this action to reset the asset groups for a specified policy. Any assigned asset groups not specified in this request will be removed.

        Args:
            id (int): Policy ID for the policy you want to update
            asset_group_ids (str): Asset groups IDs for the asset groups you want to assign to the policy specified in “id”. Multiple IDs are comma separated. Each asset group must have at least 1 assigned IP address.
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_policy_set_asset_group_ids"
        kwargs["id"] = id
        kwargs["asset_group_ids"] = asset_group_ids
        return _api_request(self, api_action, **kwargs)

    def compliance_posture_list(self, policy_id: int, **kwargs):
        """
        View current compliance posture data (info records) for hosts within the user’s account.

        Each compliance posture info record includes a compliance posture ID and other attributes. Optional input parameters support filtering the posture info record output. .

        Args:
            policy_id (int): Show compliance posture info records for a specified policy. A valid policy ID is required.
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_posture_list"
        kwargs["policy_id"] = policy_id
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_list(self, **kwargs):
        """
        List, request, update and delete exceptions in your account.

        By default, all exceptions in the user’s account are listed. Use the optional parameters to filter the list output

        Args:
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_exception_list"
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_request(
        self,
        control_id: int,
        host_id: int,
        policy_id: int,
        technology_id: int,
        assignee_id: str,
        comments: str,
        **kwargs
    ):
        """An exception is created with the expiry date matching the creation date.

        Args:
            control_id (int): Specify the control ID of the control for which you want to request an exception.
            host_id (int): Specify the host ID of the host for which you want to request an exception.
            policy_id (int): Specify the policy ID of the policy that contains the control for which you want to request an exception.
            technology_id (int): Specify the technology ID of the technology associated with the host for which you want to request an exception.
            assignee_id (str):  You can assign exception to another user. Specify user ID of the user, who has access to the hosts that the exceptions apply to.
            comments (str): User defined comments.
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_exception_request"
        kwargs["control_id"] = control_id
        kwargs["host_id"] = host_id
        kwargs["policy_id"] = policy_id
        kwargs["technology_id"] = technology_id
        kwargs["assignee_id"] = assignee_id
        kwargs["comments"] = comments
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_update(
        self, exception_numbers: str, comments: str, **kwargs
    ):
        """Update Exception(s)

        Args:
            exception_numbers (str):   Show a specific exception by specifying a valid exception number. Multiple entries are comma separated. An exception number range is specified with a hyphen (for example, 50-55).
            comments (str): User defined comments.
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_exception_update"
        kwargs["exception_numbers"] = exception_numbers
        kwargs["comments"] = comments
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_delete(self, exception_numbers: str, **kwargs):
        """Delete Exception(s)

        Args:
            exception_numbers (str):   Show a specific exception by specifying a valid exception number. Multiple entries are comma separated. An exception number range is specified with a hyphen (for example, 50-55).
            **kwargs: supported keywords documented within the `Qualys VM/PC API user guide <https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf>`_

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "compliance_exception_delete"
        return _api_request(self, api_action, **kwargs)
