import logging as logger
from pytest import mark
from base.Base import *
from endpoint_groups.PetstorePet import PetstorePet

# endpoints
post_pet_endpoint = "/pet"
put_pet_endpoint = "/pet"
patch_pet_endpoint = "/pet"

# paylaods
new_pet_payload = "jsons/new_pet.json"
patch_pet_payload = "jsons/edit_pet_patch.json"
put_pet_payload = "jsons/edit_pet_put.json"
headers = {'Content-Type': 'application/json'}

# class objects
pet = PetstorePet()
base = Base()

# globals
pet_id = 0


@mark.petstore
@mark.dependency()
def test_env_is_petstore(app_config):
    """
    Check that the test environment is correctly set to "petstore"
    """
    logger.info("TEST STEP: Check the environment is correctly set.")
    base_url = app_config.base_url
    expected_url = "https://petstore.swagger.io/v2"
    assert base_url == expected_url, \
    f"Expected ~~{expected_url}~~ but got ~~{base_url}~~"

@mark.petstore
@mark.dependency(depends = ["test_env_is_petstore"])
def test_add_pet(app_config):
    """
    Add a pet, check that the pet was created with the specified data
    """
    logger.info("TEST STEP: Add a new pet.")
    add_pet_url = app_config.base_url + post_pet_endpoint
    pet.edit_POST_pet_endpoint_payload(new_pet_payload, "category.name", "dog")
    res = pet.add_pet(add_pet_url, new_pet_payload, headers)
    global pet_id
    pet_id = pet.get_key_value_from_response(res, "id")

@mark.petstore
@mark.dependency(depends = ["test_env_is_petstore", "test_add_pet"])
def test_edit_pet_put(app_config):
    logger.info("TEST STEP: Edit created pet with put")
    edit_pet_url = app_config.base_url + put_pet_endpoint
    pet.edit_PUT_pet_endpoint_payload(put_pet_payload, "id", pet_id)
    pet.edit_PUT_pet_endpoint_payload(put_pet_payload, "category.name", "edited category - cat")
    res = pet.edit_pet_put(edit_pet_url, put_pet_payload, headers)
