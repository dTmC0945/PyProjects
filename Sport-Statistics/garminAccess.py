import garminconnect
import pandas as pd

garmin = garminconnect.Garmin("daniel@mcguiness.co.uk", "23Gg1993")
garmin.login()

import os

GARTH_HOME = os.getenv("GARTH_HOME", "~/.garth")
garmin.garth.dump(GARTH_HOME)

from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
yesterday = yesterday.isoformat()

df = pd.DataFrame(garmin.get_personal_record()[:2])

print(df)

