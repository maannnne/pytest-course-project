import logging as logger
from pytest import mark
from base.Base import *
from endpoint_groups.PetstorePet import PetstorePet


post_pet_endpoint = "/pet"
json_file_path = "jsons\\new_pet.json"
headers = {'Content-Type': 'application/json'}
pet = PetstorePet()
base = Base()

@mark.petstore
def test_env_is_petstore(app_config):
    logger.info("TEST STEP: Check the environment is correctly set.")
    base_url = app_config.base_url
    expected_url = "https://petstore.swagger.io/v2"
    assert base_url == expected_url, \
    f"Expected ~~{expected_url}~~ but got ~~{base_url}~~"

@mark.petstore
def test_add_pet(app_config):
    logger.info("TEST STEP: Add a new pet.")
    add_pet_url = app_config.base_url + post_pet_endpoint
    pet.edit_POST_pet_endpoint_payload(json_file_path, "category.name", "dog")
    res = pet.add_pet(add_pet_url, json_file_path, headers)
    logger.debug(f"TEST RESULT: Newly added pet: {res}")
