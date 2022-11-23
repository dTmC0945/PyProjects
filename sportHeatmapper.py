import gpxpy
import pandas as pd
import gpxpy.gpx as gpx


def process_gpx_to_df(file_name):
    gpx = gpxpy.parse(open(file_name))
    # (1)make DataFrame
    track = gpx.tracks[0]
    segment = track.segments[0]
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


    return gpx_df, points
