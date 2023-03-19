from base.Base import Base


class Petstore_Pet(Base):

    def add_pet(self, url, json, headers = None):
        response = self.post_request(url, json, headers)
        return response
    