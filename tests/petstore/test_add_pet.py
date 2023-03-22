import logging as logger
from pytest import mark
from base.Base import *
from endpoint_groups.Petstore_Pet import Petstore_Pet


post_pet_endpoint = '/pet'
json_file_path = 'jsons\\new_pet.json'
headers = {'Content-Type': 'application/json'}

@mark.petstore
def test_env_is_petstore(app_config):
    logger.info("TEST: Check the environment is correctly set.")
    base_url = app_config.base_url
    assert base_url == 'https://petstore.swagger.io/v2'

@mark.petstore
def test_add_pet(app_config):
    logger.info("TEST: Add a new pet.")
    petstore_pet = Petstore_Pet()
    add_pet_url = app_config.base_url + post_pet_endpoint
    res = petstore_pet.add_pet(add_pet_url, json_file_path, headers)
    
