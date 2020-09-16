from api.api import post_noise_log
from config.settings import Settings
import RPi.GPIO as GPIO
import time

# GPIO SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(Settings.CHANNEL, GPIO.IN)
PAUSE_TIME_MIL = 5000  # 5 Seconds
PAUSE_TIME_SEG = 5


def read_sound():
    GPIO.add_event_detect(
        Settings.CHANNEL,
        GPIO.BOTH,
        callback=callback,
        bouncetime=PAUSE_TIME_MIL
    )  # let us know when the pin goes HIGH or LOW
    # GPIO.add_event_callback(channel, callback)

    while True:
        time.sleep(PAUSE_TIME_SEG)


def callback():
    response = post_noise_log(Settings.DEVICE_ID)
    print("Sound Detected! Channel: " + str(Settings.CHANNEL) + " - Response: " + str(response))
    # GPIO.cleanup()
