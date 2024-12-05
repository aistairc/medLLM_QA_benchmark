## medLLM_benchmark
Trilingual medical QA benchmark for English, Japanese, and Chinese.

This repository provides medical QA benchmark datasets for English, Japanese, and Chinese, as well as scripts and Python source files to evaluate LLM.
Most hugging face hub models supported by [vllm](https://docs.vllm.ai/en/latest/) can be evaluated.
The model on the hugging face hub or locally stored checkpoint can be used for evaluation.

### This benchmark is made using the following dataset.

- en (English)　
  - [MedQA](https://arxiv.org/abs/2009.13081)
  - [MedQA-4op](https://arxiv.org/abs/2009.13081)
  - [MMLU](https://arxiv.org/abs/2009.03300)
  - [MedMCQA](https://proceedings.mlr.press/v174/pal22a.html)
  - [PubMedQA](https://doi.org/10.18653/v1/D19-1259)

- ja (Japanese)
  - [IgakuQA](https://arxiv.org/abs/2303.18027)
  - [JJSIMQA](https://arxiv.org/abs/2310.10083)
  - DenQA
  	- It contains the exam problems from the Japan National Dentistry Examination and their answers in the past two years (from 2023 through 2024) extracted from the official website of the Ministry of Health, Labor and Welfare in Japan (https://www.mhlw.go.jp/stf/english/index.html).

- zh (Chinese)
  - [MedQA](https://arxiv.org/abs/2009.13081)
  - [MedQA-4op](https://arxiv.org/abs/2009.13081)
  - [CMExam](https://arxiv.org/abs/2306.03030)

        
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

If you use this benchmark for evaluation, please site the following paper.
```
@article{published_papers/48577159,
title = {ELAINE-medLLM: Lightweight English Japanese Chinese Trilingual Large Language Model for Bio-medical Domain (To appear)},
author = {Ken Yano and Zheheng Luo and Jimin Huang and Qianqian Xie and Masaki Asada and Chenhan Yuan and Kailai Yang and Makoto Miwa and Sophia Ananiadou and Jun'ichi Tsujii},
journal = {The 31st International Conference on Computational Linguistics (COLING 2025)},
month = {1},
year = {2025}
}
```
