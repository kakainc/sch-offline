# coding=utf-8
import argparse
from db import redis_db


def cut_content(data_file):
    # index_redis = redis_db.get_index_redis()
    index_redis = redis_db.get_features_redis()
    ctr_dic = {}
    with open(data_file, 'r') as file_handler:
        for line in file_handler:
            info = line.strip().split('\t')
            if len(info) != 16:
                continue
            pid = info[14]
            click = info[15]

            ctr_dic.setdefault(str(pid), [0, 0])
            if click == '1':
                ctr_dic[str(pid)][0] += 1
            ctr_dic[str(pid)][1] += 1
    print("ctr_dic have got, begin update!!!")

    for key, value in ctr_dic.items():
        name = "new_ctr"
        if value[0] > 0:
            index_redis.hset(name, key, float(value[0])/value[1])
            index_redis.expire(name, 7 * 86400)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')  # 原始数据
    args = parser.parse_args()
    data_file = args.data_file

    cut_content(data_file)
