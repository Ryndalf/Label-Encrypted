#!/bin/bash

file="./source_code/MultiTestM1AndM2.py"

avg_range=$1
new_ratio=$2

sed -i '139s/.*/        for i in tqdm.tqdm(range('"$avg_range"')):/' "$file"

sed -i '84s/.*/    sample_ratio = '"$new_ratio"'/' "$file"
