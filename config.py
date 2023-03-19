class Config:
    def __init__(self, env):

        #the environments that are supported
        SUPPORTED_ENVS = ['agify', 'petstore']

        #check if the environment is not supported, raise an exception
        if env not in SUPPORTED_ENVS:
            raise Exception(f'Exception: \'{env}\' is not a supported environment (supported envs: {SUPPORTED_ENVS})')

        #the dictionary for supported environments
        self.base_url = {
            'agify': 'https://api.agify.io', 
            'petstore': 'https://petstore.swagger.io/v2',
        }[env]
        