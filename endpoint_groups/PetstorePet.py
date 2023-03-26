from base.Base import Base
import logging as logger


class PetstorePet(Base):

    def add_pet(self, url, json_file_path, headers = None):
        response = self.post_request(url, json_file_path, headers)
        self.check_status_code(response, 200)
        #id = self.get_response_key_value(response, "category.name")
        logger.debug(f'Pet added: {response.json()}')
        return response.json()

    def edit_pet_put(self, url, json_file_path, headers = None):
        response = self.put_request(url, json_file_path, headers)
        self.check_status_code(response, 200)
        logger.debug(f'Pet edited with put: {response.json()}')
        return response.json()
    
    def edit_pet_patch(self, url, json_file_path, headers = None):
        response = self.patch_request(url, json_file_path, headers)
        self.check_status_code(response, 200)
        logger.debug(f'Pet edited with patch: {response.json()}')
        return response.json()

    def get_pet_by_id(self, url, params = None, headers = None):
        response = self.get_request(url, params, headers)
        self.check_status_code(response, 200)
        logger.debug(f'Pet info: {response.json()}')
        return response.json()

    def get_pets_by_status(self, url, params, headers = None):
        response = self.get_pet_by_id(url, params, headers)
        self.check_status_code(response, 200)
        logger.debug(f'Pets by status: {response.json()}')
        return response.json()
    
    def get_key_value_from_response(self, response, key_path):
        key_value = self.get_response_key_value(response, key_path)
        return key_value

    def edit_POST_pet_endpoint_payload(self, json_file_path, key_path, new_value):
        self.edit_request_key_value(json_file_path, key_path, new_value)

    def edit_PUT_pet_endpoint_payload(self, json_file_path, key_path, new_value):
        self.edit_request_key_value(json_file_path, key_path, new_value)

    def edit_PATCH_pet_endpoint_payload(self, json_file_path, key_path, new_value):
        self.edit_request_key_value(json_file_path, key_path, new_value)