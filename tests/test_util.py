from qualysclient import QualysClient, _util
from qualysclient.defaults import BASE_URI
import pytest
import requests
import responses

def test_validate_parameters_api_action_as_None():
    with pytest.raises(Exception) as e_info:
        tr = _util._validate_parameters(None,ip=5)
    # assert tr in [True, False]

def test_validate_parameters_api_action_valid():
    tr = _util._validate_parameters('launch_report',id=5)
    assert tr in [True, False]

def test_validate_parameters_api_action_invalid():
    tr = _util._validate_parameters('invalid_name',id=5)
    assert tr in [True, False]

def test_validate_parameters_kwargs():
    tr = _util._validate_parameters('list_ip',simple=5)
    assert tr in [True, False]
    tr = _util._validate_parameters('launch_report',template_id=5)
    assert tr in [True, False]

@responses.activate
def test_perform_request():
    responses.add(
        responses.POST,
        BASE_URI+'/api/2.0/fo/report/?action=list',
        body = "someting went wrong",
        status= 404
    )
    
    tr = _util._perform_request(QualysClient(),BASE_URI+'/api/2.0/fo/report/?action=list', input_params={'k':'v'})
    assert tr.status_code == 404
