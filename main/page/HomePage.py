from main.page.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    _flight_button = ("tab-flight-tab-hp", By.ID)
    _from_place = ("flight-origin-hp-flight", By.ID)
    _destination_place = ("flight-destination-hp-flight", By.ID)
    _departure_date = ("flight-departing-hp-flight", By.ID)
    _arrival_date = ("flight-returning-hp-flight", By.ID)
    _search_button = ("div", By.TAG_NAME)

    def __init__(self, driver):
        super().__init__(driver)

    def click_flight_button(self):
        self.click(*self._flight_button)

    def set_from_place(self, from_place_text):
        self.send_text(*self._from_place, from_place_text)

    def set_destination_place(self, destination_place_text):
        self.send_text(*self._destination_place, destination_place_text)

    def set_departure_date(self, departure_date_text):
        self.send_text(*self._departure_date, departure_date_text)

    def set_arrival_date(self, arrival_date_text):
        self.send_text(*self._arrival_date, arrival_date_text)

    def click_search_button(self):
        self.click(*self._search_button)
