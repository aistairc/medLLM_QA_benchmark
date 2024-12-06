## medLLM_QA_benchmark
Trilingual medical QA benchmark for English, Japanese, and Chinese.

This repository is made to evaluate [ELAINE-medLLM](https://huggingface.co/kenyano/Llama3-ELAINE-medLLM-8B), [ELAINE-medLLM-instruct](https://huggingface.co/kenyano/Llama3-ELAINE-medLLM-instruct-8B), a lightweight English-Japanese-Chinese trilingual large language model for the Biomedical Domain.
It contains a wide range of medical QA benchmarks for three languages and provides scripts and Python source files for evaluating LLM.
The evaluation method uses a consistent language-dependent input format to evaluate medical LLM on all benchmarks.
Any LLM models supported by [vllm](https://docs.vllm.ai/en/latest/) can be evaluated.
We have checked those models on the hugging face hub, but a locally stored checkpoint can also be used for evaluation.

### This benchmark set is made using the following dataset.

Please abide by the original license for each benchmark.
MedQA(MIT),MMLU(MIT),MedMCQA(MIT),PubMedQA (MIT), CMExam(Apach-2.0), JJISMQA(cc-by-nc-sa-4.00).

If the original QA benchmark contains splits for training, validation, and testing, we used only the testing split.

- en (English)　
  - [MedQA](https://arxiv.org/abs/2009.13081) (./data/en/MedQA/medqa_en.jsonl)
  - [MedQA-4op](https://arxiv.org/abs/2009.13081) (./data/en/MedQA-4op/medqa_en_4op.jsonl)
  - [MMLU](https://arxiv.org/abs/2009.03300)  (./data/en/MMLU/mmluen_en_medical.jsonl)
  - [MedMCQA](https://proceedings.mlr.press/v174/pal22a.html)  (./data/en/MedMCQA/medmcqa.jsonl)
  - [PubMedQA](https://doi.org/10.18653/v1/D19-1259)  (./data/en/PubMedQA/pubmedqa.jsonl)

- ja (Japanese)
  - [IgakuQA](https://github.com/jungokasai/IgakuQA) (./data/ja/IgakuQA/igakuqa.jsonl)
  	- We concatenate the original exam data from 2018 to 2022 into a single JSON file.
  - [JJSIMQA](https://arxiv.org/abs/2310.10083) (./data/ja/JJSIMQA/jjsimqa.jsonl)
  - DenQA (./data/ja/DenQA/denqa.jsonl)
  	- It contains the exam problems from the Japan National Dentistry Examination and their answers in the past two years (from 2023 through 2024) extracted from the official website of the Ministry of Health, Labor and Welfare in Japan (https://www.mhlw.go.jp/stf/english/index.html).

- zh (Chinese)
  - [MedQA](https://arxiv.org/abs/2009.13081) (./data/zh/MedQA/medqa_zh.jsonl)
  - [MedQA-4op](https://arxiv.org/abs/2009.13081) (./data/zh/MedQA-4op/medqa_zh_4op.jsonl)
  - [CMExam](https://arxiv.org/abs/2306.03030) (./data/zh/CMExam/cmexam.jsonl)

        
### How to evaluate the medical LLMs using this benchmark

### <ins>Interactive evaluation</ins>

#### Test a single benchmark with a model
```
Usage: sh scripts/experiment.sh json_test_file model_name_or_path output_dir language few_shots
	json_test_file:		file path to the input JSON file
	model_name_or_path:	model name or path
	output_dir:	root dir for results
	lang:	the language of the benchmark
	few_shots:	number of shots for in-context learning
``` 

#### Evaluate a single result with a gold answer
```
Usage: sh scripts/evaluate.sh pred_file answer_file
	pred_file:	file path to the JSON file generated under the output_dir
	answer_file:	file path to the input JSON file used for evaluation 
```

### <ins>Batch mode evaluation</ins>

#### Test all benchmarks with multiple LLM models

To change the LLM models to be used for the experiment, manually edit the script
**scripts/experiment_batch.sh**

The following snippet shows how to add the LLM model named 'xxxx/yyyy' to experiments.
If you'd like to remove a LLM model from evaluation, comment out the model declaration.

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

### Convert the evaluation result log to a CSV file
Using the following script, you can convert the evaluation log to a compact CSV file.
```
sh scripts/evaluate_batch.sh output_dir > log
cat log | grep @@ > results.csv
```

### Remark
If you use this medical QA benchmark for evaluation, I ask that you please cite the following paper.
```
@article{published_papers/48577159,
title = {ELAINE-medLLM: Lightweight English Japanese Chinese Trilingual Large Language Model for Bio-medical Domain (To appear)},
author = {Ken Yano and Zheheng Luo and Jimin Huang and Qianqian Xie and Masaki Asada and Chenhan Yuan and Kailai Yang and Makoto Miwa and Sophia Ananiadou and Jun'ichi Tsujii},
journal = {The 31st International Conference on Computational Linguistics (COLING 2025)},
month = {1},
year = {2025}
}
```
