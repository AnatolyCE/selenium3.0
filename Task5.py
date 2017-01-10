import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome("C:\Selenium\Drivers\chromedriver.exe")
    # wd = webdriver.Ie("C:\Selenium\Drivers\IEDriverServer.exe")
    # capabilities = {"unexpectedAlertBehaviour": "dismiss"}
    # capabilities = {"requireWindowFocus": True}
    # print(wd.capabilities)

    # FF geckodriver:
    # wd = webdriver.Firefox(capabilities={"marionette": True})
    # wd = webdriver.Firefox(firefox_binary="C:\Selenium\Mozilla Firefox All\Mozilla Firefox Latest/firefox.exe")

    # FF Firefox ESR:
    # wd = webdriver.Firefox(firefox_binary="C:\Selenium\Mozilla Firefox All\Mozilla Firefox ESR/firefox.exe",
    #                        capabilities={"marionette": False})

    # FF Nightly
    wd = webdriver.Firefox(firefox_binary="C:\Selenium\Mozilla Firefox All\Mozilla Firefox Nightly/firefox.exe")

    # chrome_driver = webdriver.Chrome()
    # ie_driver = webdriver.Ie()
    print(wd.capabilities)

    # request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/lifecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
