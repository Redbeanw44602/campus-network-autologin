import sys

from requests import Response

def __assert__(cond: bool, msg: str = None):
    if cond:
        return
    if msg:
        print(msg)
    sys.exit(-1)


def __check_object__(object: object):
    __assert__(object, 'Object is empty.')


def __check_response__(response: Response):
    __check_object__(response)
    __assert__(
        response.status_code == 200,
        f'The server response status code is abnormal. ({response.status_code} != 200)',
    )


def __purecall__():
    __assert__(False, 'Pure virtual function called.')
