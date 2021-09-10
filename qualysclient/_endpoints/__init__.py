from ._ep_reports import _reports_endpoints 
from ._ep_assets import _assets_endpoints
from ._ep_compliance import _compliance_endpoints
from ._ep_session import _session_endpoints
from .endpoint import APIAction

api_actions = {}


all_endpoints = [*_reports_endpoints, 
                *_assets_endpoints,
                *_compliance_endpoints,
                *_session_endpoints]

for a in all_endpoints:
    api_actions[a[0]]  = APIAction(a[0],
        api_endpoint=a[1],
        input_params=a[2]
        )
