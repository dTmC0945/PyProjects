from sh import gunzip
import os
import folium
import gpxpy
import fitparse
import pandas as pd


def FITtoGPS(filename):
    # declare empty arrays
    array_lat, array_lon, array_id = [], [], []

    # Load the FIT file from location. All FIT files are assumed to be in FIT folder
    fitfile = fitparse.FitFile("FIT/" + filename)

    # Parses through the data inside the FIT file to find sport type
    for activity in fitfile.get_messages("sport"):
        for sport_type in activity:
            array_id.append(str(sport_type))

    # Iterate over all messages of type "record"
    # (other types include "device_info", "file_creator", "event", etc)
    for record in fitfile.get_messages("record"):
        # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
        for gps in record:

            # Print the name and value of the data (and the units if it has any)
            if gps.units:
                # Some exercises may not have GPS data (i.e., strength or indoor swim), this breaks the loop for it.
                if gps.value is None:
                    break

                # Retrieve the latitude and longitude data from the FIT file
                if gps.name == "position_lat":  # get latitude data
                    lat = array_lat.append(gps.value * 180 / (2 ** 31))
                if gps.name == "position_long":  # get longitude data
                    lat = array_lon.append(gps.value * 180 / (2 ** 31))

    # Finally record the latitude and longitude in a dataframe (from Pandas)
    df = pd.DataFrame({"Latitude": array_lat, "Longitude": array_lon})

    # Return sport type and dataframe containing GPS data.
    return array_id, df


# Declare the location for the files for FIT and GPX files
fit_location = os.listdir("FIT")
gpx_location = os.listdir("GPX")

# In those files, find the filenames that end with the .fit and .gpx ends
fit_files = [file for file in fit_location if file[-4:].lower() == '.fit']
gpx_files = [file for file in gpx_location if file[-4:].lower() == '.gpx']

# Create the map
Sport_Map = folium.Map()

for file in gpx_files:
    gpx = gpxpy.parse(open("GPX/" + file))
    track = gpx.tracks[0]
    segment = track.segments[0]
    # Load the data into a Pandas dataframe (by way of a list)
    data = []
    segment_length = segment.length_3d()
    for point_idx, point in enumerate(segment.points):
        data.append([point.latitude, point.longitude])
    columns = ["Latitude", "Longitude"]
    gpx_df = pd.DataFrame(data, columns=columns)

    if track.type == "9":
        folium.PolyLine(gpx_df.astype(float), color="red", weight=2.5, opacity=0.75).add_to(Sport_Map)
    elif track.type == "4":
        folium.PolyLine(gpx_df.astype(float), color="purple", weight=2.5, opacity=0.75).add_to(Sport_Map)

for file in fit_files:
    sport, result = FITtoGPS(file)
    if len(result) > 10:
        if bool(sport):
            if sport[0] == "name: Walk":
                folium.PolyLine(result.astype(float), color="green", weight=2.5, opacity=0.75).add_to(Sport_Map)
            elif sport[0] == "name: Bike":
                folium.PolyLine(result.astype(float), color="blue", weight=2.5, opacity=0.75).add_to(Sport_Map)
            elif sport[0] == "name: Run":
                folium.PolyLine(result.astype(float), color="red", weight=2.5, opacity=0.75).add_to(Sport_Map)
            elif sport[0] == "name: Trail Run":
                folium.PolyLine(result.astype(float), color="darkred", weight=2.5, opacity=0.75).add_to(Sport_Map)
            elif sport[0] == "name: Open Water":
                folium.PolyLine(result.astype(float), color="cadetblue", weight=2.5, opacity=0.75).add_to(Sport_Map)
            elif sport[0] == "name: Hike":
                folium.PolyLine(result.astype(float), color="purple", weight=2.5, opacity=0.75).add_to(Sport_Map)
            else:
                folium.PolyLine(result.astype(float), color="red", weight=2.5, opacity=0.75).add_to(Sport_Map)

Sport_Map.save('Act.html')
