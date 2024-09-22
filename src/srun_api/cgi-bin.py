import json

from util.network import get
from util.system import get_timestamp


def rad_user_info():
    response = get('/cgi-bin/rad_user_info', enable_auto_jsonp=True, enable_auto_timestamp=True)
    return json.loads(response)


def rad_user_dm(ip: str, username: str, unbind: bool, sign: str):
    response = get(
        f'/cgi-bin/rad_user_dm?ip={ip}&username={username}&time={get_timestamp()}&unbind={int(unbind)}&sign={sign}',
        enable_auto_jsonp=True,
        enable_auto_timestamp=True,
    )
    return json.loads(response)


def srun_portal(
    action: str,
    username: str,
    password: str,
    os: str,
    name: str,
    double_stack: int,
    checksum: str,
    info: str,
    ac_id: int,
    ip: str,
    n: int,
    type: int,
):
    response = get(
        f'/cgi-bin/srun_portal?action={action}&username={username}&password={password}&os={os}&name={name}&double_stack={double_stack}&chksum={checksum}&info={info}&ac_id={ac_id}&ip={ip}&n={n}&type={type}'
    )
    return json.loads(response)


def get_challenge(username: str, ip: str):
    response = get(f'/cgi-bin/get_challenge?username={username}&ip={ip}')
    return json.loads(response)
