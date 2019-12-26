#!/bin/sh

for i in `seq 100`
do
	num=`printf "%03d" $i`
	convert $num.jpg -crop 460x460+727+100 _$num.jpg
done
ffmpeg -f image2 -r 15 -i _%03d.jpg -r 15 -an -vcodec libx264 -pix_fmt yuv420p video.mp4