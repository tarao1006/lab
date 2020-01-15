#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

for i in `seq 0 9`
do 
        j=`printf %02d $i`
        ebicp sim12/sim12-00/udf/$j/output.udf
done
