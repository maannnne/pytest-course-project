from pytest import fixture
from selenium import webdriver
from config import Config

def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action = "store",
        help = "Environment to run tests against"
    )

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    return browser

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

#passing the fixture env here to this app_config fixture
#so we are basically building a Config class object using the env
@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg
