from .assets import Assets
from .reports import Reports
from .compliance import Compliance
from ._auth_session import AuthSession


class QualysClient(AuthSession):
    """
    a simple client for interacting with the Qualys API
    """

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        super(QualysClient, self).__init__(
            username=self.username, password=self.password
        )

    def __enter__(self, username=None, password=None):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        import traceback

        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        self.logout()
        del self

    @property
    def reports(self):
        """
        The interface object for the :doc:`Reports API <qualysclient.reports.Reports>`
        """
        return Reports(self)

    @property
    def compliance(self):
        """
        The interface object for the :doc:`Compliance API <qualysclient.compliance.Compliance>`
        """
        return Compliance(self)

    @property
    def assets(self):
        """
        The interface object for the :doc:`Assets API <qualysclient.assets.Assets>`
        """
        return Assets(self)
