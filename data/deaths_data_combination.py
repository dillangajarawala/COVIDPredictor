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

deaths = pd.read_csv("new_deaths.csv")

time_work = pd.read_csv("time_work.csv")

time_home = pd.read_csv("devices_home.csv")

deaths_main = deaths

deaths_main['time_value'] = deaths_main['time_value'].map(lambda x: datetime.fromisoformat(x))
hospital['time_value'] = hospital['time_value'].map(lambda x: datetime.fromisoformat(x))
tests['time_value'] = tests['time_value'].map(lambda x: datetime.fromisoformat(x))
search['time_value'] = search['time_value'].map(lambda x: datetime.fromisoformat(x))
visits['time_value'] = visits['time_value'].map(lambda x: datetime.fromisoformat(x))
illness['time_value'] = illness['time_value'].map(lambda x: datetime.fromisoformat(x))
cases['time_value'] = cases['time_value'].map(lambda x: datetime.fromisoformat(x))
time_work['time_value'] = time_work['time_value'].map(lambda x: datetime.fromisoformat(x))
time_home['time_value'] = time_home['time_value'].map(lambda x: datetime.fromisoformat(x))

hospital_admissions_column = []
for index, row in deaths_main.iterrows():
    
    result = hospital[(hospital['geo_value'] == row.geo_value) & (hospital['time_value'] == (row.time_value - timedelta(days=7)))]
    if len(result) > 0:
        hospital_admissions_column.append(result.iloc[0].covid_admissions)
    else:
        hospital_admissions_column.append(np.nan)
    if index % 1000 == 0:
        print(index)
print(len(hospital_admissions_column))
deaths_main['covid_admissions'] = hospital_admissions_column

testing_column = []
for index, row in deaths_main.iterrows():
    
    result = tests[(tests['geo_value'] == row.geo_value) & (tests['time_value'] == (row.time_value - timedelta(days=7)))]
    if len(result) > 0:
        try:
            testing_column.append(result.iloc[0].percent_covid_tests_positive_smoothed)
        except:
            print(result)
    else:
        testing_column.append(np.nan)
    if index % 1000 == 0:
        print(index)
print(len(testing_column))
deaths_main['percent_covid_tests_positive'] = testing_column

search_column = []
for index, row in deaths_main.iterrows():
    
    result = search[(search['geo_value'] == row.geo_value) & (search['time_value'] == (row.time_value - timedelta(days=7)))]
    if len(result) > 0:
        search_column.append(result.iloc[0].raw_search)
    else:
        search_column.append(np.nan)
    if index % 1000 == 0:
        print(index)
print(len(search_column))
deaths_main['raw_search'] = search_column

visits_column = []
for index, row in deaths_main.iterrows():
    
    result = visits[(visits['geo_value'] == row.geo_value) & (visits['time_value'] == (row.time_value - timedelta(days=7)))]
    if len(result) > 0:
        visits_column.append(result.iloc[0].percent_covid_visits)
    else:
        visits_column.append(np.nan)
    if index % 1000 == 0:
        print(index)
print(len(visits_column))
deaths_main['percent_covid_visits'] = visits_column

fb_column = []
for index, row in deaths_main.iterrows():
    
    result = illness[(illness['geo_value'] == row.geo_value) & (illness['time_value'] == (row.time_value - timedelta(days=7)))]
    if len(result) > 0:
        fb_column.append(result.iloc[0].fb_illness)
    else:
        fb_column.append(np.nan)
    if index % 1000 == 0:
        print(index)
print(len(fb_column))
deaths_main['fb_illness'] = fb_column

cases_column = []
for index, row in deaths_main.iterrows():
    
    result = cases[(cases['geo_value'] == row.geo_value) & (cases['time_value'] == (row.time_value - timedelta(days=7)))]
    if len(vresultal) > 0:
        try:
            cases_column.append(result.iloc[0].new_cases)
        except:
            print(result)
    else:
        cases_column.append(np.nan)
    if index % 1000 == 0:
        print(index)
print(len(cases_column))
deaths_main['new_cases'] = cases_column'

time_work_column = []
for index, row in deaths_main.iterrows():
    
    result = time_work[(time_work['geo_value'] == row.geo_value) & (time_work['time_value'] == (row.time_value - timedelta(days=14)))]
    if len(result) > 0:
        try:
            time_work_column.append(result.iloc[0].full_time_work_prop)
        except:
            print(result)
    else:
        time_work_column.append(np.nan)
    if index % 1000 == 0:
        print(index)
print(len(time_work_column))
deaths_main['full_time_work_prop'] = time_work_column

time_home_column = []
for index, row in deaths_main.iterrows():
    
    result = time_home[(time_home['geo_value'] == row.geo_value) & (time_home['time_value'] == (row.time_value - timedelta(days=14)))]
    if len(result) > 0:
        try:
            time_home_column.append(result.iloc[0].percent_home)
        except:
            print(result)
    else:
        time_home_column.append(np.nan)
    if index % 1000 == 0:
        print(index)
print(len(time_home_column))
deaths_main['percent_home'] = time_home_column

deaths_main = deaths_main.dropna()
deaths_main.to_csv("deathsmainwithdateoffsets.csv", index=False)