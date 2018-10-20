import time
import requests
from universe.helper import generate_filename, generate_timestamp

""" Scripted version exclusively for gathering data for WhatTrack revival project"""

njt_url = "http://dv.njtransit.com/mobile/tid-mobile.aspx?sid=NY"

# TODO Make able to run only while trains are running
while True:
    timestamp = generate_timestamp()
    try:
        page = requests.get(njt_url)
        fname = generate_filename("NYP_Departures_", "../snag/cache")

        with open(full_path, 'w') as f:
            print(page.content, file=f)

        # Log
        print("Saved snapshot at " + str(timestamp))

        time.sleep(61)

    except:
        print("Unable to reach page... Retrying in 30 seconds")
        time.sleep(30)
