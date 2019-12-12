#!/bin/sh

for i in `seq 1 32`
do
    j=`printf %02d $i`
    # rm $SIM_DIR/sim01/udf/$j/job.sh
    scp ebi:/home/katarao/Projects/lab/simulation/sim01/udf/$j/output.txt $SIM_DIR/sim01/udf/$j/
done
