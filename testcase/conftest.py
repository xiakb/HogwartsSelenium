import pytest
from selenium import webdriver


@pytest.fixture(autouse="true", scope="module")
def my_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


