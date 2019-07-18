#!/bin/bash
# This turns on xscreensaver using xwinwrap on one (or both) screens

#SCREENCOUNT=$(xrandr -q | grep " connected " | grep -v " connected (" |  wc -l)
killall xwinwrap
SCREENS=$( xrandr -q | grep " connected " | awk '{ print $3 }' )
SCREENS=$SCREENS | tr " " "\n"

find ~/video/anime_60fps/ -type f >  /tmp/wallpaper_viedeo_playlist.txt
#(xwinwrap -g 1920x1080+0 -ni -fs -o 1 -s -st -sp -b -nf -- mplayer -wid WID -quiet -loop 0 -ao null -shuffle <((find ~/Videos/anime -type f)) ) &
#(xwinwrap -g 1366x768+1000 -ni -fs -o 1 -s -st -sp -b -nf -- mplayer -wid WID -quiet -loop 0 -ao null -shuffle <((find ~/Videos/anime -type f)) ) &
#( xwinwrap -ni -fs -o 1 -s -st -sp -b -nf -- mplayer -wid WID -quiet -loop 0 -ao null -shuffle -playlist /tmp/wallpaper_viedeo_playlist.txt ) &
#sleep 1

( xwinwrap -g 1366x768-1200 -ni -fs -o 1 -s -st -sp -b -nf -- mplayer -wid WID -quiet -loop 0 -ao null -shuffle -playlist /tmp/wallpaper_viedeo_playlist.txt ) &

#youtube-dl -f bestvideo[ext!=webm]+bestaudio[ext!=webm]/best[ext!=webm]  https://www.youtube.com/playlist?list=PLxCJsNWDGPvUwollYS7EbGLYdpAxp_u0g
