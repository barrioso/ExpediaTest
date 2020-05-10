import unittest
import logging
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("Setting up driver")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.expedia.com/")

    def tearDown(self):
        logging.info("Closing driver")
        self.driver.quit()
