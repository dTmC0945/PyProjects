from sh import gunzip
import os

location = os.listdir("FIT files")
fit_files = [file for file in location if file[-7:].lower() == '.fit.gz']
for file in fit_files:
    gunzip("FIT files/" + file)