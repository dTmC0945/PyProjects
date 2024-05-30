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
                    array_lat.append(gps.value * 180 / (2 ** 31))
                if gps.name == "position_long":  # get longitude data
                    array_lon.append(gps.value * 180 / (2 ** 31))

    # Finally record the latitude and longitude in a dataframe (from Pandas)
    df = pd.DataFrame({"Latitude": array_lat, "Longitude": array_lon})

    # Return sport type and dataframe containing GPS data.
    return array_id, df


# Declare the location for the files for FIT and GPX files
fit_location, gpx_location = os.listdir("FIT"), os.listdir("GPX")

# In those files, find the filenames that end with the .fit and .gpx ends
fit_files = [file for file in fit_location if file[-4:].lower() == '.fit']
gpx_files = [file for file in gpx_location if file[-4:].lower() == '.gpx']

# Create the map
Sport_Map = folium.Map(location=[53.48, -3], zoom_start=7)

# Create the groups
running_group = folium.FeatureGroup(name="Running").add_to(Sport_Map)
hiking_group = folium.FeatureGroup(name="Hiking").add_to(Sport_Map)
cycling_group = folium.FeatureGroup(name="Cycling").add_to(Sport_Map)
swim_group = folium.FeatureGroup(name="Swimming").add_to(Sport_Map)
walking_group = folium.FeatureGroup(name="Walking").add_to(Sport_Map)
trail_r_group = folium.FeatureGroup(name="Trail Running").add_to(Sport_Map)

# Parses through the gpx files
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

    # GPX reserves number 9 for running activities
    if track.type == "9":
        # add values to running group
        running_group.add_child(folium.PolyLine(gpx_df.astype(float), color="red", weight=3, opacity=0.75))

    # GPX reserves number 4 for hiking activities
    elif track.type == "4":
        # add values to hiking group
        hiking_group.add_child(folium.PolyLine(gpx_df.astype(float), color="purple", weight=3, opacity=0.75))

for file in fit_files:
    sport, result = FITtoGPS(file)
    if len(result) > 10:
        if bool(sport):
            if sport[0] == "name: Walk":
                walking_group.add_child(folium.PolyLine(result.astype(float), color="green", weight=3, opacity=0.75))
            elif sport[0] == "name: Bike":
                cycling_group.add_child(folium.PolyLine(result.astype(float), color="blue", weight=3, opacity=0.75))
            elif sport[0] == "name: Run":
                running_group.add_child(folium.PolyLine(result.astype(float), color="red", weight=3, opacity=0.75))
            elif sport[0] == "name: Trail Run":
                trail_r_group.add_child(folium.PolyLine(result.astype(float), color="darkred", weight=3, opacity=0.75))
            elif sport[0] == "name: Open Water":
                swim_group.add_child(folium.PolyLine(result.astype(float), color="cadetblue", weight=3, opacity=0.75))
            elif sport[0] == "name: Hike":
                hiking_group.add_child(folium.PolyLine(result.astype(float), color="purple", weight=3, opacity=0.75))
            else:
                hiking_group.add_child(folium.PolyLine(result.astype(float), color="purple", weight=3, opacity=0.75))

# Finally add the layer controller for the map
folium.LayerControl().add_to(Sport_Map)

# Save the map information as Activities.html
Sport_Map.save('Activities.html')

# End of code
