import flask
from flask import request, jsonify
import csv
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def buildDailyChangeTimeline(headers, row):
    col = 2
    prev = 0
    timeline = {}
    while col < len(row):
        new = int(row[col])
        diff = new-prev
        timeline[headers[col]] = diff
        prev = new
        col += 1
    return timeline

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

@app.route('/api/v1/latest/all', methods=['GET'])
def latest_all():
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

@app.route('/api/v1/latest', methods=['GET'])
def latest_county():
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

@app.route('/api/v1/timeline/all', methods=['GET'])
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

@app.route('/api/v1/timeline', methods=['GET'])
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

@app.route('/api/v1/dailychange', methods=['GET'])
def daily_change_county():
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
                        'timeline': buildDailyChangeTimeline(headers, row)
                    }
                    return jsonify(county)
    return 'County not valid'

app.run(port=5000)