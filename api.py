import flask
from flask import request, jsonify
import csv

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def build_daily_change_timeline(headers, row):
    col = 2
    prev = 0
    timeline = {}
    while col < len(row):
        new = int(row[col])
        # diff = new - prev
        timeline[headers[col]] = new - prev
        prev = new
        col += 1
    return timeline


def build_case_count_timeline(headers, row):
    col = 2
    timeline = {}
    while col < len(row):
        timeline[headers[col]] = row[col]
        col += 1
    return timeline


@app.route('/', methods=['GET'])
def home():
    return "<h1>Texas Department of State Health Services CoVid-19 Data</h1><p>API for tracking the Covid Outbreak in Texas</p>"

@app.route('/api/v1/latest', methods=['GET'])
def latest_county():
    get_all = False
    if 'county' in request.args:
        name = request.args['county']
        name = name.lower()
    else:
        get_all = True

    with open('counties.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        counties = []
        for row in csv_reader:
            if get_all:
                county = {
                    'county': row[0],
                    'population': row[1],
                    'cases': row[-1]
                }
                counties.append(county)
                continue
            elif row[0].lower() == name:
                county = {
                    'county': row[0],
                    'population': row[1],
                    'cases': row[-1]
                }
                return jsonify(county)
    if get_all:
        return jsonify(counties)
    else:
        return 'Error: No county provided. Please specify a county, ex: Travis.'


@app.route('/api/v1/cases/all', methods=['GET'])
def timelines_all():
    with open('counties.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        headers = next(csv_reader)
        counties = []
        for row in csv_reader:
            county = {
                'county': row[0],
                'population': row[1],
                'cases': row[-1],
                'timeline': build_case_count_timeline(headers, row)
            }
            counties.append(county)
    return jsonify(counties)


@app.route('/api/v1/cases', methods=['GET'])
def timeline_county():
    get_all = False
    if 'county' in request.args:
        name = request.args['county']
        name = name.lower()
    else:
        get_all = True
        # return "Error: No county provided. Please specify a county, ex: Travis."

    with open('counties.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        headers = next(csv_reader)
        counties = []
        for row in csv_reader:
            if get_all:
                county = {
                    'county': row[0],
                    'population': row[1],
                    'cases': row[-1],
                    'timeline': build_case_count_timeline(headers, row)
                }
                counties.append(county)
                continue
            elif row[0].lower() == name:
                county = {
                    'county': row[0],
                    'population': row[1],
                    'cases': row[-1],
                    'timeline': build_case_count_timeline(headers, row)
                }
                return jsonify(county)
    if get_all:
        return jsonify(counties)
    else:
        return 'Error: No county provided. Please specify a county, ex: Travis.'


@app.route('/api/v1/dailychange', methods=['GET'])
def daily_change_county():
    get_all = False
    if 'county' in request.args:
        name = request.args['county']
        name = name.lower()
    else:
        get_all = True

    with open('counties.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        headers = next(csv_reader)
        counties = []
        for row in csv_reader:
            if get_all:
                county = {
                    'name': row[0],
                    'population': row[1],
                    'count': row[-1],
                    'timeline': build_daily_change_timeline(headers, row)
                }
                counties.append(county)   
                continue             
            elif row[0].lower() == name:
                county = {
                    'name': row[0],
                    'population': row[1],
                    'count': row[-1],
                    'timeline': build_daily_change_timeline(headers, row)
                }
                return jsonify(county)
    if get_all:
        return jsonify(counties)
    else:
        return 'Error: No county provided. Please specify a county, ex: Travis.'


app.run(port=5000)
