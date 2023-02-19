from pytest import mark

@mark.smoke
@mark.regression
def test_can_navigate_to_body_part(chrome_browser):
    chrome_browser.get('https://en.wikipedia.org')
    assert True

@mark.body
def test_door():
    assert True

@mark.body
def test_bumper():
    assert False
