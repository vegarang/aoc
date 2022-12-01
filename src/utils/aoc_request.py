import os

import requests

from src.utils.Logger import Logger


def fetch_aoc_content(url, log_lvl):
    logger = Logger(log_lvl=log_lvl)
    session = os.getenv('AOC_SESSION', None)
    if session is None:
        raise Exception('Cannot fetch data without AOC_SESSION in .env')
    cookies = {
        'session': session
    }
    logger.debug(f'Reading from {url} with session: {session}')
    return requests.get(url, cookies=cookies)
