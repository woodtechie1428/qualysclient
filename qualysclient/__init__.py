from .assets import Assets
from .reports import Reports
from .compliance import Compliance
from ._auth_session import AuthSession

from requests import Session
from qualysclient._defaults import AUTH_URI


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

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.s = Session()
        self.s.headers.update({"X-Requested-With": "Qualys Client - Python"})

        super(QualysClient, self).__init__(self.s)
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
        print("login called")
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
