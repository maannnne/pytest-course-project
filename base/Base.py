import os
import jsonpath as jsn
import requests
import json
from jsonpath_ng import jsonpath, parse

class Base:

    # GET method
    def get_request(self, url, params = None, headers = None):
        response = requests.get(url, params = params, headers = headers, verify = False)
        return response

    # POST method
    def post_request(self, url, json = None, headers = None): 
        response = requests.post(url, json = json, headers = headers, verify = False)
        return response          
