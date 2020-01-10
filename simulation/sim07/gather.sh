#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

ebicp sim07/udf/00/output.udf
ebicp sim07/udf/01/output.udf
ebicp sim07/udf/02/output.udf
ebicp sim07/udf/03/output.udf
ebicp sim07/udf/04/output.udf
ebicp sim07/udf/05/output.udf
ebicp sim07/udf/06/output.udf
ebicp sim07/udf/07/output.udf
ebicp sim07/udf/08/output.udf
ebicp sim07/udf/09/output.udf
