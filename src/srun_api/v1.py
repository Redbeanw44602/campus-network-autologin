import json

from util.network import get


def srun_protal_detect():
    response = get('/v1/srun_portal_detect')
    return json.loads(response)
