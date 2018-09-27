
class Departure(object):
    # TODO Define each attribute in docstring
    """Definition of a departure listing on the departure board"""
    def __init__(self, departure_time, destination, track, line, train, status):
        self.departure_time = departure_time
        self.destination = destination
        self.track = track
        self.line = line
        self.train = train
        self.status = status
