#!/usr/bin/python
from logs.helpers.iflan_api import post_noise_log
import RPi.GPIO as GPIO
import time

# GPIO SETUP
channel = 17
device_id = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def read_sound():
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, callback)
    while True:
        time.sleep(1)


def callback(channel):
    if GPIO.input(channel):
        post_noise_log(device_id)
        print("Sound Detected! Channel:" + str(channel))
    else:
        print("No sound? Channel:" + str(channel))
