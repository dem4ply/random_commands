# resolucion, display from xrandr despues del + es un offset
ffmpeg -f x11grab -s 1920x1080  -i :0.0+1300,200 /tmp/test.mkv
