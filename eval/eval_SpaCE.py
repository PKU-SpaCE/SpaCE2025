# !/usr/bin/env python
# -*- coding:utf-8 -*-
import argparse
import json
import traceback
import numpy as np
import datetime
import os

category_name = {'jsi': '信息正误判断',
                 'rse': '异形同义判断',
                 'rsr': '参照实体判断',
                 'spr-zh': '中文方位推理',
                 'spr-en': '英文方位推理',}

# 计算准确率
def acc_count(category):
    score_record = {}
    task_score = {}
    print('【子任务得分】')
    for k, v in category.items():
        correct, total = v
        name = category_name[k]
        try:
            score = correct / total
        except:
            score = 0
        task_score[k] = score
        score_record[name] = {
        'correct': correct,
        'total': total,
        'accuracy': score,
    }
        print(name+': %d/%d = %f' % (correct, total, score))
    print('-'*35)
    print('【能力得分】')
    lang_capa = np.mean([task_score['jsi'], task_score['rse'], task_score['rsr']])
    reason_capa = np.mean([task_score['spr-zh'], task_score['spr-en']])
    score_record['空间语言能力'] = lang_capa
    score_record['空间推理能力'] = reason_capa
    print('空间语言能力: %f' % (lang_capa))
    print('空间推理能力: %f' % (reason_capa))
    print('-'*35)
    final_score = np.mean([lang_capa, reason_capa])
    score_record['综合得分'] = final_score
    print('【综合得分（排名依据）】%f' % (final_score))
    return score_record


def main(params):
    answers = {}
    with open(params['answer_file'], 'r', encoding='utf-8') as afp:
        for line in afp:
            js = json.loads(line)
            answers[js['id']] = js

    predictions = {}
    with open(params['prediction_file'], 'r', encoding='utf-8') as fin:
        for line in fin:
            js = json.loads(line)
            if ('id' in js):
                predictions[js['id']] = js

    task_category = {task: [0, 0] for task in category_name}
    for qid in answers:
        x = answers[qid]
        name = qid.split('-')
        if name[0] in ['jsi', 'rse', 'rsr']:
            task_category[name[0]][1] += 1
            x_gold = x['answer'].strip()
            if qid in predictions:
                y = predictions[qid]
                y_predict = y['answer'].strip()
                if y_predict not in ['正确', '错误', '相同', '不同']:
                    print(f"{qid}出现非题目要求的字符串!")

        else:
            name[0] += f"-{name[1]}"
            task_category[name[0]][1] += 1
            x_gold = set(g.strip() for g in x['answer'] if g.strip() in ['A', 'B', 'C', 'D'])
            if qid in predictions:
                y = predictions[qid]
                y_predict = set()
                if not isinstance(y['answer'], list):
                    print(f"{qid}答案的数据格式非list，请调整!")
                    continue
                for p in y['answer']:
                    p = p.strip()
                    if p not in ['A', 'B', 'C', 'D']:
                        print(f"{qid}出现非ABCD的字母!")
                    y_predict.add(p)
        if x_gold == y_predict:
            task_category[name[0]][0] += 1

    scores = acc_count(task_category)

    now_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(params['output_dir'], exist_ok=True)
    input_filename = os.path.splitext(os.path.basename(params['prediction_file']))[0]
    output_filename = f"{input_filename}_{now_time}.json"
    output_file_path = os.path.join(params['output_dir'], output_filename)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # data paths
    parser.add_argument('--answer_file', type=str, default='./data/dev_answer.jsonl')  #答案文件
    parser.add_argument('--prediction_file', type=str, default='./prediction/dev_prediction.jsonl')  #预测文件
    parser.add_argument('--output_dir', type=str, default=f'./eval/scores')  #记录分数的文件夹
    args = parser.parse_args()
    params = args.__dict__
    print(params)
    main(params)