#!/bin/sh

for i in `seq 1 2`
do
    j=`printf %02d $i`
    # rm $SIM_DIR/sim01/udf/$j/job.sh
    # scp ebi:/home/katarao/Projects/lab/simulation/sim01/udf/$j/output.txt $SIM_DIR/sim01/udf/$j/
    # scp lab:/Users/taiga/Projects/lab/simulation/sim01/udf/$j/output.txt $SIM_DIR/sim01/udf/$j/
    scp ebi:/homge/katarao/Projects/lab/simulation/sim02/udf/$j/output.txt lab:/Users/taiga/Projects/lab/simulation/sim02/udf/$j/
done
