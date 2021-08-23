#!/usr/bin/env bash

today=`date +%Y%m%d`
max_day=1
data_dir="../datas/raw_data/"

if [ ! -d ${data_dir} ];then
  mkdir ${data_dir}
fi

count=`ls ${data_dir} | wc -w`
if [ "$count" -gt "0" ]; then
  find ${data_dir} -name "*data_post*" -type f -mtime +${max_day} -exec rm {} \;
fi

version=$(date "+%h")
data_file=${data_dir}"/data_post_${version}.csv"


if [ ! -f ${data_file} ];then
  echo "start update post & invdic !"
  bash -x hello_db.sh
  echo "end update"
fi

