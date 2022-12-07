from sh import gunzip
import os
from fit_tool.fit_file import FitFile
import pandas as pd
import folium

location = os.listdir("FIT files")
csv_files = [file for file in location if file[-4:].lower() == '.csv']

mymap = folium.Map()

for file in csv_files:
    df = pd.read_csv("FIT files/" + file)
    filteredd_df = df.loc[df['Type'] == 'Data']
    filtered_df = filteredd_df.loc[df['Message'] == 'record'].iloc[5:]
    result = filtered_df[["Value 1", "Value 2"]]
    results = result.rename(columns={"Value 1": "Latitude", "Value 2": "Longitude"})
    folium.PolyLine(result.astype(float), color='green', weight=3, opacity=1).add_to(mymap)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(result)


# result = result.iloc[7:-14]
#
# indx = results.loc[results['Latitude'] == 0]
#
mymap.save('Act.html')
