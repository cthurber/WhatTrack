import requests
from bs4 import BeautifulSoup as Soup
from Departure import Departure

class Board(object):
    # TODO Define each attribute in docstring
    """
    Definition of a departure board

    The Board should be "stored" in the database with methods called on each object to convert it to it's record
    """

    # TODO Add error handling for file note found
    def get_soup(self, file):

        with open(file, 'r') as f:
            page = f.read()

        soup = Soup(page, "html.parser")
        return soup

    # TODO Add explanatory exceptions for parameters
    def get_table(self):
        return self.soup.find("table", {"id" : "GridView1"})

    def __init__(self, from_file):
        self.from_file = from_file              # HTML source file from which we'll be scraping our
        self.soup = self.get_soup(from_file)    # Get entire page source as BeautifulSoup object
        self.table = self.get_table()           # NOTE (Necessary?) Contains the source of the departure table on-page
        self.departures = self.get_listings()   # Contains departure objects derived from 'listings'

    def get_listings(self):

        listings = self.table.find_all("tr")[1:]
        departures = []

        for listing in listings:
            # NOTE Silly fix... abstract this elsewhere; Move this to helper?
            if len(Soup(str(listing)).find_all("td")) == 6:
                departure = Departure(Soup(str(listing)))
                departures.append(departure)

        return departures

    def sweep():
        # TODO This function should run...
        #  - Add new departures to the Board
        #  - Compare with last run:
        #   - Has status changed
        #   - Has track changed
        #   - Has departure been removed
        pass

    # TODO Should return a dict as {'table' : 'table_name', 'values' : 'comma, separated, strings'}
    def to_record(self):
        pass

    # TODO Store the completed board in the database by calling to_record methods for each of the departures, etc.
    def save(self):
        pass

    # TODO Get each listing from the board and turn it into a departure
    def scrape(self):
        pass

    # TODO Board should be able to convert to JSON for API access
    def to_json(self):
        pass

    # TODO Board should be able to tell when listings have changed
    def listings_changed(self):
        pass

def main():
    fname = "../snag/cache/NYP_Departures_2018-09-25_22:18.html"
    board = Board(fname)

    # for departure in board.departures:
    #     print(departure.train)

if __name__ == "__main__":
    main()
