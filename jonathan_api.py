from multiprocessing.dummy import Pool
from requests import Session, codes
from functools import partial

URL = 'https://www.usgs.gov/api'
USERNAME = 'jonathan'
PASSWORD = 'l0lz'

TIME_VALUES = ['a', 'b', 'c']

def get_time_series(session, time_value):
    session.get(URL, params={'tv': time_value}, timeout=30)

pool = Pool(32)

with Session() as session:
    session.params.update({'user': USERNAME, 'password': PASSWORD})
    get_ts = partial(get_time_series, session)
    results = pool.map(get_ts, TIME_VALUES)

