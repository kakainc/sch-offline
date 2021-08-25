# coding=utf-8
import argparse
from db import redis_db


def cut_content(data_file):
    # index_redis = redis_db.get_index_redis()
    index_redis = redis_db.get_features_redis()
    with open(data_file, 'r') as file_handler:
        for line in file_handler.readlines():
            info = line.strip().split('\x01')
            if len(info) < 6:
                continue
            pid = info[0]
            top100_reviews = info[5]

            if not top100_reviews:
                continue
            comments = top100_reviews.strip().split('\t')
            key = "new_review"
            index_redis.zadd(key, {pid: -1.0 * len(comments)})
            index_redis.expire(key, 7 * 86400)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')  # 原始数据
    args = parser.parse_args()
    data_file = args.data_file

    cut_content(data_file)
