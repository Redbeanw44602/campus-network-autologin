import json

from util.network import get


def srun_portal_message():
    response = get('/v2/srun_portal_message')
    return json.loads(response)
