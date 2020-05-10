from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    DEFAULT_FLUENT_WAIT_TIME = 10

    def __init__(self, driver):
        self.driver = driver

    def send_text(self, element_locator, find_by, text):
        element = self.find_element_by(element_locator, find_by)
        element.click()
        element.clear()
        element.send_keys(text)

    def click(self, element_locator, find_by):
        element = self.find_element_by(element_locator, find_by)
        element.click()

    def find_elements_by(self, element_locator, find_by):

        try:
            self.wait_for_presence_of_element(element_locator, find_by, self.DEFAULT_FLUENT_WAIT_TIME)
            return self.driver.find_elements(find_by, element_locator)
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with locator {element_locator} was not found")

    def find_element_by(self, element_locator, find_by):

        try:
            return self.wait_for_presence_of_element(element_locator, find_by, self.DEFAULT_FLUENT_WAIT_TIME)
        except NoSuchElementException:
            raise NoSuchElementException("Element with locator" + element_locator + "was not found")

    def select_option(self, element_locator, find_by, visible_text,):
        element = Select(self.find_element_by(element_locator, find_by))
        element.select_by_visible_text(visible_text)

    def wait_for_seconds(self, seconds):
        time.sleep(seconds)

    def wait_for_presence_of_element(self, element_locator, by, seconds):
        return WebDriverWait(self.driver, seconds).until(
            EC.presence_of_element_located((by, element_locator))
        )
