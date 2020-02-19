#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

for i in `seq 0 3`; do
    for l in `seq 100 5 150`; do
        j=`printf %02d $i`
        k=`printf %03d $l`
        # cp ../sim04/$j/udf/$k/input.udf $j/udf/$k/
        # cp ../sim04/$j/udf/$k/define.udf $j/udf/$k/
        cp -r ../sim04/$j/udf/$k $j/udf/
    done
done

