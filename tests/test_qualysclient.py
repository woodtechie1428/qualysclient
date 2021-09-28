from requests.sessions import session
from requests.exceptions import SSLError, Timeout
from qualysclient import QualysClient
from qualysclient.defaults import BASE_URI
import pytest
import requests
import responses
from unittest.mock import Mock


def test_login_non_str_inputs():
    with pytest.raises(Exception):
        qc = QualysClient(username="abc", password=5)
    with pytest.raises(Exception):
        qc = QualysClient(username=5, password="def")
