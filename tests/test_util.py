from requests.sessions import session
from requests.exceptions import SSLError, Timeout
from qualysclient import QualysClient, _util
from qualysclient.defaults import BASE_URI
import pytest
import requests
import responses
from unittest.mock import Mock


def test_validate_parameters_api_action_as_None():
    with pytest.raises(Exception) as e_info:
        tr = _util._validate_parameters(None, ip=5)
    # assert tr in [True, False]


def test_validate_parameters_api_action_valid():
    tr = _util._validate_parameters("launch_report", id=5)
    assert tr in [True, False]


def test_validate_parameters_api_action_invalid():
    with pytest.raises(Exception) as e_info:
        tr = _util._validate_parameters("invalid_name", id=5)


def test_validate_parameters_kwargs():
    tr = _util._validate_parameters("list_ip", simple=5, st=7)
    assert tr in [True, False]
    tr = _util._validate_parameters("launch_report", template_id=5)
    assert tr in [True, False]


@responses.activate
def test_perform_request():
    responses.add(
        responses.POST,
        BASE_URI + "/api/2.0/fo/report/?action=list",
        body="someting went wrong",
        status=404,
    )

    tr = _util._perform_request(
        QualysClient(),
        BASE_URI + "/api/2.0/fo/report/?action=list",
        input_params={"k": "v"},
    )
    assert tr.status_code == 404


@pytest.fixture
def qc():
    q = Mock()
    # q.s.post.side_effect = exception_type
    return q


def test_perform_request_connection_timeout(qc):
    qc.s.post.side_effect = Timeout
    with pytest.raises(Timeout) as e_info:
        tr = _util._perform_request(
            qc, BASE_URI + "/api/2.0/fo/report/?action=list", input_params={"k": "v"}
        )


def test_perform_request_SSLError(qc):
    qc.s.post.side_effect = SSLError
    with pytest.raises(requests.exceptions.SSLError) as e_info:
        tr = _util._perform_request(
            qc, BASE_URI + "/api/2.0/fo/report/?action=list", None
        )


def test_perform_request_ConnectionError(qc):
    qc.s.post.side_effect = requests.ConnectionError
    with pytest.raises(requests.ConnectionError) as e_info:
        tr = _util._perform_request(
            qc, BASE_URI + "/api/2.0/fo/report/?action=list", None
        )


def test_perform_request_TooManyRedirects(qc):
    qc.s.post.side_effect = requests.TooManyRedirects
    with pytest.raises(requests.TooManyRedirects) as e_info:
        tr = _util._perform_request(
            qc, BASE_URI + "/api/2.0/fo/report/?action=list", None
        )


def test_perform_request_URLRequired(qc):
    qc.s.post.side_effect = requests.URLRequired
    with pytest.raises(requests.URLRequired) as e_info:
        tr = _util._perform_request(
            qc, BASE_URI + "/api/2.0/fo/report/?action=list", None
        )


def test_api_request_validation_fail(mocker):
    # mocker.patch('qualysclient._util._perform_request',
    #              return_value = True)

    with pytest.raises(Exception) as e_info:
        actual = _util._api_request(
            QualysClient(),
            BASE_URI + "/api/2.0/fo/report/?action=list",
            input_params={"k": "v"},
        )
    # assert expected == actual


def test_api_request_validation_pass(mocker):
    mocker.patch("qualysclient._util._perform_request", return_value=True)

    expected = True
    actual = _util._api_request(QualysClient(), "launch_report", template_id=5)
    assert expected == actual
