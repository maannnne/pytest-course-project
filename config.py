class Config:
    def __init__(self, env):

        #the environments that are supported
        SUPPORTED_ENVS = ['localhost', 'vm']

        #check if the environment is not supported, raise an exception
        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f'Exception: {env} is not a supported environment (supported envs: {SUPPORTED_ENVS})')

        #the dictionary for supported environments
        self.base_url = {
            'localhost': 'https://localhost:4450', 
            'vm': 'https://0.0.0.0:4450'
        }[env]
        