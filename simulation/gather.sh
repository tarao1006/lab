#!/bin/sh

for i in `seq 1 32`
do
	j=`printf %02d $i`
	tail -n 10 udf/$j/output.txt | head -n 1 >> all_data.txt 
done
