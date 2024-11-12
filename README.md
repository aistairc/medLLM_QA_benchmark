## medLLM_benchmark
Benchmark for medical LLM for English, Japanese, and Chinese.

This repository provides medical QA benchmark datasets for English, Japanese, and Chinese, with scripts and Python source files to evaluate LLM.
Most models supported by vllm[https://docs.vllm.ai/en/latest/] can be evaluated.

### This benchmark is made using the following dataset.

- en
  - MedQA
  - MedQA-4op
  - MMLU
  - MedMCQA
  - PubMedQA

- ja
  - IgakuQA
  - JJSIMQA
  - DenQA

- zh
  - MedQA
  - MedQA-4op
  - CMExam

        
### How to evaluate the model using this benchmark

### Interactive evaluation

#### Test a single benchmark with a model
```
Usage: sh scripts/experiment.sh json_test_file model_name_or_path output_dir language few_shots
	json_test_file:		path for input jsonl test
	model_name_or_path:	model name or path
	output_dir language:	root dir for results
	lang:	the language of the test file
	few_shots:	number of shots for in-context learning
``` 

#### Evaluate a single result with a gold answer
```
Usage: sh scripts/evaluate.sh pred_file answer_file
	pred_file:	path for the JSONL file for prediction
	answer_file:	path for the JSONL file for the answer
```

### Batch mode evaluation
#### Test all benchmarks with multiple models

To change the models to be used for the experiment, manually edit the script
**scripts/experiment_batch.sh**

The following snippet shows how to add the model named 'xxxx/yyyy' to experiments.

```
hf_model_path=xxxx/yyyyy
model_path+=($hf_model_path)
```

The following script runs an experiment for all models for each one of the benchmark datasets.

```
Usage: sh scripts/experiment_batch.sh output_dir few_shots
	output_dir:	root dir for results
	few_shots:	number of shots for in-context learning
```
#### Evaluate all results with gold answers
```
Usage: sh scripts/evaluate_batch.sh output_dir
	output_dir:	root dir for results
```


