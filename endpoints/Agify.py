from base.Base import Base


class Agify(Base):

    def get_ages(self, url, params = None, headers = None):
        response = self.get_request(url, params, headers)
        return response
    