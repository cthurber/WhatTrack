from uuid import uuid4

class Train(object):

    # TODO Define each attribute in docstring
    """A New Jersey Transit train class"""

    def __init__(self, train_number, line, destination, soup):
        self.soup = soup
        self.train_id = uuid4()
        self.train_number = train_number
        self.line = line
        self.destination = destination
        self.stops = self.get_stops()

    def __str__(self):
        train = str(self.train_number) + " to " + str(self.destination)
        return train

    def get_last_stop(self):
        return self.stops[-1]

    # TODO Should return a dict as {'table' : 'table_name', 'values' : 'comma, separated, strings'}
    def to_record(self):
        pass

    # NOTE abstract as class methods of Stop?
    # TODO Should return the link from the departue page
    def get_stop_link(self):
        print(self.soup)

    # TODO Should use return from 'get_stop_link' to get page, return soup
    def get_stop_soup(self):
        stop_page = self.get_stop_link()

    # TODO should
    def get_stops(self):
        stop_soup = self.get_stop_soup()
