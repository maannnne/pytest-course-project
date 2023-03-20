from pytest import mark
from base.Base import *
from endpoints.Petstore_Pet import Petstore_Pet
import os
import jsonpath as jsn
import requests
import json
from jsonpath_ng import jsonpath, parse

post_pet_endpoint = '/pet'
json_file_path = 'jsons\\new_pet.json'
# payload = {
#     "id": 9223372036854284571,
#     "category": {
#         "id": 0,
#         "name": "cat"
#     },
#     "name": "Lucy",
#     "photoUrls": [
#         "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Blackcat-Lilith.jpg/220px-Blackcat-Lilith.jpg"
#     ],
#     "tags": [
#         {
#             "id": 0,
#             "name": "black"
#         }
#     ],
#     "status": "available"
# }



@mark.petstore
def test_add_pet(app_config):
    petstore_pet = Petstore_Pet()
    add_pet_url = app_config.base_url + post_pet_endpoint
    res = petstore_pet.add_pet(add_pet_url, json_file_path)
    print(f'The id of the newly added pet: #{res}')




    # add_pet_url = app_config.base_url + post_pet_endpoint
    # res = requests.post(add_pet_url, json = payload)
    # response_json = res.json()
    # print(f'The url we called to: #{response_json["category.id"]}')
