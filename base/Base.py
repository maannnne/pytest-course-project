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
    def post_request(self, url, json_file_path = None, headers = None): 
        request_json = self.load_json_file(json_file_path)
        response = requests.post(url, json = request_json, headers = headers, verify = False)
        return response    

    # additionals
    def load_json_file(self, json_file_path):
        with open(json_file_path, "r") as file:
            payload = json.load(file)
            return payload  

    def check_status_code(self, response, status_code):
        assert response.status_code == status_code 

    def get_response_key_value(self, response, key_name):
        response_json = response.json()
        val = response_json[key_name]
        return val

    def check_response_key_value(self, response, key_json_path, expected_value):
        response_json = response.json()
        
        actual_value = response_json[x]
        assert actual_value == expected_value
