#!/bin/bash

wpa_cli_event.py $2

case "$2" in
    CONNECTED)
        echo "WPA supplicant: connection established";
        ;;
    DISCONNECTED)
        echo "WPA supplicant: connection lost";
        ;;
esac
