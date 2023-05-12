from base.Base import Base
import logging as logger


class PetstorePet(Base):

    # ADD PET
    def add_pet(self, url, json_file_path, headers = None):
        """
        Creates a pet
            Params:
                url - string: the url for creating the pet
                json_file_path - string: the payload json file path
                headers(optional) - dict: request headers
        """
        response = self.post_request(url, json_file_path, headers)
        self.check_status_code(response, 200)
        logger.debug(f'Pet added: {response.json()}')
        return response.json()

    # EDIT PET
    def edit_pet(self, url, json_file_path, headers = None):
        """
        Edits the pet
            Params:
                url - string: the url for editing the pet
                json_file_path - string: the payload json file path
                headers(optional) - dict: request headers
        """
        response = self.put_request(url, json_file_path, headers)
        self.check_status_code(response, 200)
        logger.debug(f'Pet edited with put: {response.json()}')
        return response.json()

    # DELETE PET
    def delete_pet(self, url, pet_id, headers = None):
        """
        Deletes the pet:
            Params:
                url - string: the url for removing the pet
                pet_id - int: the id of the pet to be deleted
                headers(optional) - dict: request headers   
        """
        response = self.delete_request(f"{url}/{pet_id}", headers)
        self.check_status_code(response, 200)
        return response.json()


    # GET PETS BY ID
    def get_pet_by_id(self, url, pet_id, params = None, headers = None):
        """
        Gets the pet by id
            Params:
                url - string: the url for getting the pet
                pet_id - int: the id of the pet
                params(optional) - dict: request query params
                headers(optional) - dict: request headers
        """
        response = self.get_request(f"{url}/{pet_id}", params, headers)
        self.check_status_code(response, 200)
        logger.debug(f'Pet info: {response.json()}')
        return response.json()

    # GET DELETED PET
    def get_deleted_pet(self, url, pet_id, params = None, headers = None):
        """
        Gets the pet after deletion
            Params:
                url - string: the url for getting the pet
                pet_id - int: the id of the pet you deleted
                params(optional) - dict: request query params
                headers(optional) - dict: request headers
        """
        response = self.get_request(f"{url}/{pet_id}", params, headers)
        self.check_status_code(response, 404)
        logger.debug(f'Pet not found response body: {response.json()}')
        return response.json()
    
