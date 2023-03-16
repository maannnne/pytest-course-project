from pytest import mark
from base.Base import *
from endpoints.Agify import Agify
from pytest import mark

get_ages_endpoint = '/'
get_ages_params  = 'name=michael'


@mark.agify
def test_get_ages(app_config):
    agify = Agify()
    get_ages_url = app_config.base_url + get_ages_endpoint
    res = agify.get_ages(get_ages_url, get_ages_params)
    print(f'The url we called to: #{res.url}')
    print(f'The respose code: #{res}')
    print(f'The response body: #{res.text}')
