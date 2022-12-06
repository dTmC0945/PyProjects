import gpxpy
import pandas as pd
import folium
from xml.dom import minidom
import os
from pathlib import Path
import plotly.express as px

gpx_files = os.listdir("activities")

gpx_files.remove(".DS_Store")

coords_df = {}
for i in range(len(gpx_files)):
    gpx = gpxpy.parse(open("activities/" + gpx_files[i]))
    track_coords = [[point.latitude, point.longitude, point.elevation]
                    for track in gpx.tracks
                    for segment in track.segments
                    for point in segment.points]
    coords_df[i] = pd.DataFrame(track_coords)

heatcoords_df = pd.concat(coords_df, ignore_index=True)
heatcoords_df.columns = ['Latitude', 'Longitude', 'Altitude']

runningheatmap = heatcoords_df.drop('Altitude', axis=1)

mymap = folium.Map(location=[heatcoords_df.Latitude.mean(), heatcoords_df.Longitude.mean()], zoom_start=6, tiles=None)
folium.PolyLine(runningheatmap, color='red', weight=2.5, opacity=.5).add_to(mymap)
folium.TileLayer("openstreetmap", name="OpenStreet Map").add_to(mymap)


mymap.save('Activities.html')

# gpx_df, points, type = process_gpx_to_df("2169765006.gpx")
# print(type)
# print(process_gpx_to_df("2169765006.gpx"))

# folium.TileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}", attr="Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC”, name=’Nat Geo Map").add_to(mymap)
# folium.TileLayer("http://tile.stamen.com/terrain/{z}/{x}/{y}.jpg", attr="terrain-bcg", name="Terrain Map").add_to(mymap)
