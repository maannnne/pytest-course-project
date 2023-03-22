from base.Base import Base
import logging as logger


class Petstore_Pet(Base):

    def add_pet(self, url, json_file_path, headers = None):
        response = self.post_request(url, json_file_path, headers)
        self.check_status_code(response, 200)
        id = self.get_response_key_value(response, "category.name")
        logger.debug(f'Pet added: {response.json()}')
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
