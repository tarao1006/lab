#!/bin/sh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

for i in `seq 0 25`; do
    j=`printf %03d $i`
    ebicp sim11/$j/output.udf
    ebicp sim11/$j/output.txt
done