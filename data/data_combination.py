import pandas as pd

tests = pd.read_csv("tests.csv")

hospital = pd.read_csv("hospital.csv")

search = pd.read_csv("search.csv")

time_work = pd.read_csv("time_work.csv")

visits = pd.read_csv("visits.csv")

illness = pd.read_csv("illness.csv")

cases = pd.read_csv("new_cases.csv")

deaths = pd.read_csv("new_deaths.csv")

time_home = pd.read_csv("devices_home.csv")

main = tests.merge(hospital, on=["geo_value", "time_value"])

main = main.merge(search, on=["geo_value", "time_value"])

main = main.merge(time_work, on=["geo_value", "time_value"])

main = main.merge(time_home, on=["geo_value", "time_value"])

main = main.merge(visits, on=["geo_value", "time_value"])

main = main.merge(illness, on=["geo_value", "time_value"])

main = main.merge(cases, on=["geo_value", "time_value"])

main = main.merge(deaths, on=["geo_value", "time_value"])

main.to_csv("main2.csv", index=False)