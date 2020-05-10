class Flight:

    def __init__(self, from_place=None, destination_place=None, departure_date=None, arrival_date=None):
        self._from_place = from_place
        self._destination_place = destination_place
        self._departure_date = departure_date
        self._arrival_date = arrival_date

    @property
    def from_place(self):
        return self._from_place

    @from_place.setter
    def from_place(self, from_place):
        self._from_place = from_place

    @property
    def destination_place(self):
        return self._destination_place

    @destination_place.setter
    def destination_place(self, destination_place):
        self._destination_place = destination_place

    @property
    def departure_date(self):
        return self._departure_date

    @departure_date.setter
    def departure_date(self, departure_date):
        self._departure_date = departure_date

    @property
    def arrival_date(self):
        return self._arrival_date

    @arrival_date.setter
    def arrival_date(self, arrival_date):
        self._arrival_date = arrival_date
