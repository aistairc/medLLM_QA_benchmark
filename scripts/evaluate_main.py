import argparse, os
import unicodedata
from utils.tools import read_jsonl, answer2jsonl, check_jsonls

def main(pred_file, gold_file):
    preds = read_jsonl(pred_file)
    golds = read_jsonl(gold_file)

    if len(preds) < len(golds):
        golds = golds[-len(preds):]

    check_jsonls(preds, golds)
    results = accuracy(preds, golds)
    print(results)

def accuracy(preds, golds):
    count = 0
    correct = 0
    total = 0
    score = 0
    for pred, ans in zip(preds, golds):
        prediction = pred["prediction"]

        # hankaku KATAKANA to zenkaku KATAKANA
        prediction = unicodedata.normalize('NFKC', prediction)
        #prediction = prediction.replace('､',',')
        prediction = prediction.replace('、',',')
        prediction = prediction.replace('，',',')
        #prediction = sorted(prediction.split(','))
        prediction = sorted([p.strip() for p in prediction.split(',')])

        gold = sorted(ans["answer"])

        #print(prediction, gold)

        points = int(ans["points"])
        if ans["problem_id"] == "116A71":
            correct += 1
            score += points
        elif ans["problem_id"] == "112B30" and (prediction == ["a"] or prediction == ["d"]):
            correct += 1
            score += points
        elif prediction == gold:
            correct += 1
            score += points
        count += 1
        total += points
    return {'accuracy': correct/count * 100, 'score': score, 'total': total}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(allow_abbrev=False)

    parser.add_argument('--pred-file', type=str, metavar='N',
                        default='', help='prediction file')
    parser.add_argument('--gold-file', type=str, metavar='N',
                        default='', help='gold file')
    args = parser.parse_args()
    main(args.pred_file, args.gold_file)
