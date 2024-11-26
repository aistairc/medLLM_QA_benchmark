#!/bin/bash

set -u
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ROOT=$SCRIPT_DIR/..


if [ $# -ne 2 ]; then
    echo "illegal number of parameters"
    echo "Usage: $0 output_dir few_shots"
    echo "\toutput_dir:\troot dir for results"
    echo "\tfew_shots:\tnumber of shots for in context learning"
    exit 0
fi

OUT_DIR=$1
FEW_SHOTS=$2

# declar models for experiments
model_path=()

#Llama3
hf_model_path=meta-llama/Meta-Llama-3-8B-Instruct
model_path+=($hf_model_path)

hf_model_path=meta-llama/Meta-Llama-3-8B
model_path+=($hf_model_path)


#Llama2
hf_model_path=meta-llama/Llama-2-7b-hf
model_path+=($hf_model_path)

hf_model_path=meta-llama/Llama-2-7b-chat-hf
model_path+=($hf_model_path)

# google gemma
f_model_path=google/gemma-7b
model_path+=($hf_model_path)

f_model_path=google/gemma-7b-it
model_path+=($hf_model_path)

# Meditron
hf_model_path=epfl-llm/meditron-7b
model_path+=($hf_model_path)


# llama3-swalow
hf_model_path=tokyotech-llm/Llama-3-Swallow-8B-v0.1
model_path+=($hf_model_path)

# llama3-swalow-sft
hf_model_path=tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1
model_path+=($hf_model_path)


hf_model_path=aaditya/Llama3-OpenBioLLM-8B
model_path+=($hf_model_path)

hf_model_path=Flmc/DISC-MedLLM
model_path+=($hf_model_path)

hf_model_path=Henrychur/MMed-Llama-3-8B
model_path+=($hf_model_path)

hf_model_path=medalpaca/medalpaca-7b
model_path+=($hf_model_path)

hf_model_path=FreedomIntelligence/Apollo-7B
model_path+=($hf_model_path)

#hf_model_path=kenyano/ELAINE-medLLM
#model_path+=($hf_model_path)

#hf_model_path=kenyano/ELAINE-medLLM-instruct
#model_path+=($hf_model_path)

infiles=`find $ROOT/data -type f -name \*jsonl`


for mpath in "${model_path[@]}"; do
    for infile in $infiles; do
        dir=$(dirname $(dirname $infile))
        lang=$(basename $dir)
   
        echo "start experiment"
        echo "model_name: $mpath"
        echo "input file: $infile"
        echo "language: $lang"
    
        # experiment.sh json_test_file model_name_or_path output_dir language few_shots
        echo "sh $SCRIPT_DIR/experiment.sh $infile $mpath $OUT_DIR $lang $FEW_SHOTS"
        bash $SCRIPT_DIR/experiment.sh $infile $mpath $OUT_DIR $lang $FEW_SHOTS
        echo "done"
    done
done

