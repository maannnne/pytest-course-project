import os
import jsonpath as jsn
import requests
import json
from jsonpath_ng import jsonpath, parse

class Base:

    def get_request(self, url, params = None, headers = None):
        response = requests.get(url, params = params, headers = headers, verify = False)
        return response
