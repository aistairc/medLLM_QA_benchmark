import string, mojimoji
import string, time
import numpy as np
from utils.tools import check_jsonls
from vllm.distributed.parallel_state import destroy_model_parallel, destroy_distributed_environment
from vllm import LLM, SamplingParams
import torch
from tqdm import tqdm
import re
import gc

import pdb


def run_hf(questions, args):

    llm = LLM(model=args.hf_model_path,
            trust_remote_code=True,
            tensor_parallel_size=args.vllm_paralell,
            dtype="half",
            max_model_len=None)
            #max_model_len=8192)

    n_few_shots = args.few_shots
    prompt = questions[:n_few_shots]
    questions = questions[n_few_shots:]

    preds = []
    outputs = []
    for q_idx in tqdm(range(len(questions))):
        question = questions[q_idx]
        hf_input = create_input(prompt, question, args.lang)
        done = False
        nb_trials = 0
        while not done:
            try:
                explanation, answer = hf_problem(hf_input, llm)
                done = True
            except:
                print('\nfailed')
                nb_trials += 1
            if nb_trials == 3:
                explanation = 'NA'
                answer = 'NA'
                break
        preds.append(answer)
        outputs.append(explanation)


    destroy_model_parallel()
    del llm
    gc.collect()
    torch.cuda.empty_cache()
    torch.distributed.destroy_process_group()
    print("Successfully delete the llm pipeline and free the GPU memory!")

    return preds, outputs

def create_input(prompt, question, lang):

    messages = []
    for example in prompt:
        messages.extend(dict2problem(example, lang, True))
    messages.extend(dict2problem(question, lang, False))
    messages = '\n'.join(messages)

    # for test
    messages += '\n'

    return messages


def dict2problem(dict_input, lang, demo):

    if lang.lower() == 'ja':
        return dict2problem_JA(dict_input, demo)
    elif lang.lower() == 'en':
        return dict2problem_EN(dict_input, demo)
    elif lang.lower() == 'zh':
        return dict2problem_ZH(dict_input, demo)
    else:
        print('unknow param', lang)
        exit(1)


def dict2problem_JA(dict_input, demo=True):

    problem = "問題: " + dict_input['problem_text']
    choices = dict_input['choices']
    answer = dict_input['answer']
    if len(choices) > 0:
        for choice, label in zip(choices, string.ascii_lowercase):
            problem = problem + '\n' + label + ': ' + choice
        problem = problem + "\n必ずa,b,c,d,eの中からちょうど{}個選んでください。".format(len(answer))
        problem = problem + "\n答え:"
    output = [problem]
    if not demo:
        return output
    output.append(",".join(answer))
    return output


def dict2problem_EN(dict_input, demo=True):

    problem = "Question: " + dict_input['problem_text']
    choices = dict_input['choices']
    answer = dict_input['answer']
    if len(choices) > 0:
        for choice, label in zip(choices, string.ascii_lowercase):
            problem = problem + '\n' + label + ': ' + choice
        problem = problem + "\nBe sure to choose exactly {} from a, b, c, d, e.".format(len(answer))
        problem = problem + "\nAnswer:"
    output = [problem]
    if not demo:
        return output
    output.append(",".join(answer))
    return output

def dict2problem_ZH(dict_input, demo=True):

    problem = "问题: " + dict_input['problem_text']
    choices = dict_input['choices']
    answer = dict_input['answer']
    if len(choices) > 0:
        for choice, label in zip(choices, string.ascii_lowercase):
            problem = problem + '\n' + label + ': ' + choice
        problem = problem + "\n请确保从 a、b、c、d、e 中准确选择 {}。".format(len(answer))
        problem = problem + "\n答话:"
    output = [problem]
    if not demo:
        return output
    output.append(",".join(answer))
    return output


def hf_problem(messages, llm):

    #sampling_params = SamplingParams(temperature=0.0, top_p=0.95)
    sampling_params = SamplingParams(temperature=0.0, top_p=0.8)
    output = llm.generate(messages,sampling_params)


    prompt = output[0].prompt
    answer = output[0].outputs[0].text

    # todo #############
    ans_lines = answer.split('\n')
    t = ''
    for t in ans_lines:
        if len(t) != 0:
            break


    m = re.search(r'(.+?)\:?',t)
    if m:
        answer = m.group(1)
    else:
        answer = 'NA'
    

    pred = mojimoji.zen_to_han(answer).lower()


    return answer, pred


