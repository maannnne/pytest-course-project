import logging as logger
from pytest import mark
from base.Base import *
from endpoint_groups.PetstorePet import PetstorePet


post_pet_endpoint = "/pet"
put_pet_endpoint = "/pet"
new_pet_payload = "jsons\\new_pet.json"
edit_pet_payload = "jsons\\edit_pet.json"
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
    pet.edit_POST_pet_endpoint_payload(new_pet_payload, "category.name", "dog")
    res = pet.add_pet(add_pet_url, new_pet_payload, headers)
    logger.debug(f"TEST RESULT: Newly added pet: {res}")

@mark.petstore
def test_edit_pet(app_config):
    logger.info("TEST STEP: Edit created pet")
    edit_pet_url = app_config.base_url + put_pet_endpoint
    pet.edit_PUT_pet_endpoint_payload(edit_pet_payload, "category.name", "utyutyu")
    res = pet.edit_pet(edit_pet_url, edit_pet_payload, headers)
