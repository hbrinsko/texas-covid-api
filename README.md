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
**Texas Department of State Health Services**

 https://www.dshs.texas.gov/coronavirus/TexasCOVID19DailyCountyCaseCountData.xlsx 
 https://www.dshs.texas.gov/coronavirus/TexasCOVID19DailyCountyFatalityCountData.xlsx

* Updated Daily. This Excel files contains daily case counts by county, beginning March 4, 2020.
* County-level case counts were not available on March 7, March 8, and March 14.
* Population data is based on Texas population projections, 2020 (https://www.dshs.texas.gov/chs/popdat/st2020.shtm).


https://www.dshs.texas.gov/coronavirus/TexasCOVID-19CumulativeTestsOverTimebyCounty.xlsx


*  Cumulative test totals include tests performed by public labs (Laboratory Response Network) AND non-public labs (commercial labs, hospitals, physician offices, and drive-thru sites) reported electronically and non-electronically. 								
* Test totals do not correlate with county counts of COVID-19 cases reported elsewhere on this DSHS website.								
* Ordering provider county is used when resident county is unavailable.								
* Note: No daily report for tests through 5/5 was produced due to delay in electronic lab reporting (ELR) system								
								
## Endpoint Information

__Query Parameters__

All endpoints have an optional parameter for county name. If no county is provided, it will provide information for all counties. To pull cumulative state totals, use *Total* for the county.

| __Query string parameter__ | __Description__                                                                  | __Type__ |
| -------------------------- | -------------------------------------------------------------------------------- | -------- |
| county                     | Name of county for pulling data. Ex: *Travis* | String   |
| -------------------------- | -------------------------------------------------------------------------------- | -------- |
| range                     | Number of days to pull the data for. Ex: *7* | String   |
| -------------------------- | -------------------------------------------------------------------------------- | -------- |
| type                     | Type of data request, *daily* for daily new cases, *total* for total amount. | String   |
| -------------------------- | -------------------------------------------------------------------------------- | -------- |
| data                     | Dataset requested. *Fatalities* or *Cases* | String   |



__Cases__
```http
GET /api/timeline
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
        "amount": 0,
        "date": "03-04-2020"
      },
      {
        "amount": 0,
        "date": "03-05-2020"
      },
      {
        "amount": 0,
        "date": "03-06-2020"
      },
      {
        "amount": 0,
        "date": "03-09-2020"
      }
    ]
}
```




