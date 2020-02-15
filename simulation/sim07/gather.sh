#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

for i in `seq 0 0`; do
    for l in `seq 0 5 100`; do
        j=`printf %02d $i`
        k=`printf %03d $l`
        ebicp sim07/$j/udf/$k/output.udf
        ebicp sim07/$j/udf/$k/output.txt
    done
done

