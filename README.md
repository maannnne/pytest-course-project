# PyTest Course Project



## How to run me from the main directory :)

- All tests: ```pytest```,
- The tests with a specific mark: ```pytest -m markerName```,
- And generate html reports: ```pytest --html="/tests/reports/result.html"```,
- And generate xml reports: ```pytest --junitxml="/tests/reports/result.xml"```
- Using verbose mode on a specific environment (env is custom) ```pytest --env dev -v```
- See info on skipped/ xfailed/ xpassed tests ```pytest -rxXs```
- See the prints along with test results with verbose mode ```pytest -s -v```
