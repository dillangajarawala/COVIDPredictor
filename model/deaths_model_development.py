from pickle import dump

import numpy as np
import pandas as pd
from sklearn import linear_model, preprocessing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("deathsmainwithdateoffsets.csv")

pop_hash = {'al': 4903185, 'ak': 731545, 'as': 55312, 'az': 7278717, 'ar': 3017804, 'ca': 39512223, 'co': 5758736, 'ct': 3565287, 'de': 973764, 'dc': 705749, 'fm': 104929, 'fl': 21477737, 'ga': 10617423, 'gu': 167294, 'hi': 1415872, 'id': 1787065, 'il': 12671821, 'in': 6732219, 'ia': 3155070, 'ks': 2913314, 'ky': 4467673, 'la': 4648794, 'me': 1344212, 'mh': 58791, 'md': 6045680, 'ma': 6892503, 'mi': 9986857, 'mn': 5639632, 'ms': 2976149, 'mo': 6137428, 'mt': 1068778, 'ne': 1934408, 'nv': 3080156, 'nh': 1359711, 'nj': 8882190, 'nm': 2096829, 'ny': 19453561, 'nc': 10488084, 'nd': 762062, 'mp': 51994, 'oh': 11689100, 'ok': 3956971, 'or': 4217737, 'pw': 18008, 'pa': 12801989, 'pr': 3193694, 'ri': 1059361, 'sc': 5148714, 'sd': 884659, 'tn': 6829174, 'tx': 28995881, 'ut': 3205958, 'vt': 623989, 'vi': 104578, 'va': 8535519, 'wa': 7614893, 'wv': 1792147, 'wi': 5822434, 'wy': 578759}

df["geo_value"] = df["geo_value"].map(lambda x: pop_hash[x])

features_num = ["new_cases"]
features_scale = ["geo_value", "percent_covid_tests_positive", "covid_admissions", "full_time_work_prop", "percent_covid_visits", "fb_illness", "percent_home"]

X_scale = df[features_scale]
X_num = df[features_num]

scaler = preprocessing.MinMaxScaler()
scaler.fit(X_scale)
scaled = scaler.transform(X_scale)
print(scaled)
X_scaled_proc = pd.DataFrame(scaled.tolist(), columns=["population", "percent_covid_tests_positive", "covid_admissions", "full_time_work_prop", "percent_covid_visits", "fb_illness", "percent_home"])

# merge features
X = pd.concat([X_scaled_proc, X_num], axis=1, sort=False)
X.head()

y = df["new_deaths"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Coefficient: " + model.coef_)

print("Error: " + mean_squared_error(y_test, y_pred))

print("R^2 Score: " + r2_score(y_test, y_pred))

dump(model, open('deathsmodel.pkl', 'wb'))

dump(scaler, open('deathsscaler.pkl', 'wb'))