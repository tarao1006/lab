#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

for i in `seq 0 9`
do 
        j=`printf %02d $i`
        # ebicp sim09/sim09-00/udf/$j/output.udf
        # ebicp sim10/sim10-00/udf/$j/output.udf
        # ebicp sim10/sim10-01/udf/$j/output.udf
        # ebicp sim11/sim11-00/udf/$j/output.udf
        ebicp sim09/sim09-00/udf/$j/torque_sum.txt
        # ebicp sim10/sim10-00/udf/$j/torque_sum.txt
        # ebicp sim10/sim10-01/udf/$j/torque_sum.txt
        # ebicp sim11/sim11-00/udf/$j/torque_sum.txt
done
