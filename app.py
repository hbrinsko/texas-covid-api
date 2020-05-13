import flask
from flask import request, jsonify
import csv
import service
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Texas Department of State Health Services CoVid-19 Data</h1><p>API for tracking the Covid Outbreak in Texas</p>"

@app.route('/api/counties', methods=['GET'])
def get_counties():
    counties = service.get_counties()
    return jsonify(counties)



@app.route('/api/latest', methods=['GET'])
def latest_county():
    get_all = False
    names = []
    if 'county' in request.args:
        names = request.args['county']
        names = names.lower().split(',')
    else:
        get_all = True

    counties = service.get_latest(get_all, names)

    if len(counties) > 0:
        return jsonify(counties)
    else:
        return 'Error: No county provided. Please specify a county, ex: Travis.'


@app.route('/api/timeline', methods=['GET'])
def timeline_county():
    get_all = False
    time_range = 0
    names = []
    if 'county' in request.args:
        names = request.args['county']
        names = names.lower().split(',')
    else:
        get_all = True

    if 'range' in request.args:
        time_range = int(request.args['range'])
    
    if 'type' in request.args:
        calculation = request.args['type']
    else:
        calculation = 'daily'

    if 'data' in request.args:
        data_source = request.args['data']
    else:
        data_source = 'data'    

    counties = service.get_timeline(get_all, time_range, names, calculation, data_source)

    if len(counties) > 0:
        return jsonify(counties)
    else:
        return 'Error: No county provided. Please specify a county, ex: Travis.'


if __name__ == "__main__":
    app.run()
