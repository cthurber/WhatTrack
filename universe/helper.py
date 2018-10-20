
import time
import requests
from bs4 import BeautifulSoup as Soup

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

# TODO Add unit tests for files, and urls
# TODO Add error handling for file note found
def get_soup(path):

    if 'http' in path:
        response = requests.get(path)
        status = response.status_code

        if status == 200:
            page = response.text
            return Soup(page, "html.parser")
        else:
            # TODO Improve this error reporting
            print("Unable to capture page",path,"error:",status)
    else:
        with open(path, 'r') as f:
            page = f.read()

        soup = Soup(page, "html.parser")
        return soup
