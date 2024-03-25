from selenium import webdriver

import pytest
import chromedriver_autoinstaller

@pytest.fixture(scope="session")
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()