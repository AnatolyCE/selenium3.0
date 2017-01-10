import pytest, time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from array import *

# @pytest.fixture
# def driver(request):
#     wd = webdriver.Chrome()
#     request.addfinalizer(wd.quit)
#     return wd
#
#
# class User(object):
#     def __init__(self, username=None, password=None, email=None):
#         self.username = username
#         self.password = password
#         self.email = email
#
#     @classmethod
#     def admin(cls):
#         return cls(username="admin", password="admin")



driver = webdriver.Chrome()
driver.get("http://localhost/lifecart/admin/")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()


def menu_links(driver):
    main_menu = driver.find_elements_by_css_selector("ul li#app- a")

    menu_index = 0

    for data in main_menu:
        menu_index += 1

        wait = WebDriverWait(driver, 5)  # seconds
        menu_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ul li#app-:nth-child({}) .name".format(menu_index))))
        menu_link.click()

        sub_menu = driver.find_elements_by_css_selector("ul.docs li")
        if sub_menu:
            sub_index = 0
            for sub_data in sub_menu:
                sub_index += 1

                wait = WebDriverWait(driver, 5)  # seconds
                sub_link = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.docs li:nth-child({}) .name".format(sub_index))))
                sub_link.click()

                header = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                print(header.text)
                #
                # menu_links = []
                # menu_links = driver.find_elements_by_css_selector("#app- a")
                # print  menu_links


                # for (int i=0;i < menu_links.size();i++)
                #     ArrayList <WebElement> input_type = (ArrayList < WebElement >)
                #     driver.find_elements_by_css_selector("#app- a")
                #
                # for (WebElement type: input_type)
                #     type.click()



                # driver.get("http://localhost/lifecart/admin/?app=appearance&doc=template")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=appearance&doc=logotype")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=catalog&doc=catalog")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=countries&doc=countries")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=currencies&doc=currencies")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=customers&doc=customers")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=geo_zones&doc=geo_zones")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=languages&doc=languages")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=modules&doc=jobs")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=orders&doc=orders")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=pages&doc=pages")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=reports&doc=monthly_sales")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=settings&doc=store_info")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=slides&doc=slides")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=tax&doc=tax_classes")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=translations&doc=search")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=users&doc=users")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                #
                # driver.get("http://localhost/lifecart/admin/?app=vqmods&doc=vqmods")
                # wait.until(
                #     EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))


def test_task7(driver):
    # login(driver, "admin", "admin")
    menu_links(driver)


test_task7(driver)
