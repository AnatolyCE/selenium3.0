import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    # wd = webdriver.Edge() # works for some function
    wd = webdriver.Ie("C:\Selenium\Drivers\IEDriverServer.exe",
                      capabilities={"unexpectedAlertBehaviour": "dismiss", "requireWindowFocus": True,
                                    "ignoreZoomSetting": True,
                                    "ignoreProtectedModeSettings": True})
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/lifecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
