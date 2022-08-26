import pytest
import time
from selenium.webdriver.common.by import By



class TestLangInterfaces():

    def test_interface_language(self, browser, language):
        browser.get(f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/')
        browser.implicitly_wait(20)

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')

        assert button, "Can't find element with this selector"
        time.sleep(30)