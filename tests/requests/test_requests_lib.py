import requests
from pytest import mark

req_url = 'https://www.postman-echo.com/get'
params  = {'key1':'value1', 'key2':'value2'}
headers  = {'Content-Type':'application/json'}

@mark.requests_lib
def test_check_status_code():
    res = requests.get(req_url)
    print(f"status code is: {res.status_code}")
    assert res.status_code == 200
    
@mark.requests_lib
def test_response_text():
    res = requests.get(req_url)
    print(f"response body is: {res.text}")
    assert isinstance(res.text, str)

@mark.requests_lib 
def test_send_params_get_url():
    res = requests.get(req_url, params = params)
    print(f"url is: {res.url}")
    assert res.url == f"{req_url}?key1=value1&key2=value2"

@mark.requests_lib
def test_check_encoding():
    res = requests.get(req_url)
    print(f"encoding is: {res.encoding}")
    assert res.encoding == 'utf-8'

@mark.requests_lib
def test_use_decoder():
    res = requests.get(req_url)
    #the type is <class 'requests.models.Response'>
    print(f"encoded: {type(res)}")
    #the type is <class 'dict'>
    print(f"decoded: {type(res.json())}")
    #the type is <class 'str'>
    print(f"decoded: {type(res.text)}")
    assert isinstance(res.json(), dict)

@mark.requests_lib   
def test_send_params_get_url():
    res = requests.get(req_url, headers = headers)
    print(f"headers are: {res.headers}")
    assert res.headers['content-type'] == 'application/json; charset=utf-8'
    #the same can be done using res.headers.get('content-type')
