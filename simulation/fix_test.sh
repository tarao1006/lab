for i in `seq 17 23`
do
	j=`printf %02d $i`
	scp ebi:/home/katarao/Projects/lab/simulation/sim$j/udf/32/output.udf /Users/taiga/Projects/lab/simulation/sim$j/udf/32/output.udf
done
