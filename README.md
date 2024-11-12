## medLLM_benchmark
Benchmark for medical LLM for English, Japanese, and Chinese.
We provide scripts and Python source files to evaluate the model using this benchmark.
This tool can evaluate models that are supported by vllm[https://docs.vllm.ai/en/latest/].

### The benchmark is made using the following dataset.

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
Usage: scripts/experiment.sh json_test_file model_name_or_path output_dir language few_shots
	json_test_file:		path for input jsonl test
	model_name_or_path:	model name or path
	output_dir language:	root dir for results
	lang:	language of the test file
	few_shots:	number of shots for in context learning
``` 

#### Evaluate a single result with a gold answer
```
Usage: scripts/evaluate.sh pred_file answer_file
	pred_file:	path for the jsonl file for prediction
	answer_file:	path for the jsonl file for answer
```

### Batch mode evaluation
#### Test all benchmarks with multiple models
```
Usage: scripts/experiment_batch.sh output_dir few_shots
	output_dir:	root dir for results
	few_shots:	number of shots for in context learning
```
#### Evaluate all results with gold answers
```
Usage: scripts/evaluate_batch.sh output_dir
	output_dir:	root dir for results
```


