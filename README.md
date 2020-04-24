<h1 align="center">
    Texas Coronavirus Tracker API
</h1>

## Setting up the Python Application
Provides up-to-date data about Coronavirus outbreak in Texas.

Assuming that before you begin, you will have [Python](http://www.python.org/) and [pip](http://www.pip-installer.org/en/latest/) installed on your system and available at the command line.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run app on http://127.0.0.1:5000/:
```bash
python3 api.py
```
## Data Source
**Texas Department of State Health Services** - https://www.dshs.texas.gov/coronavirus/TexasCOVID19DailyCountyCaseCountData.xlsx - 
* Updated Daily. This Excel files contains daily case counts by county, beginning March 4, 2020.
* County-level case counts were not available on March 7, March 8, and March 14.
* Population data is based on Texas population projections, 2020 (https://www.dshs.texas.gov/chs/popdat/st2020.shtm).

### Endpoint Information

__Query Parameters__

All endpoints have an optional parameter for county name. If no county is provided, it will provide information for all counties.

| __Query string parameter__ | __Description__                                                                  | __Type__ |
| -------------------------- | -------------------------------------------------------------------------------- | -------- |
| county                     | Name of county for pulling data. Ex: *Travis* | String   |





__Latest__

```http
GET /api/v1/latest
```

Gets latest amount of total confirmed cases

__Sample response__
```json
  {
    "cases": "10", 
    "county": "Anderson", 
    "population": "62,245"
  }
```

__Cases__
```http
GET /api/v1/cases
```
Gets timeline of case count

__Sample response__
```json
  {
    "cases": "4977", 
    "county": "Harris", 
    "population": "4,885,616", 
    "timeline": {
      "03-04-2020": "0", 
      "03-05-2020": "0", 
      "03-06-2020": "4", 
      "03-09-2020": "5", 
      "03-10-2020": "5"
      }
  }
```

__New Cases Daily__
```http
GET /api/v1/dailychange
```

Gets a timeline of the newly confirmed cases for a given county

__Sample response__
```json
  {
    "count": "4977", 
    "name": "Harris", 
    "population": "4,885,616", 
    "timeline": {
      "03-04-2020": 0, 
      "03-05-2020": 0, 
      "03-06-2020": 4, 
      "03-09-2020": 1, 
      "03-10-2020": 0, 
      "03-11-2020": 0, 
      "03-12-2020": 2
    }
  }
```
### Query Parameters




