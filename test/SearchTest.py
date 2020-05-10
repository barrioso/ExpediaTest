import logging
from .BaseTest import BaseTest
from main.service.FlightManager import FlightManager
from main.entity.Flight import Flight


class SearchTest(BaseTest):

    def test_sort(self):
        flight = self.build_flight()
        flight_manager = FlightManager(self.driver)

        logging.info("Searching for flight")
        flight_manager.search_flight(flight)

        logging.info("Sorting prices")
        flight_manager.sort_prices("Price (Highest)")

        logging.info("Getting prices")
        prices = flight_manager.get_flight_prices()

    def are_prices_sorted(self, prices):
        return prices == sorted(prices, reverse=True)

    def build_flight(self):
        flight = Flight()
        flight.from_place = "Mexico City, Distrito Federal, Mexico (MEX-Mexico City Intl.)"
        flight.destination_place = "Las Vegas, NV (LAS-All Airports)"
        flight.departure_date = "07/26/2020"
        flight.arrival_date = "07/28/2020"
        return flight
