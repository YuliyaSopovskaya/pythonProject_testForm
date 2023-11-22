from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import TextBoxLocators
from data_generator import generate_random_string, generate_random_email

class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"
        self.full_name = TextBoxLocators.FULL_NAME
        self.email = TextBoxLocators.EMAIL
        self.current_address = TextBoxLocators.CURRENT_ADDRESS
        self.permanent_address = TextBoxLocators.PERMANENT_ADDRESS
        self.submit_button = TextBoxLocators.SUBMIT_BUTTON
        self.output_text = TextBoxLocators.OUTPUT_TEXT

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

    def fill_form(self):
        self.fill_text_box(self.full_name, generate_random_string(10))
        self.fill_text_box(self.email, generate_random_email())
        self.fill_text_box(self.current_address, generate_random_string(20))
        self.fill_text_box(self.permanent_address, generate_random_string(20))

    def get_output_text(self):
        return self.driver.find_element(*self.output_text).text

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
