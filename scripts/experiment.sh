#!/bin/bash

set -u
set -e

if [ $# -ne 5 ]; then
    echo "illegal number of parameters"
    echo "Usage: $0 json_test_file model_name_or_path output_dir language few_shots"
    echo "\tjson_test_file:\t\tpath for input jsonl test"
    echo "\tmodel_name_or_path:\tmodel name or path"
    echo "\toutput_dir language:\troot dir for results"
    echo "\tlang:\tlanguage of the test file"
    echo "\tfew_shots:\tnumber of shots for in context learning"
    exit 0
fi

TEST_JSONL=$1
MODEL_NAME_OR_PATH=$2
OUT_DIR=$3
LANG=$4
FEW_SHOTS=$5

# set the number of GPU fro vllm to use
GPU_NUM=1

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ROOT=$SCRIPT_DIR/..
PYTHONPATH=$ROOT/scripts

output_sub_dir=${MODEL_NAME_OR_PATH/\//_}
benchmark=$(basename $(dirname $TEST_JSONL))
lang=$(basename $(dirname $(dirname $TEST_JSONL)))

OUTPUT_DIR=$OUT_DIR/$output_sub_dir/$lang/$benchmark

if [ ! -d $OUTPUT_DIR ];then
    mkdir -p $OUTPUT_DIR
fi


echo "python ./scripts/experiment_main.py --in-file $TEST_JSONL --hf_model_path $MODEL_NAME_OR_PATH --out-dir $OUTPUT_DIR --vllm_paralell $GPU_NUM --lang $LANG --few_shots $FEW_SHOTS"

python ./scripts/experiment_main.py --in-file $TEST_JSONL --hf_model_path $MODEL_NAME_OR_PATH --out-dir $OUTPUT_DIR --vllm_paralell $GPU_NUM --lang $LANG --few_shots $FEW_SHOTS

