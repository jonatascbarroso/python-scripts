# [Python Scripts](https://github.com/jonatascbarroso/python-scripts/)

## [Performance Test](https://github.com/jonatascbarroso/python-scripts/tree/master/performance-test)

This script is used to perform load, stress and performance tests on an API.

The result is saved to the `log.txt` file.

```
$ performance-test.py -h

usage: performance-test.py [-h] [-u URL] [-r REQUESTS] [-w WORKERS]

Perform load, stress and performance tests on an API.

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to be called. Default: http://localhost
  -r REQUESTS, --requests REQUESTS
                        How many requests will be made. Default: 1
  -w WORKERS, --workers WORKERS
                        How many works will act. Default: 1
```

```
$ performance-test.py -u http://localhost:8080 -r 3 -w 2

---------------
Starting requests...
2019-10-03 08:41:32.386676
Processing 1 of 3
Processing 2 of 3
Request 1 OK: Hello World!
Request 2 OK: Hello World!
Processing 3 of 3
Request 3 OK: Hello World!
---------------
Final Report
---------------
Start time: 2019-10-03 08:41:32.386676
URL: http://localhost:8080
Requests: 3
Workers: 2
Total time: 0:00:00.252866
Mean time: 0:00:00.084289
Error requests: 0
Error rate: 0.00%
```
