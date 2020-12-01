import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta

tests = pd.read_csv("tests.csv")

hospital = pd.read_csv("hospital.csv")

search = pd.read_csv("search.csv")

visits = pd.read_csv("visits.csv")

illness = pd.read_csv("illness.csv")

cases = pd.read_csv("new_cases.csv")

time_work = pd.read_csv("time_work.csv")

time_home = pd.read_csv("devices_home.csv")

main = tests.merge(hospital, on=["geo_value", "time_value"])

main = main.merge(search, on=["geo_value", "time_value"])

main = main.merge(visits, on=["geo_value", "time_value"])

main = main.merge(illness, on=["geo_value", "time_value"])

main = main.merge(cases, on=["geo_value", "time_value"])

time_work['time_value'] = time_work['time_value'].map(lambda x: datetime.fromisoformat(x))
time_home['time_value'] = time_home['time_value'].map(lambda x: datetime.fromisoformat(x))
main['time_value'] = main['time_value'].map(lambda x: datetime.fromisoformat(x))

time_work_column = []
for index, row in main.iterrows():
    
    result = time_work[(time_work['geo_value'] == row.geo_value) & (time_work['time_value'] == (row.time_value + timedelta(days=7)))]
    if len(result) > 0:
        time_work_column.append(result.iloc[0].full_time_work_prop)
    else:
        time_work_column.append(np.nan)
    if index % 1000 == 0:
        print(index)
print(len(time_work_column))

main['full_time_work_prop'] = time_work_column

time_home_column = []
for index, row in main.iterrows():
    
    result = time_home[(time_home['geo_value'] == row.geo_value) & (time_home['time_value'] == (row.time_value + timedelta(days=7)))]
    if len(result) > 0:
        time_home_column.append(result.iloc[0].percent_home)
    else:
        time_home_column.append(np.nan)
    if index % 1000 == 0:
        print(index)
print(len(time_home_column))

main['percent_home'] = percent_home_column

main = main.dropna()

main.to_csv("casesmainwithdateoffsets.csv", index=False)