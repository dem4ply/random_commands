#!/bin/sh
arecord -d 5 /tmp/test-mic.wav
aplay /tmp/test-mic.wav
