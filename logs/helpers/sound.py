#!/usr/bin/python
from logs.helpers.iflan_api import post_noise_log
import RPi.GPIO as GPIO
import time

# GPIO SETUP
channel = 17
device_id = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
PAUSE_TIME = 5000 # 5 Seconds


def read_sound():
    GPIO.add_event_detect(channel, GPIO.BOTH, callback=callback, bouncetime=PAUSE_TIME)  # let us know when the pin goes HIGH or LOW
    # GPIO.add_event_callback(channel, callback)

    while True:
        time.sleep(1)


def callback(channel):
    response = post_noise_log(device_id)
    print("Sound Detected! Channel: " + str(channel) + " - Response: " + str(response))
    GPIO.cleanup()
