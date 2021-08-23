# coding=utf-8
import argparse
from db import mongo_db


def cut_content(data_file):
    post_mg = mongo_db.get_col_post()
    isn = 0
    udn = 0
    with open(data_file, 'r') as file_handler:
        for line in file_handler.readlines():
            info = line.strip().split('\x01')
            pid = info[0]
            ptype = info[1]
            tid = info[2]
            content = info[3]
            tname = info[4]
            top100_reviews = info[5]

            postdoc = {"_id": pid, "ptype": ptype, "tid": tid, "tname": tname,
                       "content": content, "top100_reviews": top100_reviews}
            dup = post_mg.find_one({"_id": pid})
            if not dup:
                post_mg.insert_one(postdoc)
                isn += 1
            else:
                query = {"_id": pid}                                                    # $set $inc $gt $gte
                newvalues = {"$set": {"ptype": ptype, "tid": tid, "tname": tname,
                                      "content": content, "top100_reviews": top100_reviews}}

                post_mg.update_one(query, newvalues)
                udn += 1
    print(isn, udn)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')  # 原始数据
    args = parser.parse_args()
    data_file = args.data_file

    cut_content(data_file)
