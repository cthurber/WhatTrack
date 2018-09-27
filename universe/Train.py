from uuid import uuid4

class Train(object):

    # TODO Define each attribute in docstring
    """A New Jersey Transit train class"""

    def __init__(self, origin, destination, number, departure_time, line, stops, track):
        self.origin = origin
        self.destination = destination
        self.number = number
        self.departure_time = departure_time
        self.line = line
        self.stops = stops
        self.track = track
        self.train_id = uuid4()

    def get_last_stop(self):
        return self.stops[-1]

    # TODO Should return a departure object from the train
    def to_departure(self):
        pass
