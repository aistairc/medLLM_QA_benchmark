#!/bin/bash

set -u
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ROOT=$SCRIPT_DIR/..
PYTHONPATH=$ROOT/scripts

if [ $# -ne 2 ]; then
    echo "illegal number of parameters"
    echo "Usage: $0 pred_file answer_file"
    echo "\tpred_file:\tpath for the jsonl file for prediction"
    echo "\tanswer_file:\tpath for the jsonl file for answer"
    exit 0
fi

PRED_FILE=$1
GOLD_FILE=$2

echo "python ./scripts/evaluate_main.py --gold-file $GOLD_FILE --pred-file $PRED_FILE"
python ./scripts/evaluate_main.py --gold-file $GOLD_FILE --pred-file $PRED_FILE

