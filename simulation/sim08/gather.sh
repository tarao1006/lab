#!/bin/sh

for i in `seq 0 10 360`
do
	j=`printf %03d $i`
	tail -n 10 udf/$j/output.txt | head -n 1 >> test.txt
done
