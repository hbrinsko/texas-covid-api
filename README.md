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

## Endpoint Information

__Query Parameters__

All endpoints have an optional parameter for county name. If no county is provided, it will provide information for all counties. To pull cumulative state totals, use *Total* for the county.

| __Query string parameter__ | __Description__                                                                  | __Type__ |
| -------------------------- | -------------------------------------------------------------------------------- | -------- |
| county                     | Name of county for pulling data. Ex: *Travis* | String   |



__Latest__

```http
GET /api/latest
```

Gets latest amount of total confirmed cases

Sample Response:
```json
  {
    "cases": 10, 
    "county": "Anderson", 
    "population": 62245
  }
```

__Cases__
```http
GET /api/cases
```
Gets timeline of case count

Sample Response:
```json
{
    "count": 541,
    "county": "Galveston",
    "population": 335006,
    "timeline": [
      {
        "cases": 0,
        "date": "03-04-2020"
      },
      {
        "cases": 0,
        "date": "03-05-2020"
      },
      {
        "cases": 0,
        "date": "03-06-2020"
      },
      {
        "cases": 0,
        "date": "03-09-2020"
      }
    ]
}
```

__New Cases Daily__
```http
GET /api/dailychange
```

Gets a timeline of the newly confirmed cases for a given county

Sample Response:
```json
{
    "count": 541,
    "county": "Galveston",
    "population": 335006,
    "timeline": [
      {
        "cases": 0,
        "date": "03-04-2020"
      },
      {
        "cases": 0,
        "date": "03-05-2020"
      },
      {
        "cases": 0,
        "date": "03-06-2020"
      },
      {
        "cases": 0,
        "date": "03-09-2020"
      }
    ]
}
```




