#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

for i in `seq 1 32`
do 
        j=`printf %02d $i`
        ebicp sim04/sim04-01/udf/$j/output.udf
done
