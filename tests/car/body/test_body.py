from pytest import mark

#I expect this test to be skipped, even if I run marker smoke or regression
@mark.skip(reason = "I am the reason this test is skipped")
@mark.smoke
@mark.regression
def test_can_navigate_to_body_part(chrome_browser):
    chrome_browser.get('https://en.wikipedia.org')
    assert True

@mark.xfail(reason = "Valid reason")
def test_door():
    assert True

#I expect this test to fail, because e.g. I know there is a bug 
@mark.xfail
def test_bumper():
    assert False
