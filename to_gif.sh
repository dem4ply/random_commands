ffmpeg -i $1 -ss $2 -to $3 -c:v libvpx -c:a libvorbis -crf 4 -b:v 1500K -vf scale=720:-1 -threads 4 -an output.webm
