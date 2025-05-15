import zipfile
import os
import numpy as np
import pandas as pd
import random
import argparse
from tqdm import tqdm
"""
数据集构成
"""

csv_path = "sha256_family.csv"
zip_path = "feature_vectors.zip"

malicious_df = pd.read_csv(csv_path)
malicious_set = set(malicious_df['sha256'].tolist())
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    all_file_names = [os.path.basename(name) for name in zip_ref.namelist() if not name.endswith('/')]
malicious_files = [f for f in all_file_names if f in malicious_set]
benign_files = [f for f in all_file_names if f not in malicious_set]
random.seed(42)
benign_sampled = random.sample(benign_files, 11120)
files_to_load = malicious_files + benign_sampled

samples = []

valid_prefixes = ['api_call', 'call', 'feature', 'intent', 'permission', 'provider', 'real_permission']
vocab_set = set()
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    for file_name in tqdm(zip_ref.namelist()):
        if file_name.endswith('/'):
            continue
        base_name = os.path.basename(file_name)
        if base_name in files_to_load:
            with zip_ref.open(file_name) as f:
                lines = f.read().decode('utf-8').splitlines()
                samples.append(lines)
                for line in lines:
                    if any(line.startswith(prefix + '::') for prefix in valid_prefixes):
                        vocab_set.add(line.strip())

vocab_list = sorted(list(vocab_set))
vocab_index = {item: i for i, item in enumerate(vocab_list)}  # item -> index
num_samples = len(files_to_load)
num_features = len(vocab_list)
X = np.zeros((num_samples, num_features), dtype=np.uint8)
for i, sample in tqdm(enumerate(samples)):
    for feat in sample:
        feat = feat.strip()
        if feat in vocab_index:
            X[i, vocab_index[feat]] = 1
print('The drebin is saved in Label-Encrypted/data/drebin/vec.npy')
np.save('vec.npy', X)

