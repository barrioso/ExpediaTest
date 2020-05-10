from main.page.HomePage import HomePage
from main.page.ResultPage import ResultPage


class FlightManager:

    def __init__(self, driver):
        self.driver = driver

    def search_flight(self, flight):
        home_page = HomePage(self.driver)
        home_page.click_flight_button()
        home_page.set_from_place(flight.from_place)
        home_page.set_destination_place(flight.destination_place)
        home_page.set_departure_date(flight.departure_date)
        home_page.set_arrival_date(flight.arrival_date)
        home_page.click_search_button()

    def sort_prices(self, sort_by):
        result_page = ResultPage(self.driver)
        result_page.sort_prices(sort_by)

    def get_flight_prices(self):
        result_page = ResultPage(self.driver)

        return None
