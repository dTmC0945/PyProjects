import gpxpy
import pandas as pd
import folium
from xml.dom import minidom


def process_gpx_to_df(file_name):
    gpx = gpxpy.parse(open(file_name))
    file = minidom.parse(file_name)

    # (1)make DataFrame
    track = gpx.tracks[0]
    segment = track.segments[0]
    type = file.getElementsByTagName('item')
    # Load the data into a Pandas dataframe (by way of a list)
    data = []
    segment_length = segment.length_3d()
    for point_idx, point in enumerate(segment.points):
        data.append([point.longitude, point.latitude, point.elevation,
                     point.time, segment.get_speed(point_idx)])
    columns = ["Longitude", "Latitude", "Altitude", "Time", "Speed"]
    gpx_df = pd.DataFrame(data, columns=columns)

    # 2(make points tuple for line)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))


    return gpx_df, points, type



gpx_df, points, type = process_gpx_to_df("2169765006.gpx")
print(type)
print(process_gpx_to_df("2169765006.gpx"))
mymap = folium.Map( location=[ gpx_df.Latitude.mean(), gpx_df.Longitude.mean() ], zoom_start=6, tiles=None)
folium.PolyLine(points, color='red', weight=4.5, opacity=.5).add_to(mymap)
folium.TileLayer("openstreetmap", name="OpenStreet Map").add_to(mymap)
#folium.TileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}", attr="Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC”, name=’Nat Geo Map").add_to(mymap)
#folium.TileLayer("http://tile.stamen.com/terrain/{z}/{x}/{y}.jpg", attr="terrain-bcg", name="Terrain Map").add_to(mymap)

mymap.save('aee.html')
