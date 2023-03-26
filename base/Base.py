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

    #PUT method
    def put_request(self, url, json_file_path, headers = None):
        request_json = self.load_json_file(json_file_path)
        response = requests.put(url, json = request_json, headers = headers, verify = False)
        return response

    #PATCH method
    def patch_request(self, url, json_file_path, headers = None):
        request_json = self.load_json_file(json_file_path)
        response = requests.patch(url, json = request_json, headers = headers, verify = False)
        return response

    #DELETE method 
    def delete_request(self, url, headers = None):
        response = requests.delete(url, headers = headers, verify = False)
        return response

    # additionals
    def load_json_file(self, json_file_path):
        """
        Loads the json file
        prepares it as a payload
            Params:
                json_file_path: the file path of the json file, which should be loaded as a payload 
        """
        with open(json_file_path, "r") as file:
            payload = json.load(file)
            return payload  

    def check_status_code(self, response, status_code):
        """
        Checks the status code
            Params:
                response: the response object
                status_code: the expected status code
        """
        assert response.status_code == status_code 

    def get_response_key_value(self, response, key_json_path):
        """
        Gets a specific key's value from the response body and returns the value, using json path
            Params:
                response: the response object
                key_json_path: the json path of the corresponsing key (e.g "category.id")
        """
        response_json = response.json()
        json_exp = parse(f'$.{key_json_path}')
        match = json_exp.find(response_json)
        return match[0].value

    def check_response_key_value(self, response, key_json_path, expected_value):
        """
        Checks a specific key's value from the response body, using json path
            Params: 
                response: the response object
                key_json_path: the json path of the corresponding key (e.g "category.id")
                expected_value: the expected value of the corresponding key
        """
        response_json = response.json()
        json_exp = parse(f'$.{key_json_path}')
        match = json_exp.find(response_json)
        assert match[0].value == expected_value

    def edit_request_key_value(self, json_file_path, key_json_path, changed_value):
        """
        Changes a specific key's value, using json path
            Params: 
                json_file_path: the response object
                key_json_path: the json path of the corresponding key (e.g "category.id")
                changed_value: the value you want the corresponding key to have

        """
        request_json = self.load_json_file(json_file_path)

        json_exp = parse(f'$.{key_json_path}')
        match = json_exp.find(request_json)
        match[0].value = changed_value
        json_exp.update(request_json, match[0].value)

        with open(json_file_path, "w") as file:
            json.dump(request_json, file)

