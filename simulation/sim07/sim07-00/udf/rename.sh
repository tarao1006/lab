#!/bin/sh

for i in `seq 0 9`
do 
	j=`printf %02d $i`
	mv $j 0$j
done
