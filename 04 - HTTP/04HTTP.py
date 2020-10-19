from flask import Flask, redirect, url_for, request, render_template
import requests  # needs to be installed through pip.
import json
from opencage.geocoder import OpenCageGeocode# Pip install opencage, used for geodecoding of ISS coordinates.
app = Flask(__name__)
from pprint import pprint

# In this folder there is an .html file with a form in it. Submitting the form
# with your name will send a POST request with the form data to this app.
# When pressing submit, it will be processed by the /login route, and
# you will be redirected to /welcome/<name>, where your name will be printed.
# The "else" part is when it is a GET request. The result is the same in this case.
@app.route('/welcome/<name>/')
def welcome(name):
    return f"Weclome {name}!"

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('welcome', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('welcome', name=user))

# Below is a more polished interaction between two separate pages,
# one input and one output page.

@app.route('/grades')
def grades():
    return render_template('grades.html')


@app.route('/results', methods = ['POST', 'GET'])
def results():
    if request.method == 'POST':
        results = request.form
        return render_template('results.html', results=results)


iss_api = r"http://api.open-notify.org/iss-now.json"  # The 'r' before the string makes it a raw string. This is to
# ensure that the string isn't processed by the interpreter in any way.

api_key = "becc1e9dfc254530ad1d58991bcd0ae4"
geocoder = OpenCageGeocode(api_key)

@app.route('/iss')
def iss():
    iss_response = requests.get(iss_api)

    if (iss_response.status_code != 200): # 200 means success.
        print(f"Something went wrong with calling {iss_api}")
    else:
        # The result is given (as with many APIs) in JSON format,
        # which is very close (if not identical) to Python's dicts.
        # However, all responses are returned as pure text. The json()
        # function will turn them into a useable, subscriptable dict.

        iss_json = iss_response.json()
        pprint(iss_json)
        lat = iss_json["iss_position"]["latitude"]
        lon = iss_json["iss_position"]["longitude"]

        geo_results = geocoder.reverse_geocode(lat, lon)
        pprint(geo_results)
        formatted_location = geo_results[0]["formatted"]
        return render_template('iss.html', iss_data=iss_json, lat=lat, lon=lon, location=formatted_location)

if __name__ == '__main__':
    app.run(debug=True)