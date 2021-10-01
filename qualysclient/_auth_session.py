from requests import Session
from qualysclient._defaults import AUTH_URI


class AuthSession:
    """
    Authenticates to Qualys API
    """

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.s = Session()
        self.s.headers.update({"X-Requested-With": "Qualys Client - Python"})

        if username:
            self.login(username=username, password=password)

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
