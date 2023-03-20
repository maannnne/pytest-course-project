# PyTest Course Project



## How to run me from the main directory :)

- Run the tests with a specific mark, on a specific environment (env is custom): ```pytest -m markerName --env envName```

## Additionally ... 

- Generate html reports: ```--html="/tests/reports/result.html"```,
- Generate xml reports: ```--junitxml="/tests/reports/result.xml"```
- Use verbose mode on a specific environment (env is custom) ```--env dev -v```
- See info on skipped/ xfailed/ xpassed tests ```-rxXs```
- See the prints along with test results with verbose mode ```-s -v```
