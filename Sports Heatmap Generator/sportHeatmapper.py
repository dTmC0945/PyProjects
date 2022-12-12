from sh import gunzip
import os
from fit_tool.fit_file import FitFile
import pandas as pd
import folium
import gpxpy

import FITtoGPS as f2g

fit_location = os.listdir("FIT")
gpx_location = os.listdir("GPX")

fit_files = [file for file in fit_location if file[-4:].lower() == '.fit']
gpx_files = [file for file in gpx_location if file[-4:].lower() == '.gpx']

mymap = folium.Map()

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
        folium.PolyLine(gpx_df.astype(float), color="red", weight=2.5, opacity=0.75).add_to(mymap)
    elif track.type == "4":
        folium.PolyLine(gpx_df.astype(float), color="purple", weight=2.5, opacity=0.75).add_to(mymap)


for file in fit_files:
    sport, result = f2g.FITtoGPS(file)
    if len(result) > 10:
        if bool(sport):
            if sport[0] == "name: Walk":
                folium.PolyLine(result.astype(float), color='green', weight=2.5, opacity=0.75).add_to(mymap)
            elif sport[0] == "name: Bike":
                folium.PolyLine(result.astype(float), color='blue', weight=2.5, opacity=0.75).add_to(mymap)
            elif sport[0] == "name: Run":
                folium.PolyLine(result.astype(float), color='red', weight=2.5, opacity=0.75).add_to(mymap)
            elif sport[0] == "name: Trail Run":
                folium.PolyLine(result.astype(float), color='darkred', weight=2.5, opacity=0.75).add_to(mymap)
            elif sport[0] == "name: Open Water":
                folium.PolyLine(result.astype(float), color='cadetblue', weight=2.5, opacity=0.75).add_to(mymap)
            elif sport[0] == "name: Hike":
                folium.PolyLine(result.astype(float), color='purple', weight=2.5, opacity=0.75).add_to(mymap)
            else:
                folium.PolyLine(result.astype(float), color='red', weight=2.5, opacity=0.75).add_to(mymap)


# result = result.iloc[7:-14]
#
# indx = results.loc[results['Latitude'] == 0]
#
mymap.save('Act.html')
