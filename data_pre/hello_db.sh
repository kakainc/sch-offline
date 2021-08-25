#!/usr/bin/env bash

export PYTHONPATH=../:../../
pythonenv3="/usr/local/bin/python3"

start_unix=`date +%s`
echo "update_post_data"

${pythonenv3} post_info_mongo.py '../datas/raw_data/search_demp_test_case.csv'
echo "update post info done"

${pythonenv3} post_ctr_redis.py '../datas/raw_data/search_demp_test_case.csv'
echo "update post ctr done"

${pythonenv3} post_review_redis.py '../datas/raw_data/search_demo_test_case.csv'
echo "update post reviews done"
end_post_unix=`date +%s`
spent_time_post=$(($end_post_unix - $start_unix))
echo "update post total spend time: ${spent_time_post}"

echo "update invdics"
start_inv_unix=`date +%s`

${pythonenv3} inv_content_redis.py '../datas/raw_data/search_demo_test_case.csv' '../datas/phase_py.txt' '../datas/stopword.txt'
end_unix1=`date +%s`
spent_time1=$(($end_unix1 - $start_inv_unix))
echo "content cut done, spend time: ${spent_time1}!!!"

${pythonenv3} inv_comment_redis.py '../datas/raw_data/search_demo_test_case.csv' '../datas/phase_py.txt' '../datas/stopword.txt'
end_unix2=`date +%s`
spent_time2=$(($end_unix2 - $end_unix1))
echo "comment cut done, spend time: ${spent_time2}!!!"

${pythonenv3} inv_tname_redis.py '../datas/raw_data/search_demo_test_case.csv' '../datas/phase_py.txt' '../datas/stopword.txt'
end_unix3=`date +%s`
spent_time3=$(($end_unix3 - $end_unix2))
echo "tname cut done, spend time: ${spent_time3}!!!"

spent_time_inv=$(($end_unix3 - $start_inv_unix))
echo "update invdics total spend time: ${spent_time_inv}"

spent_time=$(($end_unix3 - $start_unix))
echo "all done! total spend time: ${spent_time}"

