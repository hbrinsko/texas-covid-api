import flask
from flask import request, jsonify
import csv
import json
from collections import OrderedDict

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def buildTimeline(headers, row):
    col = 2
    timeline = {}
    while col < len(row):
        timeline[headers[col]] = row[col]
        col += 1
    return timeline

@app.route('/', methods=['GET'])
def home():
    return "<h1>Texas Department of State Health Services CoVid-19 Data</h1><p>API for tracking the Covid Outbreak in Texas</p>"

@app.route('/api/v1/counties/latest/all', methods=['GET'])
def counties_all():
    with open('counties.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            next(csv_reader)
            counties = []
            for row in csv_reader:
                county = {
                    'name': row[0],
                    'population': row[1],
                    'count': row[-1]
                }
                counties.append(county)
    return jsonify(counties)

@app.route('/api/v1/counties/latest', methods=['GET'])
def counties_county():
    if 'county' in request.args:
        name = request.args['county']
        name = name.lower()
    else:
        return "Error: No county provided. Please specify a county, ex: Travis."

    with open('counties.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                if row[0].lower() == name:
                    county = {
                        'name': row[0],
                        'population': row[1],
                        'count': row[-1]
                    }
                    return jsonify(county)
    return 'County not valid'

@app.route('/api/v1/counties/timeline/all', methods=['GET'])
def timelines_all():
    with open('counties.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headers = next(csv_reader)
            counties = []
            for row in csv_reader:
                county = {
                    'name': row[0],
                    'population': row[1],
                    'count': row[-1],
                    'timeline': buildTimeline(headers, row)
                }
                counties.append(county)
    return jsonify(counties)

@app.route('/api/v1/counties/timeline', methods=['GET'])
def timeline_county():
    if 'county' in request.args:
        name = request.args['county']
        name = name.lower()
    else:
        return "Error: No county provided. Please specify a county, ex: Travis."

    with open('counties.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            headers = next(csv_reader)
            for row in csv_reader:
                if row[0].lower() == name:
                    county = {
                        'name': row[0],
                        'population': row[1],
                        'count': row[-1],
                        'timeline': buildTimeline(headers, row)
                    }
                    return jsonify(county)
    return 'County not valid'

app.run(port=5000)