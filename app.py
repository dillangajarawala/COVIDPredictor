from flask import Flask, request, redirect, render_template, flash
from api.cases_predictor import CasesPredictor
from api.deaths_predictor import DeathsPredictor

app = Flask(__name__)
app.config.update(DEBUG=True, TEMPLATES_AUTO_RELOAD=True)

cases_predictor = CasesPredictor()
deaths_predictor = DeathsPredictor()


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/predictcasesform', methods=['GET'])
def predict_cases_form():
    return render_template('predict_cases_form.html')

@app.route('/predictcases', methods=["GET"])
def predict_cases():
    error = False
    if "geo_value" in request.args:
        geo_value = request.args['geo_value']
    else:
        flash("You must select a state to predict cases for", 'error')
        error = True
    if "tests_positive" in request.args:
        tests_positive = request.args['tests_positive']
    else:
        flash("You must enter the percentage of COVID tests that are positive", 'error')
        error = True
    if "admissions" in request.args:
        admissions = request.args['admissions']
    else:
        flash("You must enter the percentage of COVID-related hospital visits", 'error')
        error = True
    if "full_time" in request.args:
        full_time = request.args['full_time']
    else:
        flash("You must enter the percentage of mobile devices that spent 6 hours at a location other than their home during the daytime 1 week ago", 'error')
        error = True
    if "visits" in request.args:
        visits = request.args['visits']
    else:
        flash("You must enter the percentage of COVID-related doctor's visits", 'error')
        error = True
    if "fb_illness" in request.args:
        fb_illness = request.args['fb_illness']
    else:
        flash("You must enter the estimated percentage of people with COVID-like illness according to Facebook", 'error')
        error = True
    if "home" in request.args:
        home = request.args['home']
    else:
        flash("You must enter the percentage of mobile devices that did not leave the immediate area of their home 1 week ago", 'error')
        error = True
    if error:
        return render_template("predict_cases_form.html")
    else:
        state = [geo_value.lower()]
        numerical_vars = [tests_positive, admissions, full_time, visits, fb_illness, home]
        cases = CasesPredictor.predict_cases(state, numerical_vars)
        return render_template("predicted_cases.html")

@app.route('/predictdeathsform', methods=["GET"])
def predict_deaths_form():
    return render_template('predict_deaths_form.html')

@app.route('/predictdeaths', methods=["GET"])
def predict_deaths():
    error = False
    if "geo_value" in request.args:
        geo_value = request.args['geo_value']
    else:
        flash("You must select a state to predict cases for", 'error')
        error = True
    if "cases" in request.args:
        cases = request.args['cases']
    else:
        flash("You must the number of cases 1 week ago", 'error')
        error = True
    if "tests_positive" in request.args:
        tests_positive = request.args['tests_positive']
    else:
        flash("You must enter the percentage of COVID tests that were positive 1 week ago", 'error')
        error = True
    if "admissions" in request.args:
        admissions = request.args['admissions']
    else:
        flash("You must enter the percentage of COVID-related hospital visits 1 week ago", 'error')
        error = True
    if "full_time" in request.args:
        full_time = request.args['full_time']
    else:
        flash("You must enter the percentage of mobile devices that spent 6 hours at a location other than their home during the daytime 2 weeks ago", 'error')
        error = True
    if "visits" in request.args:
        visits = request.args['visits']
    else:
        flash("You must enter the percentage of COVID-related doctor's visits 1 week ago", 'error')
        error = True
    if "fb_illness" in request.args:
        fb_illness = request.args['fb_illness']
    else:
        flash("You must enter the estimated percentage of people with COVID-like illness according to Facebook 1 week ago", 'error')
        error = True
    if "home" in request.args:
        home = request.args['home']
    else:
        flash("You must enter the percentage of mobile devices that did not leave the immediate area of their home 2 weeks ago", 'error')
        error = True
    if error:
        return render_template("predict_deaths_form.html")
    else:
        state = geo_value.lower()
        features_to_scale = [tests_positive, admissions, full_time, visits, fb_illness, home]
        deaths = DeathsPredictor.predict_deaths(cases, features_to_scale, state)
        return render_template("predicted_deaths.html")

if __name__ == "__main__":
    app.run()