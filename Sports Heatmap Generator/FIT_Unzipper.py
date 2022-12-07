from sh import gunzip
import os
from fit_tool.fit_file import FitFile
import pandas as pd

location = os.listdir("FIT files")
fit_files = [file for file in location if file[-7:].lower() == '.fit.gz']
for file in fit_files:
    gunzip("FIT files/" + file)

#path = 'FIT files/7138243092.fit'
#fit_file = FitFile.from_file(path)

#out_path = 'FIT files/7138243092.csv'
#fit_file.to_csv(out_path)

df = pd.read_csv("FIT files/7138243092.csv")

print(df)