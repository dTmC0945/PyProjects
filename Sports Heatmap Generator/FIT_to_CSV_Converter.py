from sh import gunzip
import os
from fit_tool.fit_file import FitFile


location = os.listdir("FIT files")
fit_files = [file for file in location if file[-4:].lower() == '.fit']
print(fit_files)
for files in fit_files:
    path = "FIT files/" + files
    fit_file = FitFile.from_file(path)

    out_path = "FIT files/" + files[:-4] + ".csv"
    fit_file.to_csv(out_path)

