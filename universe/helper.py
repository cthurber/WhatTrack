
import time

# TODO Define each function in docstring
"""
A series of helper functions
"""

# TODO Generate current timestamp as 'YYYY-MM-DD HH:MM'
def generate_timestamp():
    return time.strftime("%Y-%m-%d_%H:%M")

# Generates a file at 'path' with a timestamp as unique identifier and a prefix to delineate the contents
def generate_filename(prefix, path='./', extension='.html'):
    fname = prefix + str(generate_timestamp()) + extension
    return path + fname
