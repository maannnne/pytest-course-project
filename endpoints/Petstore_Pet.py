from base.Base import Base


class Petstore_Pet(Base):

    def add_pet(self, url, json_file_path, headers = None):
        response = self.post_request(url, json_file_path, headers)
        self.check_status_code(response, 200)
        id = self.get_response_key_value(response, "id")
        return id
    