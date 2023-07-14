#!/usr/bin/env python
# (c) 2015 John Strickler
#
from pprint import pprint
import requests

BASE_URL = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
TOKEN = 'RZvAuJvzafAimtwbJFmORyXQbOpEoVId'

response = requests.get(
    BASE_URL,
    headers = {
        'token': TOKEN,
    },
    params={
        'datasetid': 'PRECIP_HLY',
        'stationid': 'COOP:010957',
        'startdate': '1970-01-01',
        'enddate': '1970-12-31',
    }
)

pprint(response.json())
