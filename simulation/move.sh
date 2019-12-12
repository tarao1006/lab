#!/bin/sh

for i in `seq 1 32`
do
    j=`printf %02d $i`
    scp ebi:/home/katarao/Projects/lab/simulation/sim00/udf/$j/output.txt $SIM_DIR/sim00/udf/$j/
done