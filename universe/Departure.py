from uuid import uuid4
from bs4 import BeautifulSoup as Soup

class Departure(object):
    # TODO Define each attribute in docstring
    """
        Definition of a departure listing on the departure board
        All getter methods require a Soup object to operate

        Here, we'll scrape the information from the soup, create a Departure object, and initialize the Train object as part of the record
    """

    def get_departure_time(self):
        return self.cells[0]

    def get_destination(self):
        return self.cells[1]

    def get_track(self):
        return self.cells[2]

    def get_line(self):
        return self.cells[3]

    def get_train_number(self):
        return self.cells[4]

    def get_status(self):
        return self.cells[5]

    # TODO Should return a dict as {'table' : 'table_name', 'values' : 'comma, separated, strings'}
    def to_record(self):
        pass

    def __str__(self):
        departure = str(self.departure_time)  + ', ' + str(self.destination)  + ', ' + str(self.track)  + ', ' + str(self.line)  + ', ' + str(self.train_number)  + ', ' + str(self.status)
        return departure

    def __init__(self, soup):
        self.cells = [str(cell.text).replace('\\r','').replace('\\n','').strip() for cell in soup.find_all("td")]
        self.departure_id = uuid4()
        self.departure_time = self.get_departure_time()
        self.track = self.get_track()
        self.status = self.get_status()
        self.train = Train(self.get_train_number(), self.get_line(), self.get_destination())
