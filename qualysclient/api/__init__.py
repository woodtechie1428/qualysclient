"""API Module"""

from qualysclient._api_endpoint import APIEndpoint
from qualysclient.api.vmpc.reports import Reports
from qualysclient.api.vmpc.assets import Assets
from qualysclient.api.vmpc.compliance import Compliance
from qualysclient.api.vmpc.scan_configuration import ScanConfiguration


class VMPCApi(APIEndpoint):
    "Class Interface to Qualys VM & PC API"

    @property
    def reports(self) -> Reports:
        """
        The interface object for the :doc:`Reports API <qualysclient.api.vmpc.reports.Reports>`
        """
        return Reports(shared_session=self.s)

    @property
    def compliance(self) -> Compliance:
        """
        The interface object for the :doc:`Compliance API <qualysclient.api.vmpc.compliance.Compliance>`
        """
        return Compliance(shared_session=self.s)

    @property
    def assets(self) -> Assets:
        """
        The interface object for the :doc:`Assets API <qualysclient.api.vmpc.assets.Assets>`
        """
        return Assets(shared_session=self.s)

    @property
    def scan_configuration(self) -> ScanConfiguration:
        """
        The interface object for the :doc:`Scan Configuration API <qualysclient.api.vmpc.scan_configuration.ScanConfiguration>`
        """
        return ScanConfiguration(shared_session=self.s)
