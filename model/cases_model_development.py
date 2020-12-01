import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from pickle import dump

df = pd.read_csv("casesmainwithdateoffsets.csv")

features_num = ["percent_covid_tests_positive_smoothed", "covid_admissions", "full_time_work_prop", "percent_covid_visits", "fb_illness", "percent_home"]
features_cat = ["geo_value"]

X_cat = df[features_cat]
X_num = df[features_num]

enc = preprocessing.OneHotEncoder()
enc.fit(X_cat)
one_hot = enc.transform(X_cat)

X_cat_proc = pd.DataFrame(one_hot.toarray(), columns=enc.get_feature_names())

# merge features
X = pd.concat([X_cat_proc, X_num], axis=1, sort=False)
X.head()

y = df["new_cases"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Coefficient: " + model.coef_)

print("Error: " + mean_squared_error(y_test, y_pred))

print("R^2 Score: " + r2_score(y_test, y_pred))

dump(model, open('casesmodel.pkl', 'wb'))
dump(enc, open('casesenc.pkl', 'wb'))