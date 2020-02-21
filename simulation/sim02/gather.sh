#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

for i in `seq 6 6`; do
    for l in `seq 1 32`; do
        j=`printf %02d $i`
        k=`printf %02d $l`
        ebicp sim02/$j/udf/$k/output.udf
        ebicp sim02/$j/udf/$k/output.txt
    done
done

