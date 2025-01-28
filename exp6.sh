#!/bin/bash

file1="./source_code/CalculateTList.py"
file2="./source_code/MainExperiment.py"
cal_new_epoch=$1
cal_new_ratio=$2
main_new_epoch=$3
main_new_ratio=$4

sed -i '385s/.*/        epoch = '"$cal_new_epoch"'/' "$file1"
sed -i '428s/.*/    sample_ratio = '"$cal_new_ratio"'/' "$file1"

sed -i '67s/.*/        epoch = '"$main_new_epoch"'/' "$file2"
sed -i '76s/.*/    sample_ratio = '"$main_new_ratio"'/' "$file2"
