from pytest import mark


@mark.skip
def test_env_is_localhost(app_config):
    base_url = app_config.base_url
    assert base_url == 'https://localhost:4450'

@mark.skip
def test_env_is_vm(app_config):
    base_url = app_config.base_url
    assert base_url == 'https:/0.0.0.0:4450'