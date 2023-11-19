from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import pytest


# driver = webdriver.Chrome(executable_path='прямой путь к дровам')
# driver.get('https://demoqa.com/text-box')
# driver.maximize_window()
#
# userName = driver.find_element(by.CSS_SELECTOR, "#userName")
# userEmail = driver.find_element(by.CSS_SELECTOR, "#userEmail")
# currentAddress = driver.find_element(by.CSS_SELECTOR, "#currentAddress")
# permanentAddress = driver.find_element(by.CSS_SELECTOR, "#permanentAddress")
#
# random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
# userName.send_keys(random_string)
#
# email = f"{random_string(6)}@example.com"
# userEmail.send_keys(email)
# currentAddress.send_keys(random_string)
# permanentAddress.send_keys(random_string)
#
# button_submit = driver.find_element(By.XPATH, "//input[@id='submit']")
# button_submit.click()


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"
        self.full_name = (By.ID, "userName")
        self.email = (By.ID, "userEmail")
        self.current_address = (By.ID, "currentAddress")
        self.permanent_address = (By.ID, "permanentAddress")
        self.submit_button = (By.ID, "submit")
        self.output_text = (By.ID, "output")

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_submit(self):
        submit_button = self.wait_for_element(self.submit_button)
        submit_button.click()

    def open_page(self):
        self.driver.get(self.url)

    def fill_text_box(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def generate_random_string(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    
    def fill_form(self):
        self.fill_text_box(self.full_name, self.generate_random_string(10))
        self.fill_text_box(self.email, self.generate_random_string(8) + "@example.com")
        self.fill_text_box(self.current_address, self.generate_random_string(20))
        self.fill_text_box(self.permanent_address, self.generate_random_string(20))


    def get_output_text(self):
        return self.driver.find_element(*self.output_text).text


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_text_box_form(driver):
    textbox_page = TextBoxPage(driver)
    textbox_page.open_page()
    textbox_page.fill_form()
    textbox_page.click_submit()

    submitted_text = textbox_page.get_output_text()

    assert "Name" in submitted_text, "Name is not displayed in the output text"
    assert "Email" in submitted_text, "Email is not displayed in the output text"
    assert "Current Address" in submitted_text, "Current Address is not displayed in the output text"
    assert "Permanent Address" in submitted_text, "Permanent Address is not displayed in the output text"

    print(submitted_text)
