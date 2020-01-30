#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

for i in `seq 3 4`; do
    for l in `seq 0 5 100`; do
        j=`printf %02d $i`
        k=`printf %03d $l`
        ebicp sim03/$j/udf/$k/output.udf
        ebicp sim03/$j/udf/$k/output.txt
    done
done

