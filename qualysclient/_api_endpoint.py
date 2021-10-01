from requests import Session


class APIEndpoint:
    """
    Base class that other API specific classes are harnessed to.
    """

    def __init__(self, shared_session: Session):
        self.s = shared_session
