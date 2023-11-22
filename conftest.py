
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    chromedriver_path = '/Users/Roman/PycharmProjects/pythonProject2/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    yield driver
    driver.quit()
