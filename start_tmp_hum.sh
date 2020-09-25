#!/bin/bash

# Start serial
cd /home/pi/iflan-raspberry/startup_scripts
python3 init_sound.py &
python3 init_tmp_hum.py &
