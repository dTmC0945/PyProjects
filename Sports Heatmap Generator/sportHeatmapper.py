from sh import gunzip
import os
from fit_tool.fit_file import FitFile
import pandas as pd
import folium
import FITtoGPS as f2g
location = os.listdir("FIT")
fit_files = [file for file in location if file[-4:].lower() == '.fit']


mymap = folium.Map()

for file in fit_files:
    sport, result = f2g.FITtoGPS(file)
    if len(result) > 10:
    #df = pd.read_csv("FIT files/" + file)
    #filteredd_df = df.loc[df['Type'] == 'Data']
    #filtered_df = filteredd_df.loc[df['Message'] == 'record'].iloc[5:]
    #result = filtered_df[["Value 1", "Value 2"]]
    #results = result.rename(columns={"Value 1": "Latitude", "Value 2": "Longitude"})
        if bool(sport):
            if sport[0] == "name: Walk":
                folium.PolyLine(result.astype(float), color='green', weight=1.5, opacity=1).add_to(mymap)
            elif sport[0] == "name: Bike":
                folium.PolyLine(result.astype(float), color='blue', weight=1.5, opacity=1).add_to(mymap)
            elif sport[0] == "name: Run":
                folium.PolyLine(result.astype(float), color='red', weight=1.5, opacity=1).add_to(mymap)
            elif sport[0] == "name: Trail Run":
                folium.PolyLine(result.astype(float), color='darkred', weight=1.5, opacity=1).add_to(mymap)
            elif sport[0] == "name: Open Water":
                folium.PolyLine(result.astype(float), color='cadetblue', weight=1.5, opacity=1).add_to(mymap)
            elif sport[0] == "name: Hike":
                folium.PolyLine(result.astype(float), color='purple', weight=1.5, opacity=1).add_to(mymap)
            else:
                folium.PolyLine(result.astype(float), color='red', weight=1.5, opacity=1).add_to(mymap)

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(result)


# result = result.iloc[7:-14]
#
# indx = results.loc[results['Latitude'] == 0]
#
mymap.save('Act.html')
