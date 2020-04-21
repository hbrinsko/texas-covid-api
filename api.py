import flask
from flask import request, jsonify
import csv
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class county:
  def __init__(self, name,population,cases):
    self.name = name
    self.population = population
    self.cases = cases

@app.route('/', methods=['GET'])
def home():
    return "<h1>Texas Department of State Health Services CoVid-19 Data</h1><p>API for tracking the Covid Outbreak in Texas</p>"

@app.route('/api/v1/counties/latest', methods=['GET'])
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

app.run()