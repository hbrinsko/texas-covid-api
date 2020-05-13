import csv

def build_timeline(headers, row, time_range, chart):
    col = 2
    prev = 0
    time_range = time_range
    if time_range != 0:
        col = len(row) - time_range
        prev = int(row[col-1])
    timeline = []
    while col < len(row):
        new = int(row[col])
        if (chart == "daily"):
            date = {
                'date': headers[col],
                'amount': new - prev
            }
        elif (chart == "total"): 
            date = {
                'date': headers[col],
                'amount': int(row[col])
            }
        timeline.append(date)
        prev = new
        col += 1
    return timeline

def get_timeline(get_all, time_range, names, timeline, data_source):
    file = data_source + '.csv'
    with open(file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        headers = next(csv_reader)
        counties = []
        for row in csv_reader:
            if get_all:
                county = {
                    'county': row[0],
                    'population': int(row[1].replace(',','')),
                     data_source: int(row[-1]),
                    'timeline': build_timeline(headers, row, time_range, timeline)
                }
                counties.append(county)
                continue
            elif row[0].lower().replace(' ','') in names:
                county = {
                    'county': row[0],
                    'population': int(row[1].replace(',','')),
                     data_source: int(row[-1]),
                    'timeline': build_timeline(headers, row, time_range, timeline)
                }
                counties.append(county)
    return counties

def get_latest(get_all, names):
    with open('cases.csv', 'r') as csvfile:
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
    return counties

def get_counties():
    with open('cases.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        counties = []
        for row in csv_reader:
            name = row[0]
            counties.append(name)
    return counties