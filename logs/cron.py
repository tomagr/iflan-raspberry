from logs.helpers.tmp_hum_log_api import post_tmp_hum_log


def send_tmp_hum():
    post_tmp_hum_log(13.3, 24.6)