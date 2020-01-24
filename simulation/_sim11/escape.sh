for i in `seq 0 25`
do
	j=`printf %03d $i`
	mkdir $j
	cp ../sim11/$j/input.udf $j
	cp ../sim11/$j/output.udf $j
	cp ../sim11/$j/output.txt $j
done
