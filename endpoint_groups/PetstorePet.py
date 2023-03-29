from base.Base import Base
import logging as logger


class PetstorePet(Base):

    # ADD/ EDIT/ REMOVE PETS
    def add_pet(self, url, json_file_path, headers = None):
        """
        Creates a pet
            Params:
                url - string: the url for creating the pet,
                json_file_path - string: the payload json file path
                headers(optional) - dict: request headers
        """
        response = self.post_request(url, json_file_path, headers)
        self.check_status_code(response, 200)
        #logger.debug(f'Pet added: {response.json()}')
        return response.json()

    def edit_pet_put(self, url, json_file_path, headers = None):
        """
        Edits the pet
            Params:
                url - string: the url for editing the pet,
                json_file_path - string: the payload json file path
                headers(optional) - dict: request headers
        """
        response = self.put_request(url, json_file_path, headers)
        self.check_status_code(response, 200)
        #logger.debug(f'Pet edited with put: {response.json()}')
        return response.json()


    # GET PETS
    def get_pet_by_id(self, url, params = None, headers = None):
        """
        Gets the pet by id
            Params:
                url - string: the url for getting the pet (id included)
                params(optional) - dict: request query params
                headers(optional) - dict: request headers
        """
        response = self.get_request(url, params, headers)
        self.check_status_code(response, 200)
        #logger.debug(f'Pet info: {response.json()}')
        return response.json()

    def get_pets_by_status(self, url, params, headers = None):
        """
        Gets the pet by status
            Params:
                url - string: the url for getting the pet (id included)
                params - dict: request query params
                headers(optional) - dict: request headers
        """
        response = self.get_pet_by_id(url, params, headers)
        self.check_status_code(response, 200)
        #logger.debug(f'Pets by status: {response.json()}')
        return response.json()


    # GET DATA FROM RESPONSE
    def get_key_value_from_response(self, response, key_path):
        """
        Gets the value of the specified key
            Params:
                response - dict: the response of the request
                key_path - string: the corresponding key
        """
        return self.get_response_key_value(response, key_path)


    # PAYLOAD
    def edit_POST_pet_endpoint_payload(self, json_file_path, key_path, new_value):
        """
        Changes key values for the specified request payload:
            Params:
                json_file_path - dict: the path of the json, that should be used as a payload
                key_path - string: the corresponding key path
                new_value - string: the new value of the corresponding key
        """
        self.edit_request_key_value(json_file_path, key_path, new_value)

    def edit_PUT_pet_endpoint_payload(self, json_file_path, key_path, new_value):
        """
        Changes key values for the specified request payload:
            Params:
                json_file_path - dict: the path of the json, that should be used as a payload
                key_path - string: the corresponding key path
                new_value - string: the new value of the corresponding key
        """
        self.edit_request_key_value(json_file_path, key_path, new_value)

    def edit_PATCH_pet_endpoint_payload(self, json_file_path, key_path, new_value):
        """
        Changes key values for the specified request payload:
            Params:
                json_file_path - dict: the path of the json, that should be used as a payload
                key_path - string: the corresponding key path
                new_value - string: the new value of the corresponding key
        """
        self.edit_request_key_value(json_file_path, key_path, new_value)
