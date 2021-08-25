# coding=utf-8
import pymongo

DB_POST_HOST = '127.0.0.1'
DB_POST_PORT = 27017
DB_POST = 'newpost'

DB_POST_DATA = 'postinfo'
DB_HOT_POST_DATA = 'hotpost'


def get_col_post():
    c = pymongo.MongoClient(DB_POST_HOST, DB_POST_PORT)
    db = c.get_database(DB_POST)
    col = db.get_collection(DB_POST_DATA)
    return col


def get_hot_post():
    c = pymongo.MongoClient(DB_POST_HOST, DB_POST_PORT)
    db = c.get_database(DB_POST)
    col = db.get_collection(DB_HOT_POST_DATA)
    return col


if __name__ == "__main__":
    post_mg = get_col_post()
    postdoc = {"_id": 1, "ptype": 2, "tid": 3, "content": "mongo_test", "tname": "three",
               "top100_reviews": [{"rev1": "test1", "rev2": "test2"}]}

    # obj = post_mg.insert_one(postdoc)
    # print(obj.inserted_id)

    # dup = post_mg.find_one({"_id": "233399776"})
    # print(not dup)

    # query = {"_id": 1}
    # newvalues = {"$set": {"tname": "III", "top100_reviews": "update test"}}
    # post_mg.update_one(query, newvalues)
