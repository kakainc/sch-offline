# coding=utf-8

import argparse
import jieba           # jieba.load_userdict(phase_file)
import jieba.analyse as analyse
from db import redis_db
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def cut_content(data_file, phase_file, stpwd_file):
    # index_redis = redis_db.get_index_redis()
    index_redis = redis_db.get_features_redis()
    anys = analyse
    anys.set_stop_words(stpwd_file)
    # phase = pd.read_table(phase_file, header=None)
    phase = pd.read_csv(phase_file, sep='\t', header=None)
    for i in phase.index.tolist():
        temp = phase.loc[i, 0]
        jieba.add_word(temp.lower(), tag='ng')
    print("segment loading done!!!")
    with open(data_file, 'r') as file_handler:
        for line in file_handler:
            info = line.strip().split('\x01')
            pid = info[0]
            content = info[3]
            content = content.lower()
            keywords_tf = anys.extract_tags(content, withWeight=True)
            for item in keywords_tf:
                key = "内容_"+item[0]
                index_redis.zadd(key, {pid: -1.0 * float(item[1])})
                index_redis.expire(key, 7 * 86400)

    print("cut done!!!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')  # 原始数据
    parser.add_argument('phase_file')
    parser.add_argument('stpwd_file')
    args = parser.parse_args()
    data_file = args.data_file
    phase_file = args.phase_file
    stpwd_file = args.stpwd_file

    cut_content(data_file, phase_file, stpwd_file)
