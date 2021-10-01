from requests import Response
from qualysclient._util import _api_request, _perform_request
from qualysclient._api_endpoint import APIEndpoint


class ScanConfiguration(APIEndpoint):
    """methods to interact with the scan configuration endpoints"""

    def list_knowledgebase(self, **kwargs) -> Response:
        """Download a list of vulnerabilities from Qualys’ KnowledgeBase.

        Several input parameters grant users control over which vulnerabilities to download and the amount of detail to download, and the XML output provides a rich information source for each vulnerability.

        Returns:
            :class:`~requests.Response`: Qualys API response contained within request.Response object
        """
        api_action = "list_knowledgebase"
        return _api_request(self, api_action, **kwargs)
