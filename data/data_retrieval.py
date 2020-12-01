import covidcast
import pandas as pd

print("Retrieving Data...")

visits = covidcast.signal("chng", "smoothed_outpatient_covid", geo_type="state")
print("Visits done...")

search = covidcast.signal("ght", "raw_search", geo_type="state")
print("Searches done...")

hospital = covidcast.signal("hospital-admissions", "smoothed_covid19_from_claims", geo_type="state")
print("Hospital done...")

new_cases = covidcast.signal("jhu-csse", "confirmed_incidence_num", geo_type="state")
print("Cases done...")

time_work = covidcast.signal("safegraph", "full_time_work_prop", geo_type="state")
print("Mobile Devices done...")

time_home = covidcast.signal("safegraph", "completely_home_prop", geo_type="state")
print("Mobile Devices home done...")

tests = covidcast.signal("quidel", "covid_ag_smoothed_pct_positive", geo_type="state")
print("Tests done...")

new_deaths = covidcast.signal("jhu-csse", "deaths_incidence_num", geo_type="state")
print("Deaths done...")

illness = covidcast.signal("fb-survey", "smoothed_wcli", geo_type="state")
print("FB Survey done...")

print("Retrieved All Data")

visits = visits.drop(columns=['signal', 'geo_type', 'data_source', 'stderr', 'issue', 'direction', 'lag', 'sample_size'])
visits = visits.rename(columns={"value": "percent_covid_visits"})

search = search.drop(columns=['signal', 'geo_type', 'data_source', 'stderr', 'issue', 'direction', 'lag', 'sample_size'])
search = search.rename(columns={"value": "raw_search"})

hospital = hospital.drop(columns=['signal', 'geo_type', 'data_source', 'stderr', 'issue', 'direction', 'lag', 'sample_size'])
hospital = hospital.rename(columns={"value": "covid_admissions"})

new_cases = new_cases.drop(columns=['signal', 'geo_type', 'data_source', 'stderr', 'issue', 'direction', 'lag', 'sample_size'])
new_cases = new_cases.rename(columns={"value": "new_cases"})

tests = tests.drop(columns=['signal', 'geo_type', 'data_source', 'stderr', 'issue', 'direction', 'lag', 'sample_size'])
tests = tests.rename(columns={"value": "percent_covid_tests_positive"})

time_work = time_work.drop(columns=['signal', 'geo_type', 'data_source', 'stderr', 'issue', 'direction', 'lag', 'sample_size'])
time_work = time_work.rename(columns={"value": "full_time_work_prop"})
time_work["full_time_work_prop"] = time_work["full_time_work_prop"].map(lambda x: x*100)

time_home = time_home.drop(columns=['signal', 'geo_type', 'data_source', 'stderr', 'issue', 'direction', 'lag', 'sample_size'])
time_home = time_home.rename(columns={"value": "percent_home"})
time_home["percent_home"] = time_home["percent_home"].map(lambda x: x*100)

new_deaths = new_deaths.drop(columns=['signal', 'geo_type', 'data_source', 'stderr', 'issue', 'direction', 'lag', 'sample_size'])
new_deaths = new_deaths.rename(columns={"value": "new_deaths"})

illness = illness.drop(columns=['signal', 'geo_type', 'data_source', 'stderr', 'issue', 'direction', 'lag', 'sample_size'])
illness = illness.rename(columns={"value": "fb_illness"})

print("Data manipulation complete")

visits.to_csv("visits.csv", index=False)

search.to_csv("search.csv", index=False)

hospital.to_csv("hospital.csv", index=False)

new_cases.to_csv("new_cases.csv", index=False)

new_deaths.to_csv("new_deaths.csv", index=False)

tests.to_csv("tests.csv", index=False)

time_work.to_csv("time_work.csv", index=False)

time_home.to_csv("time_home.csv", index=False)

illness.to_csv("illness.csv", index=False)

print("Data exported to CSV")