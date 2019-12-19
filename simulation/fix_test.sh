for i in `seq 17 23`
do
	j=`printf %02d $i`
	tail ./sim$j/udf/32/output.udf
done
