import pytest
import urllib3

urllib3.disable_warnings()

@pytest.fixture
def base_url():
    return "https://dummyjson.com"
