import fitparse
import pandas as pd


def FITtoGPS(filename):
    array_lat = []
    array_lon = []
    array_id = []
    # Load the FIT file
    fitfile = fitparse.FitFile("FIT/" + filename)

    for activity in fitfile.get_messages("sport"):
        for data in activity:

            array_id.append(str(data))
    # Iterate over all messages of type "record"
    # (other types include "device_info", "file_creator", "event", etc)
    for record in fitfile.get_messages("record"):
        # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
        for data in record:

            # Print the name and value of the data (and the units if it has any)
            if data.units:
                if data.value is None:
                    break
                if data.name == "position_lat":
                    lat = array_lat.append(data.value * 180 / (2 ** 31))
                if data.name == "position_long":
                    lat = array_lon.append(data.value * 180 / (2 ** 31))
                # print(" * {}: {} ({})".format(data.name, data.value, data.units))
            # print(" * {}: {}".format(data.name, data.value))

    df = pd.DataFrame({"Latitude": array_lat, "Longitude": array_lon})

    return array_id, df
