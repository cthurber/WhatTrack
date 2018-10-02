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
        contents = self.soup.find("table", {"id" : "GridView1"})
        self.contents = contents
        return contents

    def __init__(self, from_file):
        self.from_file = from_file
        self.soup = self.get_soup(from_file)
        self.table = self.get_table()
        self.listings = self.get_listings()
        self.departures = []

    def get_listings(self):

        listings = self.contents.find_all("tr")[1:]

        for listing in listings:
            # NOTE Silly fix... abstract this elsewhere; Move this to helper?
            if len(Soup(str(listing)).find_all("td")) == 6:
                departure = Departure(Soup(str(listing)))
                self.departures.append(departure)
        print(self.departures)

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
    board.scrape()


if __name__ == "__main__":
    main()
