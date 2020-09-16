from config.settings import *
import requests


def post_tmp_hum_log(tmp, hum):
    url = settings.API_URL + "/tmp_hum_logs"
    params = {"tmp_hum_log": {"temperature": tmp, "humidity": hum}}
    r = requests.post(url, json=params)
    return r.status_code


def post_noise_log(device_id):
    url = settings.API_URL + "/noise_logs"
    params = {"noise_log": {"device_id": device_id}}
    r = requests.post(url, json=params)
    return r.status_code
