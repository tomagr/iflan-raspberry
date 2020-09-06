import requests


def post_tmp_hum_log(tmp, hum):
    # url = "http://localhost:3000/1/tmp_hum_logs"
    url = "http://api.iflan.house/1/tmp_hum_logs"
    params = {"tmp_hum_log": {"temperature": tmp, "humidity": hum}}
    r = requests.post(url, json=params)
    return r.status_code
