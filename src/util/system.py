import time


def get_timestamp():
    return int(time.time())


def get_millisecond_timestamp():
    return get_timestamp() * 1000
