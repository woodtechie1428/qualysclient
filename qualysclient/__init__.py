
from aiohttp import payload
from qualysclient.defaults import AUTH_URI
import requests


class QualysClient(object):
    
    def __init__(self, username, password):

        self.s = requests.Session()
        self.s.headers.update({'X-Requested-With':'Qualys Client - Python'})

        payload = {
            'action': 'login',
            'username': username,
            'password': password
        }

        self.login(payload)

    
    def login(self, payload):
        r = self.s.post(AUTH_URI, payload)
        if (r.status_code != 200):
            print('Status:', r.status_code, 'Headers:', r.headers, 'Error Response:', r.content)

    def logout(self):
        payload = {
            'action': 'logout'
        }
        r = self.s.post(AUTH_URI, payload)
        if (r.status_code != 200):
            print('Status:', r.status_code, 'Headers:', r.headers, 'Error Response:', r.content)
