from uuid import uuid4
from Stop import Stop

class Train(object):

    # TODO Define each attribute in docstring
    """A New Jersey Transit train class"""

    def __init__(self, train_number, line, destination, soup):
        self.soup = soup
        self.train_id = uuid4()
        self.train_number = train_number
        self.line = line
        self.destination = destination
        # TODO Temporarily removing stops functionality
        # self.stops = Stop.get_stops(self.train_number)

    def __str__(self):
        train = str(self.train_number) + " to " + str(self.destination)
        return train

    def get_last_stop(self):
        return self.stops[-1]

    # TODO Should return a dict as {'table' : 'table_name', 'values' : 'comma, separated, strings'}
    def to_record(self):
        pass
