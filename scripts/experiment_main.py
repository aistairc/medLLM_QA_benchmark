import os
from utils.tools import read_jsonl, answer2jsonl, check_jsonls
from generation.hf_vllm import run_hf


def main(args, in_file, out_dir=):
    questions = read_jsonl(in_file)

    answers, outputs = run_hf(questions, args)
    out_file = os.path.basename(in_file)
    out_file = os.path.join(out_dir, out_file)

    answer2jsonl(answers, outputs, questions[args.few_shots:], out_file)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(allow_abbrev=False)

    parser.add_argument('--in-file', type=str, metavar='N',
                        default='../data/2022/116-A.jsonl', help='input jsonl file')
    parser.add_argument('--out-dir', type=str, metavar='N',
                        default='../baseline_results/', help='baseline results output')
    parser.add_argument('--hf_model_path', type=str, metavar='N',
                        default='', help='hf model path')
    parser.add_argument('--vllm_paralell', default=8, type=int, help='vllm tensor parallel')
    parser.add_argument('--lang', type=str, help='language')
    parser.add_argument('--few_shots', default=5, type=int, help='language')


    args = parser.parse_args()
    print(args)

    main(args, args.in_file, args.out_dir)

