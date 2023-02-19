from pytest import mark

@mark.smoke
@mark.regression
def test_can_navigate_to_engine_part(chrome_browser):
    chrome_browser.get('https://www.howacarworks.com/basics/the-engine')
    assert True
    