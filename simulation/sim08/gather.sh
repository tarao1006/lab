#!/bin/zsh

function ebicp() {
        scp ebi:/home/katarao/Projects/lab/simulation/$1 $SIM_DIR/$1
}

ebicp sim08/udf/00/output.udf
ebicp sim08/udf/01/output.udf
ebicp sim08/udf/02/output.udf
ebicp sim08/udf/03/output.udf
ebicp sim08/udf/04/output.udf
ebicp sim08/udf/05/output.udf
ebicp sim08/udf/06/output.udf
ebicp sim08/udf/07/output.udf
ebicp sim08/udf/08/output.udf
ebicp sim08/udf/09/output.udf
