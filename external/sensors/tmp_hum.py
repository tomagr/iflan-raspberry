from api.api import post_tmp_hum_log
from config.settings import Settings
from logs.logger import Log
import Adafruit_DHT
import time

DELAY = 120  # Seconds
DHT_SENSOR = Adafruit_DHT.DHT22


def get_tmp_hum():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, Settings.DHT_PIN)
        tmp = round(temperature, 2)
        hum = round(humidity, 2)
        read_tmp_hum(tmp, hum)
        time.sleep(DELAY)


def read_tmp_hum(tmp, hum):
    if hum is not None or tmp is not None:
        response = post_tmp_hum_log(tmp, hum)
        message = "Response: " + str(response) + " - Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(tmp, hum)
        Log.write(message)
    else:
        Log.write("Failed to retrieve data from humidity sensor")
