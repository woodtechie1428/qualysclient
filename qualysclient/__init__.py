import requests

from qualysclient.defaults import AUTH_URI, BASE_URI


from qualysclient._util import _api_request

class QualysClient:
    
    def __init__(self, username=None, password=None):
        # TODO throw exception for missing creds
        self.username = username
        self.password = password
        self.s = requests.Session()
        self.s.headers.update({'X-Requested-With':'Qualys Client - Python'})

        if (username):
            self.login(username=username, password=password)

    
    def login(self, username, password):
        payload = {
            'action': 'login',
            'username': username,
            'password': password
        }
        r = self.s.post(AUTH_URI, payload)
        if (r.status_code != 200):
            print('Status:', r.status_code, 'Headers:', r.headers, 'Error Response:', r.content)

    # def login(self, **kwargs):
    #     api_action = 'login'
    #     return _api_request(self, api_action, **kwargs)


    def logout(self):
        payload = {
            'action': 'logout'
        }
        r = self.s.post(AUTH_URI, payload)
        if (r.status_code != 200):
            print('Status:', r.status_code, 'Headers:', r.headers, 'Error Response:', r.content)

    #REPORTS
    def list_reports(self, **kwargs):
        api_action = 'list_reports'
        return _api_request(self, api_action, **kwargs)

    def launch_report(self, **kwargs):
        api_action = 'launch_report'
        return _api_request(self, api_action, **kwargs)

    
    def launch_scorecard(self, **kwargs):
        api_action = 'launch_scorecard'
        return _api_request(self, api_action, **kwargs)
    
    def cancel_running_report(self, **kwargs):
        api_action = 'cancel_running_report'
        return _api_request(self, api_action, **kwargs)
    
    def download_saved_report(self, **kwargs):
        api_action = 'download_saved_report'
        return _api_request(self, api_action, **kwargs)


    #ASSET
    
    def list_ip(self, **kwargs):
        api_action = 'list_ip'
        return _api_request(self, api_action, **kwargs)
    
    def add_ips(self, **kwargs):
        api_action = 'add_ips'
        return _api_request(self, api_action, **kwargs)
    
    def update_ips(self, **kwargs):
        api_action = 'update_ips'
        return _api_request(self, api_action, **kwargs)

    def host_list(self, truncation_limit=10, **kwargs):
        api_action = 'host_list'
        if (kwargs.get('truncation_limit') is None):
            kwargs['truncation_limit'] = truncation_limit
        return _api_request(self, api_action, **kwargs)
    
    def host_list_detection(self, truncation_limit=10, **kwargs):
        api_action = 'host_list_detection'
        if (kwargs.get('truncation_limit') is None):
            kwargs['truncation_limit'] = truncation_limit
        return _api_request(self, api_action, **kwargs)
               
    def excluded_host_list(self, **kwargs):
        api_action = 'update_ips'
        return _api_request(self, api_action, **kwargs)

    def excluded_host_change_history(self, **kwargs):
        api_action = 'update_ips'
        return _api_request(self, api_action, **kwargs)


    #COMPLIANCE

    def compliance_control_list(self, **kwargs):
        api_action = 'compliance_control_list'
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_list(self, **kwargs):
        api_action = 'compliance_policy_list'
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_export(self, **kwargs):
        api_action = 'compliance_policy_export'
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_import(self, **kwargs):
        api_action = 'compliance_policy_import'
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_merge(self, **kwargs):
        api_action = 'compliance_policy_merge'
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_add_asset_group_ids(self, **kwargs):
        api_action = 'compliance_policy_add_asset_group_ids'
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_set_asset_group_ids(self, **kwargs):
        api_action = 'compliance_policy_set_asset_group_ids'
        return _api_request(self, api_action, **kwargs)

    def compliance_policy_add_asset_groups(self, **kwargs):
        api_action = 'compliance_policy_add_asset_groups'
        return _api_request(self, api_action, **kwargs)

    def compliance_posture_list(self, **kwargs):
        api_action = 'compliance_posture_list'
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_list(self, **kwargs):
        api_action = 'compliance_exception_list'
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_request(self, **kwargs):
        api_action = 'compliance_exception_request'
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_update(self, **kwargs):
        api_action = 'compliance_exception_update'
        return _api_request(self, api_action, **kwargs)

    def compliance_exception_delete(self, **kwargs):
        api_action = 'compliance_exception_delete'
        return _api_request(self, api_action, **kwargs)

    


                
    