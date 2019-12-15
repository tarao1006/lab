mkdir udf
for i in `seq 0 10 360`
do 
	j=`printf %03d $i`
	mkdir ./udf/$j
	cp /home/katarao/Projects/dontuse/strage/sim00/udf/004/$j/output.udf ./udf/$j
	cp /home/katarao/Projects/dontuse/strage/sim00/udf/004/$j/input.udf ./udf/$j
	cp /home/katarao/Projects/dontuse/strage/sim00/udf/004/$j/define.udf ./udf/$j
	cp /home/katarao/Projects/dontuse/strage/sim00/stdout/004/$j/output.txt ./udf/$j
done
