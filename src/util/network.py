import requests
import json

from urllib.parse import urlparse, urlunparse, urlencode, parse_qsl

import config

from util.internal import __check_response__
from util.system import get_millisecond_timestamp

JSONP_DEFAULT_NAME = 'jQuery_114514_1919810'

def add_query_param(url, param_name, param_value):
    url_parts = list(urlparse(url))
    query = dict(parse_qsl(url_parts[4]))
    query[param_name] = param_value
    url_parts[4] = urlencode(query)
    return urlunparse(url_parts)

def get(filename, enable_auto_jsonp = False, enable_auto_timestamp = False) -> str:
    url = config.SRUN_BASE_URL + filename
    if enable_auto_jsonp:
        url = add_query_param(url, 'callback', JSONP_DEFAULT_NAME)
    if enable_auto_timestamp:
        url = add_query_param(url, '_', get_millisecond_timestamp())
    response = requests.get(url, timeout=config.REQUESTS_TIMEOUT)
    __check_response__(response)
    if enable_auto_jsonp:
        return response.content.removeprefix(f'{JSONP_DEFAULT_NAME}(').removesuffix(')')
    return response.content

# def post(filename):
#     pass
