# coding=utf-8
import redis

INDEX_REDIS_HOST = '127.0.0.1'
INDEX_REDIS_PORT = 6379
INDEX_REDIS_AUTH = ''

REDIS_RECFEARES_HOST = ''
REDIS_RECFEARES_PORT = 6379
REDIS_RECFEARES_PASSWD = ''


def get_redis(host, port, db=0, password=''):
    pool = redis.ConnectionPool(host=host, port=port, db=db, password=password)
    redis_conn = redis.StrictRedis(connection_pool=pool)
    return redis_conn


def get_index_redis():
    return get_redis(INDEX_REDIS_HOST, INDEX_REDIS_PORT, 0, INDEX_REDIS_AUTH)


def get_features_redis():
    return get_redis(REDIS_RECFEARES_HOST, REDIS_RECFEARES_PORT, password=REDIS_RECFEARES_PASSWD)


if __name__ == "__main__":

    # index_redis = get_index_redis()
    index_redis = get_features_redis()

    # key = '内容_' + 'p图'
    # key = '评论_' + 'p图'
    # key = '话题_' + '浙江'
    # key = "new_review"
    # name = "new_ctr"

    # print(index_redis.zrange(key, 0, 5, withscores=True))
    # print index_redis.hget(name, "100643854")
