from sh import gunzip
import os
from fit_tool.fit_file import FitFile
import pandas as pd
import folium

location = os.listdir("FIT files")
fit_files = [file for file in location if file[-7:].lower() == '.fit.gz']
for file in fit_files:
    gunzip("FIT files/" + file)

path = 'FIT files/8203768911.fit'
fit_file = FitFile.from_file(path)

out_path = 'FIT files/8203768911.csv'
fit_file.to_csv(out_path)

df = pd.read_csv("FIT files/8203768911.csv")
mymap = folium.Map()
result = df[["Value 1", "Value 2"]]
result = result.iloc[100:-100]
print(result.astype(float))

folium.PolyLine(result.astype(float), color='red', weight=2, opacity=1).add_to(mymap)
mymap.save('Act.html')
