from sh import gunzip
import os
from fit_tool.fit_file import FitFile
import pandas as pd
import folium

location = os.listdir("FIT files")
fit_files = [file for file in location if file[-7:].lower() == '.fit.gz']
for file in fit_files:
    gunzip("FIT files/" + file)

# path = 'FIT files/8599976892.fit'
# fit_file = FitFile.from_file(path)
# #
# out_path = 'FIT files/8599976892.csv'
# fit_file.to_csv(out_path)

df = pd.read_csv("FIT files/6080193171.csv")
initial_filter = df.loc[df['Type'] == 'Data']

if initial_filter.iloc[0]["Value 0"] == 0:
    exercise_type = "Zwift"
else:
    exercise_type = str(initial_filter.loc[df["Message"] == "sport"].iloc[0]["Value 0"])

print(exercise_type)
gps_data = initial_filter.loc[df["Field 1"] == "position_lat"]

filtered_gps_data = gps_data.loc[df['Message'] == 'record']

filtered_gps_data_lat_lon = filtered_gps_data[["Value 1", "Value 2"]]

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(result)

mymap = folium.Map()

labelled_data = filtered_gps_data_lat_lon.rename(columns={"Value 1": "Latitude", "Value 2": "Longitude"})

labelled_data_float = labelled_data.astype(float)

result = labelled_data_float.query("Latitude < 90")

print(result)

# result = result.iloc[7:-14]
#
# indx = results.loc[results['Latitude'] == 0]
if exercise_type == "Bike":
    folium.PolyLine(result, color="blue", weight=1.5, opacity=1).add_to(mymap)
elif exercise_type == "Trail Run":
    folium.PolyLine(result, color="darkred", weight=1.5, opacity=1).add_to(mymap)
elif exercise_type == "Run":
    folium.PolyLine(result, color="red", weight=1.5, opacity=1).add_to(mymap)
elif exercise_type == "Walk":
    folium.PolyLine(result, color="green", weight=1.5, opacity=1).add_to(mymap)
elif exercise_type == "Zwift":
    folium.PolyLine(result, color="orange", weight=1.5, opacity=1).add_to(mymap)
# elif exercise_type == "Strength":


mymap.save('Act.html')
