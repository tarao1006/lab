#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

ebicp ./sim01/sim01-02/udf/000/output.udf
ebicp ./sim01/sim01-02/udf/005/output.udf
ebicp ./sim01/sim01-02/udf/006/output.udf
ebicp ./sim01/sim01-02/udf/007/output.udf
ebicp ./sim01/sim01-02/udf/008/output.udf
ebicp ./sim01/sim01-02/udf/009/output.udf
ebicp ./sim01/sim01-02/udf/010/output.udf
