from requests import Session


class AuthSession:
    """
    Authenticates to Qualys API
    """

    def __init__(self, shared_session: Session):
        self.s = shared_session
