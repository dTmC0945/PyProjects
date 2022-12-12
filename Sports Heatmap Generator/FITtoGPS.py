import fitparse
import pandas as pd


def FITtoGPS(filename):
    array_lat = []
    array_long = []
    # Load the FIT file
    fitfile = fitparse.FitFile("FIT/" + filename)

    # Iterate over all messages of type "record"
    # (other types include "device_info", "file_creator", "event", etc)
    for event in fitfile.get_messages("sport"):
        print(event)

    for record in fitfile.get_messages("record"):
        # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
        for data in record:

            # Print the name and value of the data (and the units if it has any)
            if data.units:
                if data.name == "position_lat":
                    lat = array_lat.append(data.value * 180 / (2 ** 31))
                if data.name == "position_long":
                    lat = array_long.append(data.value * 180 / (2 ** 31))
                # print(" * {}: {} ({})".format(data.name, data.value, data.units))
            # print(" * {}: {}".format(data.name, data.value))

    return array_lat, array_long
