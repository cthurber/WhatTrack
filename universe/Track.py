from helper import generate_timestamp

class Track(object):

    # TODO Define each attribute in docstring
    """Defines a departure track for a Train."""

    def __init__(self, number, is_confirmed=False):
        self.number = number
        self.time_recorded = generate_timestamp()
        self.is_confirmed = is_confirmed
