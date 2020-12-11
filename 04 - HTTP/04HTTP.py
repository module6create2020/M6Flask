from flask import Flask, redirect, url_for, request, render_template
import requests
import json
from opencage.geocoder import OpenCageGeocode # Used for geodecoding of ISS coordinates.
app = Flask(__name__)
from pprint import pprint


@app.route('/')
def home():
    return redirect('/grades')


@app.route('/grades')
def grades():
    return redirect(url_for('login'))

@app.route('/welcome/<name>/')
def welcome(name):
    return f"Weclome {name}!"

@app.route('/results', methods = ['POST', 'GET'])
def results():
    if request.method == 'POST':  # Submitting a form will create a POST request
        results = request.form  # Get the form data from the HTTP data.
        return render_template('results.html', results=results)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':  # If a request is sent
        user = request.form['nm']
        return redirect(url_for('welcome', name=user))
    else:  # If no request is sent (Pages are retreived using a GET method).
        return render_template('login.html')


iss_api = r"http://api.open-notify.org/iss-now.json"  # The 'r' before the string makes it a raw string. This is to
# ensure that the string isn't processed by the interpreter in any way.

# Get your own API key at https://opencagedata.com/api
api_key = "REPLACE_THIS_WITH_YOUR_OWN_KEY"
geocoder = OpenCageGeocode(api_key)

@app.route('/iss')
def iss():
    iss_response = requests.get(iss_api)  # Send a request to the API URL.

    if (iss_response.status_code != 200): # 200 means success.
        print(f"Something went wrong with calling {iss_api}")
    else:
        # The result is given (as with many APIs) in JSON format,
        # which is very similar to Python's dicts.
        # However, all responses are returned as pure text. The json()
        # function will turn them into a useable, subscriptable dict.

        iss_json = iss_response.json()
        pprint(iss_json) # pprint means pretty print.
        lat = iss_json["iss_position"]["latitude"]
        lon = iss_json["iss_position"]["longitude"]

        geo_results = geocoder.reverse_geocode(lat, lon)
        pprint(geo_results)
        formatted_location = geo_results[0]["formatted"]
        return render_template('iss.html', iss_data=iss_json, lat=lat, lon=lon, location=formatted_location)

if __name__ == '__main__':
    app.run(debug=True)