from pytest import fixture
from selenium import webdriver
from config import Config
import json


####HOW TO SET UP AN ENVIRONMENT FOR RUNNING TESTS
#how we use Python Argparse is PyTest, creates a custom command --evn that can be sued in cmd
def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action = "store",
        help = "Environment to run tests against"
    )

#gets the env option and returns it as a value for fixture env
@fixture(scope = 'session')
def env(request):
    return request.config.getoption("--env")

#passing the fixture env here as arg
#so we are basically building a Config class object
#using the env value, which is our current environment
@fixture(scope = 'session')
def app_config(env):
    cfg = Config(env)
    return cfg




####HOW TO GET A CHROME BROWSER WITH A SEPARATE FIXTURE
@fixture(scope = 'function')
def chrome_browser():
    browser = webdriver.Chrome()
    return browser



 
####HOW TO ADD A FIXTURE TO RUN CROSS-BROWSER TESTS
#any test that uses this fixture is going to run that test one time for every param in here
# @fixture(params = [webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
# def browser(request):
#     driver = request.param
#     d = driver()
#     yield d
#     d.quit()





####USING DATA RETRIEVED FROM JSON FILE
data_path = 'test_data.json'

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params = load_test_data(data_path))
def test_data(request):
    data = request.param
    return data
