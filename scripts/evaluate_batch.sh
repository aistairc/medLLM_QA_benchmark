#!/bin/bash

set -u
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ROOT=$SCRIPT_DIR/..

if [ $# -ne 1 ]; then
    echo "illegal number of parameters"
    echo "Usage: $0 output_dir"
    echo "\toutput_dir:\troot dir for results"
    exit 0
fi

OUT_DIR=$1

pred_files=`find $OUT_DIR -type f -name \*jsonl | sort`


for predfile in $pred_files; do
    fname=$(basename $predfile)
    benchmark=$(basename $(dirname $predfile))
    lang=$(basename $(dirname $(dirname $predfile)))
    goldfile=$ROOT/data/$lang/$benchmark/$fname

    echo "evaluate start"
    echo "pred_file: $predfile"
    echo "gold_file: $goldfile"
    # sh evaluate.sh pred_file answer_file"
    echo "sh evaluate.sh $predfile $goldfile"
    sh evaluate.sh $predfile $goldfile
    echo "done"

done

