# import csv
# import os
# import fitparse
# import pytz
#
# allowed_fields = ['timestamp', 'position_lat', 'position_long', 'distance',
#                   'enhanced_altitude', 'altitude', 'enhanced_speed',
#                   'speed', 'heart_rate', 'cadence', 'fractional_cadence']
# required_fields = ['timestamp', 'position_lat', 'position_long', 'altitude']
#
# UTC = pytz.UTC
# CST = pytz.timezone('US/Central')
#
# def write_fitfile_to_csv(fitfile, output_file='test_output.csv'):
#     messages = fitfile.messages
#     data = []
#     for m in messages:
#         skip = False
#         if not hasattr(m, 'fields'):
#             continue
#         fields = m.fields
#         # check for important data types
#         mdata = {}
#         for field in fields:
#             if field.name in allowed_fields:
#                 if field.name == 'timestamp':
#                     mdata[field.name] = 0
#                 else:
#                     mdata[field.name] = field.value
#         for rf in required_fields:
#             if rf not in mdata:
#                 skip = True
#         if not skip:
#             data.append(mdata)
#     # write to csv
#     with open(output_file, 'w') as f:
#         writer = csv.writer(f)
#         writer.writerow(allowed_fields)
#         for entry in data:
#             writer.writerow([str(entry.get(k, '')) for k in allowed_fields])
#     print('wrote %s' % output_file)
#
#
# files = os.listdir()
# fit_files = [file for file in files if file[-4:].lower() == '.fit']
# for file in fit_files:
#     new_filename = file[:-4] + '.csv'
#     if os.path.exists(new_filename):
#         # print('%s already exists. skipping.' % new_filename)
#         continue
#     fitfile = fitparse.FitFile(file, data_processor=fitparse.StandardUnitsDataProcessor())
#
#     print('converting %s' % file)
#     write_fitfile_to_csv(fitfile, new_filename)
# print('finished conversions')

"""Some functions for parsing a FIT file (specifically, a FIT file
generated by a Garmin vívoactive 3) and creating a Pandas DataFrame
with the data.
"""

from datetime import datetime, timedelta
from typing import Dict, Union, Optional, Tuple

import pandas as pd

import fitdecode

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

fname = "~/"  # Path to FIT file to be given as first argument to script
laps_df, points_df = get_dataframes("6531086260.fit")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(points_df)
