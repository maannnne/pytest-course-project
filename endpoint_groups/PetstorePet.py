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

    def edit_pet(self, url, json_file_path, headers = None):
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

    def remove_pet(self, url, pet_id, headers = None):
        """
        Deletes the pet:
            Params:
                url - string: the url for removing the pet,
                pet_id - int: the id of the pet to be deleted,
                headers(optional) - dict: request headers   
        """
        response = self.delete_request(url + "/" + pet_id, headers)
        self.check_status_code(response, 200)
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
