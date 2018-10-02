from uuid import uuid4

class Train(object):

    # TODO Define each attribute in docstring
    """A New Jersey Transit train class"""

    def __init__(self, train_number, line, destination):
        self.train_id = uuid4()
        self.train_number = train_number
        self.line = line
        self.destination = destination

    def get_last_stop(self):
        return self.stops[-1]

    # TODO Should return a dict as {'table' : 'table_name', 'values' : 'comma, separated, strings'}
    def to_record(self):
        pass

    # NOTE Should employ 'get_soup' helper method in the future
    # TODO Should take soup and retrieve
    def get_stops(self, stop_soup):
        pass
