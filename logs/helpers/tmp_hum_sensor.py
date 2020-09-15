from logs.helpers.iflan_api import post_tmp_hum_log
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
DELAY = 10  # Seconds


def post_tmp_hum(tmp, hum):
    if hum is not None or tmp is not None:
        post_tmp_hum_log(tmp, hum)
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(tmp, hum))
        print(tmp)
        print(hum)
    else:
        print("Failed to retrieve data from humidity sensor")


while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    post_tmp_hum(temperature, humidity)
    time.sleep(DELAY)
