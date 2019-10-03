'''
This script is used to perform load, stress and performance tests on an API.
'''

import asyncio
import concurrent.futures
import requests
import json
import os
from datetime import datetime
from time import sleep


def print_line(size=15):
    print(size * '-')


def log(msg):
    print(msg)
    with open('log.txt', 'a+') as file:
        file.write(f'{msg}\n')


def error(i, code, text):
    global errors
    msg = str(f'Request {i} - Error {code} - {text}')
    log(msg)
    errors += 1


def request(i):
    print(f'Processing {i+1} of {requestsNumber}')
    try:
        response = requests.get(url=url)
        response_status_code = response.status_code
        response_text = response.text
        response.close()
        if response is not None:
            if response_status_code != requests.codes.ok:
                error(i + 1, response_status_code, response_text)
            else:
                msg = str(f'Request {i+1} OK: {response_text}')
                log(msg)
                return response_text
        else:
            error(i + 1, 0, 'Null response')
    except requests.exceptions.RequestException as e:
        error(i + 1, 0, e)
    return None


async def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                request, # executed function
                i # param
            )
            for i in range(requestsNumber)
        ]
        for response in await asyncio.gather(*futures):
            pass


# Questions
url = input('What is the URL (http address)? ')
requestsNumber = int(input('How many requests? '))
workers = int(input('How many workers? '))

errors = 0

print_line()

print('Starting requests...')
startTime = datetime.now()
log(str(startTime))
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
endTime = datetime.now()

print_line()

# Report information
totalTime = endTime - startTime
meanTime = totalTime / requestsNumber
errorRate = (errors / requestsNumber) * 100

print('Final Report')
print_line()

print(f'Start time: {startTime}')
print(f'URL: {url}')
print(f'Requests: {requestsNumber}')
print(f'Total time: {totalTime}')
print(f'Mean time: {meanTime}')
print(f'Error requests: {errors}')
print(f'Error rate: {errorRate:.2f}%')
