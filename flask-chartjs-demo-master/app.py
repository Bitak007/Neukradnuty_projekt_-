from flask import render_template, Flask, jsonify
import os, random, csv, json, urllib2, requests
api_key = "9c4572da6dce19ff1bc941fe8310338f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name ='Opava,cz'
complete_url = base_url + "q=" + city_name + "&appid=" + api_key

app = Flask(__name__)

def wpjson():
    r=urllib2.urlopen(complete_url)
    data=json.load(r)
    return data

@app.route('/datawp')
def datawp():
    data = wpjson()
    return render_template('datawp.jinja2',data = data)


@app.route('/')
def index():
    # get data from database or mqtt whatever...
    title = 'Hi'
    labels = list(range(1, 20))
    data = [random.randint(-100, 100) for x in labels]

    return render_template('index.html', data={'title': title, 'data': data, 'labels': labels} )

@app.route('/get_new_data/')
def get_new_data():
    # simulate incremental data for ajax call...
    nwe_data = {'value': random.randint(-100, 100)}
    return jsonify(nwe_data)

if __name__ == '__main__':
    app.run()
