#!/usr/bin/python
from logs.helpers.iflan_api import post_noise_log
import RPi.GPIO as GPIO
import time

# GPIO SETUP
channel = 17
device_id = 1


def read_sound():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

    while True:
        time.sleep(1)


def callback(channel):
    if GPIO.input(channel):
        post_noise_log(device_id)
        print("Sound Detected! Channel:" + channel)
    else:
        print("Sound Detected! Channel:" + channel)
