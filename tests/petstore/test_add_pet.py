import logging as logger
from pytest import mark
from base.Base import *
from endpoint_groups.PetstorePet import PetstorePet

# endpoints
post_pet_endpoint = "/pet"
put_pet_endpoint = "/pet"
delete_pet_endpoint = "/pet" #/pet/{id} 
get_pet_endpoint = "/pet" #/pet/{id}

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
pet_name = "Lucy"
category_name = "cat"
tag_name = "black"
pet_status = "available"


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

    logger.info("TEST STEP: ")
    add_pet_url = app_config.base_url + post_pet_endpoint
    base.edit_request_key_value(new_pet_payload, "name", pet_name)
    base.edit_request_key_value(new_pet_payload, "category.name", category_name)
    base.edit_request_key_value(new_pet_payload, "tags[0].name", tag_name)
    base.edit_request_key_value(new_pet_payload, "status", pet_status)

    res = pet.add_pet(add_pet_url, new_pet_payload, headers)

    global pet_id
    pet_id = base.get_response_key_value(res, "id")
    response_pet_name = base.get_response_key_value(res, "name")
    response_category_name = base.get_response_key_value(res, "category.name")
    response_tag_name = base.get_response_key_value(res, "tags[0].name")
    response_pet_status = base.get_response_key_value(res, "status")


    assert response_pet_name == pet_name, \
    f"Expected ~~{pet_name}~~ but got ~~{response_pet_name}~~"
    assert response_category_name == category_name, \
    f"Expected ~~{category_name}~~ but got ~~{response_category_name}~~"
    assert response_tag_name == tag_name, \
    f"Expected ~~{tag_name}~~ but got ~~{response_tag_name}~~"
    assert response_pet_status == pet_status, \
    f"Expected ~~{pet_status}~~ but got ~~{response_pet_status}~~"
    
    
    



# @mark.petstore
# @mark.dependency(depends = ["test_env_is_petstore", "test_add_pet"])
# def test_edit_pet_put(app_config):
#     logger.info("TEST STEP: Edit created pet with put")
#     edit_pet_url = app_config.base_url + put_pet_endpoint
#     base.edit_request_key_value(put_pet_payload, "id", pet_id)
#     base.edit_request_key_value(put_pet_payload, "category.name", "edited category - cat")
#     res = pet.edit_pet(edit_pet_url, put_pet_payload, headers)
