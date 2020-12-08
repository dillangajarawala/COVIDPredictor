from flask import Flask, request, redirect, render_template, flash
from api.cases_predictor import CasesPredictor
from api.deaths_predictor import DeathsPredictor

app = Flask(__name__)
app.config.update(DEBUG=True, TEMPLATES_AUTO_RELOAD=True)

cases_predictor = CasesPredictor()
deaths_predictor = DeathsPredictor()

states = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY']

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/predictcasesform', methods=['GET'])
def predict_cases_form():
    return render_template('predict_cases_form.html', states=states)

@app.route('/predictcases', methods=["GET"])
def predict_cases():
    error = False
    geo_value = request.args['geo_value']
    try:
        tests_positive = float(request.args['tests_positive'])
    except ValueError:
        flash("You must enter the percentage of COVID tests that were positive 1 week ago", 'danger')
        error = True
    try:
        admissions = float(request.args['admissions'])
    except ValueError:
        flash("You must enter the percentage of COVID-related hospital visits 1 week ago", 'danger')
        error = True
    try:
        full_time = float(request.args['full_time'])
    except ValueError:
        flash("You must enter the percentage of mobile devices that spent 6 hours at a location other than their home during the daytime 2 weeks ago", 'danger')
        error = True
    try:
        visits = float(request.args['visits'])
    except ValueError:
        flash("You must enter the percentage of COVID-related doctor's visits 1 week ago", 'danger')
        error = True
    try:
        fb_illness = float(request.args['fb_illness'])
    except ValueError:
        flash("You must enter the estimated percentage of people with COVID-like illness according to Facebook 1 week ago", 'danger')
        error = True
    try:
        home = float(request.args['home'])
    except ValueError:
        flash("You must enter the percentage of mobile devices that did not leave the immediate area of their home 2 weeks ago", 'danger')
        error = True
    if error:
        return render_template("predict_cases_form.html", states=states)
    else:
        state = [geo_value.lower()]
        numerical_vars = [tests_positive, admissions, full_time, visits, fb_illness, home]
        cases = cases_predictor.predict_cases(state, numerical_vars)
        return render_template('predicted_cases.html', cases=cases, state=geo_value, positive_pct= tests_positive, admissions=admissions, full_time=full_time, home=home, fb=fb_illness, visits=visits)

@app.route('/predictdeathsform', methods=["GET"])
def predict_deaths_form():
    return render_template('predict_deaths_form.html', states=states)

@app.route('/predictdeaths', methods=["GET"])
def predict_deaths():
    error = False
    geo_value = request.args['geo_value']
    try:
        cases = int(request.args['cases'])
    except ValueError:
        flash("You must the number of cases 1 week ago", 'danger')
        error = True
    try:
        tests_positive = float(request.args['tests_positive'])
    except ValueError:
        flash("You must enter the percentage of COVID tests that were positive 1 week ago", 'danger')
        error = True
    try:
        admissions = float(request.args['admissions'])
    except ValueError:
        flash("You must enter the percentage of COVID-related hospital visits 1 week ago", 'danger')
        error = True
    try:
        full_time = float(request.args['full_time'])
    except ValueError:
        flash("You must enter the percentage of mobile devices that spent 6 hours at a location other than their home during the daytime 2 weeks ago", 'danger')
        error = True
    try:
        visits = float(request.args['visits'])
    except ValueError:
        flash("You must enter the percentage of COVID-related doctor's visits 1 week ago", 'danger')
        error = True
    try:
        fb_illness = float(request.args['fb_illness'])
    except ValueError:
        flash("You must enter the estimated percentage of people with COVID-like illness according to Facebook 1 week ago", 'danger')
        error = True
    try:
        home = float(request.args['home'])
    except ValueError:
        flash("You must enter the percentage of mobile devices that did not leave the immediate area of their home 2 weeks ago", 'danger')
        error = True
    if error:
        return render_template("predict_deaths_form.html", states=states)
    else:
        state = geo_value.lower()
        features_to_scale = [tests_positive, admissions, full_time, visits, fb_illness, home]
        deaths = deaths_predictor.predict_deaths(cases, features_to_scale, state)
        return render_template("predicted_deaths.html")

if __name__ == "__main__":
    app.run()