#!/bin/bash
nohup cvlc -q -vvv alsa://plughw:1 --gain 8.0 --sout '#transcode{acodec=mp3,ab=64,channels=1}:standard{access=http,dst=0.0.0.0:8888/audio.mp3}'  2> /dev/null &
