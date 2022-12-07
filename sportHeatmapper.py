import gpxpy
import pandas as pd
import folium
import os
import gzip
from sh import gunzip
import fitdecode
from datetime import datetime, timedelta
from typing import Dict, Union, Optional,Tuple

#gunzip('FIT files/3694695330.fit.gz')

# The names of the columns we will use in our points DataFrame. For the data we will be getting
# from the FIT data, we use the same name as the field names to make it easier to parse the data.
POINTS_COLUMN_NAMES = ['latitude', 'longitude', 'lap', 'altitude', 'timestamp', 'heart_rate', 'cadence', 'speed']

# The names of the columns we will use in our laps DataFrame.
LAPS_COLUMN_NAMES = ['number', 'start_time', 'total_distance', 'total_elapsed_time',
                     'max_speed', 'max_heart_rate', 'avg_heart_rate']


def get_fit_lap_data(frame: fitdecode.records.FitDataMessage) -> Dict[str, Union[float, datetime, timedelta, int]]:
    """Extract some data from a FIT frame representing a lap and return
    it as a dict.
    """

    data: Dict[str, Union[float, datetime, timedelta, int]] = {}

    for field in LAPS_COLUMN_NAMES[1:]:  # Exclude 'number' (lap number) because we don't get that
        # from the data but rather count it ourselves
        if frame.has_field(field):
            data[field] = frame.get_value(field)

    return data


def get_fit_point_data(frame: fitdecode.records.FitDataMessage) -> Optional[
    Dict[str, Union[float, int, str, datetime]]]:
    """Extract some data from an FIT frame representing a track point
    and return it as a dict.
    """

    data: Dict[str, Union[float, int, str, datetime]] = {}

    if not (frame.has_field('position_lat') and frame.has_field('position_long')):
        # Frame does not have any latitude or longitude data. We will ignore these frames in order to keep things
        # simple, as we did when parsing the TCX file.
        return None
    else:
        data['latitude'] = frame.get_value('position_lat') / ((2 ** 32) / 360)
        data['longitude'] = frame.get_value('position_long') / ((2 ** 32) / 360)

    for field in POINTS_COLUMN_NAMES[3:]:
        if frame.has_field(field):
            data[field] = frame.get_value(field)

    return data


def get_dataframes(fname: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Takes the path to a FIT file (as a string) and returns two Pandas
    DataFrames: one containing data about the laps, and one containing
    data about the individual points.
    """

    points_data = []
    laps_data = []
    lap_no = 1
    with fitdecode.FitReader(fname) as fit_file:
        for frame in fit_file:
            if isinstance(frame, fitdecode.records.FitDataMessage):
                if frame.name == 'record':
                    single_point_data = get_fit_point_data(frame)
                    if single_point_data is not None:
                        single_point_data['lap'] = lap_no
                        points_data.append(single_point_data)
                elif frame.name == 'lap':
                    single_lap_data = get_fit_lap_data(frame)
                    single_lap_data['number'] = lap_no
                    laps_data.append(single_lap_data)
                    lap_no += 1

    # Create DataFrames from the data we have collected. If any information is missing from a particular lap or track
    # point, it will show up as a null value or "NaN" in the DataFrame.

    laps_df = pd.DataFrame(laps_data, columns=LAPS_COLUMN_NAMES)
    laps_df.set_index('number', inplace=True)
    points_df = pd.DataFrame(points_data, columns=POINTS_COLUMN_NAMES)

    return laps_df, points_df
gpx_files = os.listdir("activities")

gpx_files.remove(".DS_Store")
runningheatmap_df = {}
coords_df = {}
mymap = folium.Map()
for i in range(len(gpx_files)):
    gpx = gpxpy.parse(open("activities/" + gpx_files[i]))
    track_coords = [[point.latitude, point.longitude, point.elevation]
                    for track in gpx.tracks
                    for segment in track.segments
                    for point in segment.points]
    coords_df = pd.DataFrame(track_coords, columns=['Latitude', 'Longitude', 'Altitude'])
    ref_df = coords_df.drop(["Altitude"], axis=1)
    #mymap = folium.Map(location=[ref_df.Latitude.mean(), ref_df.Longitude.mean()], zoom_start=6, tiles=None)
    folium.PolyLine(ref_df, color='blue', weight=1, opacity=1).add_to(mymap)
    #folium.TileLayer("openstreetmap", name="OpenStreet Map").add_to(mymap)


mymap.save('Activities.html')

# gpx_df, points, type = process_gpx_to_df("2169765006.gpx")
# print(type)
# print(process_gpx_to_df("2169765006.gpx"))

# folium.TileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}", attr="Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC”, name=’Nat Geo Map").add_to(mymap)
# folium.TileLayer("http://tile.stamen.com/terrain/{z}/{x}/{y}.jpg", attr="terrain-bcg", name="Terrain Map").add_to(mymap)
