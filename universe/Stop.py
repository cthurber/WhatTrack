from uuid import uuid4
from helper import get_soup

class Stop(object):
    """
    TODOs: Need to figure out how to get stops page as it's generated on the fly
    """


    def get_name(self):
        pass

    def get_estimated_time(self):
        pass

    def get_status(self):
        pass

    def __init__(self, soup):
        self.cells = [str(cell.text).replace('\\r','').replace('\\n','').strip() for cell in soup.find_all("td")]
        self.stop_id = uuid4()
        self.name = name
        self.estimated_time = estimated_time
        self.status = status
        self.time_recorded = generate_timestamp()

    # TODO Should return a dict as {'table' : 'table_name', 'values' : 'comma, separated, strings'}
    def to_record(self):
        pass

    # NOTE abstract as class methods of Stop?
    # TODO Should return the link from the departue page
    @classmethod
    def get_stop_link(self, train_number):
        base_url = "http://dv.njtransit.com/mobile/train_stops.aspx?sid=NY&train=7245"
        return base_url #+ "train_stops.aspx?sid=NY&train=" + str(train_number)

    # TODO Should use return from 'get_stop_link' to get page, return soup
    @classmethod
    def get_stop_soup(self, train_number):
        stop_page = self.get_stop_link(train_number)
        return get_soup(stop_page)

    # TODO should
    @classmethod
    def get_stops(self, train_number):
        stop_soup = self.get_stop_soup(train_number)
        print(stop_soup)
