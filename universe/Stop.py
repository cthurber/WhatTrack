from uuid import uuid4

class Stop(object):
    """A class for a Stop on a New Jersey Transit train line"""
    def __init__(self, name, estimated_time, status):
        self.stop_id = uuid4()
        self.name = name
        self.estimated_time = estimated_time
        self.status = status
        self.time_recorded = generate_timestamp()

    # TODO Should return a dict as {'table' : 'table_name', 'values' : 'comma, separated, strings'}
    def to_record(self):
        pass
