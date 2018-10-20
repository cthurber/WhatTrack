from uuid import uuid4

class Stop(object):
    """A class for a Stop on a New Jersey Transit train line"""

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
