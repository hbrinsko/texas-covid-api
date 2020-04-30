import flask
from flask import request, jsonify
import csv
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

def build_daily_change_timeline(headers, row, time_range):
    col = 2
    prev = 0
    time_range = time_range
    if time_range != 0:
        col = len(row) - time_range
    timeline = []
    while col < len(row):
        new = int(row[col])
        date = {
            'date': headers[col],
            'cases': new - prev
        }
        timeline.append(date)
        prev = new
        col += 1
    return timeline


def build_case_count_timeline(headers, row, time_range):
    col = 2
    time_range = time_range
    if time_range != 0:
        col = len(row) - time_range
    timeline = []
    while col < len(row):
        date = {
            'date': headers[col],
            'cases': int(row[col])
        }
        timeline.append(date)
        col += 1
    return timeline


@app.route('/', methods=['GET'])
def home():
    return "<h1>Texas Department of State Health Services CoVid-19 Data</h1><p>API for tracking the Covid Outbreak in Texas</p>"

@app.route('/api/counties', methods=['GET'])
def get_counties():
    with open('counties.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        counties = []
        for row in csv_reader:
            name = row[0]
            counties.append(name)
    return jsonify(counties)



@app.route('/api/latest', methods=['GET'])
def latest_county():
    get_all = False
    if 'county' in request.args:
        names = request.args['county']
        names = names.lower().split(',')
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
                    'population': int(row[1].replace(',','')),
                    'cases': int(row[-1])
                }
                counties.append(county)
                continue
            elif row[0].lower().replace(' ','') in names:
                county = {
                    'county': row[0],
                    'population': int(row[1].replace(',','')),
                    'cases': int(row[-1])
                }
                counties.append(county)
    if len(counties) > 0:
        return jsonify(counties)
    else:
        return 'Error: No county provided. Please specify a county, ex: Travis.'


@app.route('/api/cases', methods=['GET'])
def timeline_county():
    get_all = False
    time_range = 0
    if 'county' in request.args:
        names = request.args['county']
        names = names.lower().split(',')
    else:
        get_all = True

    if 'range' in request.args:
        time_range = int(request.args['range'])

    with open('counties.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        headers = next(csv_reader)
        counties = []
        for row in csv_reader:
            if get_all:
                county = {
                    'county': row[0],
                    'population': int(row[1].replace(',','')),
                    'cases': int(row[-1]),
                    'timeline': build_case_count_timeline(headers, row, time_range)
                }
                counties.append(county)
                continue
            elif row[0].lower().replace(' ','') in names:
                county = {
                    'county': row[0],
                    'population': int(row[1].replace(',','')),
                    'cases': int(row[-1]),
                    'timeline': build_case_count_timeline(headers, row, time_range)
                }
                counties.append(county)
    if len(counties) > 0:
        return jsonify(counties)
    else:
        return 'Error: No county provided. Please specify a county, ex: Travis.'


@app.route('/api/dailychange', methods=['GET'])
def daily_change_county():
    get_all = False
    time_range = 0
    if 'county' in request.args:
        names = request.args['county']
        names = names.lower().split(',')
    else:
        get_all = True

    if 'range' in request.args:
        time_range = int(request.args['range'])    

    with open('counties.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        headers = next(csv_reader)
        counties = []
        for row in csv_reader:
            if get_all:
                county = {
                    'county': row[0],
                    'population': int(row[1].replace(',','')),
                    'count': int(row[-1]),
                    'timeline': build_daily_change_timeline(headers, row, time_range)
                }
                counties.append(county)   
                continue             
            elif row[0].lower().replace(' ','') in names:
                county = {
                    'county': row[0],
                    'population': int(row[1].replace(',','')),
                    'count': int(row[-1]),
                    'timeline': build_daily_change_timeline(headers, row, time_range)
                }
                counties.append(county)
    if len(counties) > 0:
        return jsonify(counties)
    else:
        return 'Error: No county provided. Please specify a county, ex: Travis.'


if __name__ == "__main__":
    app.run()
