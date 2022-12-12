import fitparse
import pandas as pd


df = pd.DataFrame([])
array = []
# Load the FIT file
fitfile = fitparse.FitFile("6104083085.fit")

# Iterate over all messages of type "record"
# (other types include "device_info", "file_creator", "event", etc)
for record in fitfile.get_messages("record"):
    # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
    for data in record:


        # Print the name and value of the data (and the units if it has any)
         if data.units:
             array.append(data.value)
             print(" * {}: {} ({})".format(data.name, data.value, data.units))
         else:
             print(" * {}: {}".format(data.name, data.value))

    print("---")

print(array)