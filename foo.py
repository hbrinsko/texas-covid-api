import flask
from flask import request, jsonify
import csv
import json

def buildTimeline(headers, row):
    col = 2
    timeline = {}
    while col < len(row):
        timeline[headers[col]] = row[col]
        col += 1
    return timeline

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

def main():
    with open('counties.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
                county = {
                    'name': row[0],
                    'population': row[1],
                    'count': row[-1],
                    'timeline': buildDailyChangeTimeline(headers, row)
                }
                print(county)

main()

