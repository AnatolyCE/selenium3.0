import pytest, time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


class User(object):
    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def admin(cls):
        return cls(username="admin", password="admin")


def login(driver, username, password):
    driver.get("http://localhost/lifecart/admin/")
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()


def menu_links(driver):
    main_menu = driver.find_elements_by_css_selector("ul li#app- a")

    menu_index = 0

    for data in main_menu:
        menu_index += 1

        wait = WebDriverWait(driver, 5)
        menu_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ul li#app-:nth-child({}) .name".format(menu_index))))
        menu_link.click()

        sub_menu = driver.find_elements_by_css_selector("ul.docs li")
        if sub_menu:
            sub_index = 0
            for sub_data in sub_menu:
                sub_index += 1

                wait = WebDriverWait(driver, 5)
                sub_link = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.docs li:nth-child({}) .name".format(sub_index))))
                sub_link.click()
                h1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))


def test_task7(driver):
    login(driver, "admin", "admin")
    menu_links(driver)


test_task7
