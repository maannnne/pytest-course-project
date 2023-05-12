import logging as logger
import pytest
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

# test data
pet_id = 0
pet_name = "Lucy"
edited_pet_name = "Max"
category_name = "cat"
edited_category_name = "dog"
tag_name = "black"
edited_tag_name = "white"
pet_status = "available"
edited_pet_status = "unavailable"
deleted_pet_error_message = "Pet not found"


@mark.petstore
@mark.dependency()
def test_env_is_petstore(app_config):
    """
    Check that the test environment is correctly set to "petstore"
    """
    logger.info("EXECUTING: environment - check the env is correctly set")
    base_url = app_config.base_url
    expected_url = "https://petstore.swagger.io/v2"
    assert base_url == expected_url, \
    f"Expected ~~{expected_url}~~ but got ~~{base_url}~~"


@mark.petstore
@mark.dependency(depends = ["test_env_is_petstore"])
def test_post_add_pet(app_config):
    """
    Add a pet, check that the pet was created with the specified data
    """
    logger.info("EXECUTING: test_add_pet - add the pet and make response assertions")
    
    logger.info("TEST STEP: Preparing payload")
    base.edit_request_key_value(new_pet_payload, "name", pet_name)
    base.edit_request_key_value(new_pet_payload, "category.name", category_name)
    base.edit_request_key_value(new_pet_payload, "tags[0].name", tag_name)
    base.edit_request_key_value(new_pet_payload, "status", pet_status)
    
    logger.info("TEST STEP: Creating a pet - POST /pet")
    add_pet_url = app_config.base_url + post_pet_endpoint
    res = pet.add_pet(add_pet_url, new_pet_payload, headers)
    
    logger.info("TEST STEP: Getting values from POST /pet response")
    global pet_id
    pet_id = base.get_response_key_value(res, "id")
    logger.debug(f"THE PET ID: {pet_id}")
    res_pet_name = base.get_response_key_value(res, "name")
    res_category_name = base.get_response_key_value(res, "category.name")
    res_tag_name = base.get_response_key_value(res, "tags[0].name")
    res_pet_status = base.get_response_key_value(res, "status")

    logger.info("TEST STEP: Asserting the POST /pet response")
    assert res_pet_name == pet_name, \
    f"Expected ~~{pet_name}~~ but got ~~{res_pet_name}~~"
    assert res_category_name == category_name, \
    f"Expected ~~{category_name}~~ but got ~~{res_category_name}~~"
    assert res_tag_name == tag_name, \
    f"Expected ~~{tag_name}~~ but got ~~{res_tag_name}~~"
    assert res_pet_status == pet_status, \
    f"Expected ~~{pet_status}~~ but got ~~{res_pet_status}~~"
   
   
@mark.petstore
@mark.dependency(depends = ["test_env_is_petstore", "test_post_add_pet"])
def test_get_pet_after_creation(app_config):
    logger.info("EXECUTING: test_get_pet_after_creation - get the pet and make response assertions")
    
    logger.info("TEST STEP: Getting the pet - GET /pet/id")
    get_pet_url = f"{app_config.base_url}{get_pet_endpoint}"
    res = pet.get_pet_by_id(get_pet_url, pet_id)
    
    logger.info("TEST STEP: Getting values from GET /pet/id response")
    res_pet_id  = base.get_response_key_value(res, "id")
    res_pet_name = base.get_response_key_value(res, "name")
    res_category_name = base.get_response_key_value(res, "category.name")
    res_tag_name = base.get_response_key_value(res, "tags[0].name")
    res_pet_status = base.get_response_key_value(res, "status")
    
    logger.info("TEST STEP: Asserting the GET /pet response")
    assert res_pet_name == pet_name, \
    f"Expected ~~{pet_name}~~ but got ~~{res_pet_name}~~"
    assert res_category_name == category_name, \
    f"Expected ~~{category_name}~~ but got ~~{res_category_name}~~"
    assert res_tag_name == tag_name, \
    f"Expected ~~{tag_name}~~ but got ~~{res_tag_name}~~"
    assert res_pet_status == pet_status, \
    f"Expected ~~{pet_status}~~ but got ~~{res_pet_status}~~"


@mark.petstore
@mark.dependency(depends = ["test_env_is_petstore", "test_post_add_pet"])
def test_put_edit_pet(app_config):
    logger.info("EXECUTING: test_edit_pet - edit the pet and make response assertions")
    
    logger.info("TEST STEP: Preparing payload")
    logger.debug(f"THE PET ID: {pet_id}")
    base.edit_request_key_value(put_pet_payload, "id", pet_id)
    base.edit_request_key_value(put_pet_payload, "name", edited_pet_name)
    base.edit_request_key_value(put_pet_payload, "category.name", edited_category_name)
    base.edit_request_key_value(put_pet_payload, "tags[0].name", edited_tag_name)
    base.edit_request_key_value(put_pet_payload, "status", edited_pet_status)
    
    logger.info("TEST STEP: Editing a pet - PUT /pet")
    edit_pet_url = app_config.base_url + put_pet_endpoint
    res = pet.edit_pet(edit_pet_url, put_pet_payload, headers)
    
    logger.info("TEST STEP: Getting values from PUT /pet response")
    res_pet_id = base.get_response_key_value(res, "id")
    res_pet_name = base.get_response_key_value(res, "name")
    res_category_name = base.get_response_key_value(res, "category.name")
    res_tag_name = base.get_response_key_value(res, "tags[0].name")
    res_pet_status = base.get_response_key_value(res, "status")
    
    logger.info("TEST STEP: Asserting PUT /pet response")
    assert res_pet_id == pet_id, \
        f"Expected ~~{pet_id}~~ but got ~~{res_pet_id}~~"
    assert res_pet_name == edited_pet_name, \
        f"Expected ~~{edited_pet_name}~~ but got ~~{res_pet_name}~~"
    assert res_category_name == edited_category_name, \
        f"Expected ~~{edited_category_name}~~ but got ~~{res_category_name}~~"
    assert res_tag_name == edited_tag_name, \
        f"Expected ~~{edited_tag_name}~~ but got ~~{res_tag_name}~~"
    assert res_pet_status == edited_pet_status, \
        f"Expected ~~{edited_pet_status}~~ but got ~~{res_pet_status}~~"


@mark.petstore
@mark.dependency(depends = ["test_env_is_petstore", "test_post_add_pet", "test_put_edit_pet"])
def test_get_pet_after_editing(app_config):
    logger.info("EXECUTING: test_get_pet_after_editing - get the pet and make response assertions")
    
    logger.info("TEST STEP: Getting the pet - GET /pet/id")
    get_pet_url = app_config.base_url + get_pet_endpoint
    res = pet.get_pet_by_id(get_pet_url, pet_id)
    
    logger.info("TEST STEP: Getting values from GET /pet/id response")
    res_pet_id  = base.get_response_key_value(res, "id")
    res_pet_name = base.get_response_key_value(res, "name")
    res_category_name = base.get_response_key_value(res, "category.name")
    res_tag_name = base.get_response_key_value(res, "tags[0].name")
    res_pet_status = base.get_response_key_value(res, "status")
    
    logger.info("TEST STEP: Asserting the GET /pet response")
    assert res_pet_id == pet_id, \
        f"Expected ~~{pet_id}~~ but got ~~{res_pet_id}~~"
    assert res_pet_name == edited_pet_name, \
        f"Expected ~~{edited_pet_name}~~ but got ~~{res_pet_name}~~"
    assert res_category_name == edited_category_name, \
        f"Expected ~~{edited_category_name}~~ but got ~~{res_category_name}~~"
    assert res_tag_name == edited_tag_name, \
        f"Expected ~~{edited_tag_name}~~ but got ~~{res_tag_name}~~"
    assert res_pet_status == edited_pet_status, \
        f"Expected ~~{edited_pet_status}~~ but got ~~{res_pet_status}~~"
        

@mark.petstore
@mark.dependency(depends = ["test_env_is_petstore", "test_post_add_pet"])
def test_delete_pet(app_config):
    logger.info("EXECUTING: test_delete_pet - delete the pet")
    
    logger.info("TEST STEP: Deleting the pet - DELETE /pet/id")
    delete_pet_url = app_config.base_url + delete_pet_endpoint
    
    logger.info("TEST STEP: Asserting deleted pet response - DELETE /pet/id")
    res = pet.delete_pet(delete_pet_url, pet_id)
    res_pet_id = int(pet.get_response_key_value(res, "message"))
    assert res_pet_id == pet_id, \
        f"Expected ~~{pet_id}~~ but got ~~{res_pet_id}~~"
    
    logger.info("TEST STEP: Getting deleted pet - GET /pet/id")
    get_pet_url = app_config.base_url + get_pet_endpoint
    deleted_pet_info = pet.get_deleted_pet(get_pet_url, pet_id)    
    
    logger.info("TEST STEP: Asserting error message for deleted pet - GET /pet/id")
    res_message = pet.get_response_key_value(deleted_pet_info, "message")
    assert res_message == deleted_pet_error_message, \
        f"Expected ~~{deleted_pet_error_message}~~ but got ~~{res_message}~~"
    