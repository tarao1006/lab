#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

array0=(5 6 7 8 9 10)
array1=(0 5 6 7 8 9 10)
for i in ${array0[@]}; do
    for l in ${array1[@]}; do
        j=`printf %03d $i`
        k=`printf %03d $l`
        ebicp sim01/gammadot/$j/B1/$k/output.udf
        ebicp sim01/gammadot/$j/B1/$k/output.txt
    done
done

