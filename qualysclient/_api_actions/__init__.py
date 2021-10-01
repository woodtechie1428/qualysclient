from .vmpc._actions_reports import _reports_actions
from .vmpc._actions_assets import _assets_actions
from .vmpc._actions_compliance import _compliance_actions
from .vmpc._actions_scan_configuration import _scan_configuration_actions
from .vmpc._actions_session import _session_actions
from .._models import APIAction

api_actions = {}


all_endpoints = [
    *_reports_actions,
    *_assets_actions,
    *_compliance_actions,
    *_session_actions,
    *_scan_configuration_actions,
]

for a in all_endpoints:
    api_actions[a[0]] = APIAction(a[0], api_endpoint=a[1], input_params=a[2])
