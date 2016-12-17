import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome("C:\Selenium\Drivers\chromedriver.exe")
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://www.google.com/")
    # driver.find_element_by_name("q").send_keys("web").send_keys("Return")
    # driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 10).until(EC.title_is("Selenium WebDriver"))
