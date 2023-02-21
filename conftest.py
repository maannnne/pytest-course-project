from pytest import fixture
from selenium import webdriver
from config import Config

#how we use Python Argparse is PyTest
#creates a custom command --evn that can be sued in cmd
def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action = "store",
        help = "Environment to run tests against"
    )

#gets the env option and returns it as a value for fixture env
@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

#passing the fixture env here as arg
#so we are basically building a Config class object
#using the env value, which is our current environment
@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    return browser
