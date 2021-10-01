from qualysclient._auth_session import AuthSession


class APIEndpoint:
    """
    Base class that other API specific classes are harnessed to.
    """

    def __init__(self, authed_session: AuthSession):
        self.s = authed_session.s
