from .BasePage import BasePage
from selenium.webdriver.common.by import By


class ResultPage(BasePage):

    _prices = ("div", By.TAG_NAME)
    _sort_prices_select = ("sortDropdown", By.ID)

    def sort_prices(self, sort_by):
        self.select_option(*self._sort_prices_select, sort_by)
        self.wait_for_seconds(5)

    def get_prices(self):
        return self.find_elements_by(*self._prices)
