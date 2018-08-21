import pytest
from ..utils import helper

@pytest.fixture()
def start(request):
    helper.Appium.driver()

    def teardown():
        util._kill_appium_by_port()

    request.addfinalizer(teardown)