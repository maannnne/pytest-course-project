import requests
from pytest import mark

#POST request examples

req_url = 'https://httpbin.org/post'
json_payload = {'key1':'value1', 'key2':'value2'}
data_payload = {'key3':'value3'}

@mark.requests_lib_post
def test_post_request_w_json():
    r = requests.post(req_url, json = json_payload).json()
    form_val = r["json"]
    print(f'this is the data from response: {form_val}')
    assert 'key2' in form_val and 'key1' in form_val

@mark.requests_lib_post
def test_post_request_w_data():
    r = requests.post(req_url, data = data_payload).json()
    form_val = r["form"]
    print(f'this is the form from response: {form_val["key3"]}')
    assert form_val['key3']
