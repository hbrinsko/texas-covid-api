<h1 align="center">
    Texas Coronavirus Tracker API
</h1>

## Setting up the Python Application
Provides up-to-date data about Coronavirus outbreak in Texas.

Assuming that before you begin, you will have [Python](http://www.python.org/) and [pip](http://www.pip-installer.org/en/latest/) installed on your system and available at the command line.

Install depenedencies:

```bash
pip install -r requirements.txt
```
## Data Source
**Texas Department of State Health Services** - https://www.dshs.texas.gov/coronavirus/TexasCOVID19DailyCountyCaseCountData.xlsx - 
* Updated Daily. This Excel files contains daily case counts by county, beginning March 4, 2020.
* County-level case counts were not available on March 7, March 8, and March 14.
* Population data is based on Texas population projections, 2020 (https://www.dshs.texas.gov/chs/popdat/st2020.shtm).

## Endpoints

### Latest Endpoint

Getting latest amount of total confirmed cases

```http
GET /api/v1/latest
```

__Query String Parameters__
| __Query string parameter__ | __Description__                                                                  | __Type__ |
| -------------------------- | -------------------------------------------------------------------------------- | -------- |
| county                     | Name of county for pulling data. Ex: *Travis* | String   |

__Sample response__
```json
  {
    "count": "10", 
    "name": "Anderson", 
    "population": "62,245"
  }
```

### Case Count Endpoint

Getting timeline of case count

```http
GET /api/v1/cases
```

__Query String Parameters__
| __Query string parameter__ | __Description__                                                                  | __Type__ |
| -------------------------- | -------------------------------------------------------------------------------- | -------- |
| county                     | Name of county for pulling data. Ex: *Travis* | String   |

__Sample response__
```json
  {
    "count": "27", 
    "name": "Angelina", 
    "population": "94,245", 
    "timeline": {
      "03-04-2020": 0, 
      "03-05-2020": 0, 
      "03-06-2020": 0, 
      "03-09-2020": 0
      }
  }
```
### Daily Change Endpoint

Gets a timeline of the newly confirmed cases for a given county

```http
GET /api/v1/dailychange
```

__Query String Parameters__
| __Query string parameter__ | __Description__                                                                  | __Type__ |
| -------------------------- | -------------------------------------------------------------------------------- | -------- |
| county                     | Name of county for pulling data. Ex: *Travis* | String   |

__Sample response__
```json
  {
    "count": "27", 
    "name": "Angelina", 
    "population": "94,245", 
    "timeline": {
      "03-04-2020": 0, 
      "03-05-2020": 0, 
      "03-06-2020": 0, 
      "03-09-2020": 0
      }
  }
```
