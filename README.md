# Accessing Value of Collaboration via FHE and Label-DP
Artifact to accompany: "Practical, Private Assurance of the Value of Collaboration via Fully Homomorphic Encryption".

This artifact includes the source code for achieving the experimental results in the paper, the datasets used, the configuration of the code environment and how to run it.

# Datasets
- Iris(20K), Wine(16K) and Seeds(12K): The datasets are uploaded which are sourced from:
```commandline
Markelle Kelly, Rachel Longjohn, and Kolby Nottingham. 2022. The UCI Machine Learning Repository. https://archive.ics.uci.edu
```
- Abrupto(504K): The datasets can be downloaded from [here](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/5OWRGB), which is named as "mixed_0101_abrupto.tab". When you access the data, please select "Comma Separated Values (Original File Format)". We selected the first 10,000 samples from the dataset for our experiments. The dataset is sourced from:
```commandline
Jesús López Lobo. 2020. Synthetic datasets for concept drift detection purposes. https://doi.org/10.7910/DVN/5OWRGB
```
- Drebin(446M): We don't have the authority to share this dataset. Please contact the authors directly for the access permissions. The dataset is sourced from:
```commandline
Daniel Arp, Michael Spreitzenbarth, Malte Hubner, Hugo Gascon, Konrad Rieck, and CERT Siemens. 2014. Drebin: Effective and explainable detection of android malware in your pocket. In Ndss, Vol. 14. 23–26.
```
- CIFAR-10(177M) and CIFAR-100(177M): The datasets will be automatically downloaded when you run the code. The dataset is sourced from:
```commandline
Alex Krizhevsky et al. 2009. Learning multiple layers of features from tiny images. (2009).
```
- Purchase-10(230M): The dataset is sourced from:
```commandline
Kaggle competition. 2014. Acquire Valued Shoppers Challenge. https://www.kaggle.com/c/acquire-valued-shoppers-challenge/overview
```
# Artifact Appendix

Paper title: **Practical, Private Assurance of the Value of Collaboration via Fully Homomorphic Encryption**

Artifacts HotCRP Id: **#17** (not your paper Id, but the artifacts id)

Requested Badge: **Available**, **Functional**, and **Reproduced**

## Description
The artifact encompasses source code replicating the paper's algorithms, the employed datasets, and the code environment setup. The source code is key to reproducing the experiments including Table 3, 4, 6, 7, 8 and Figure 5, 6.
The environment configuration ensures proper code execution. 

### Security/Privacy Issues and Ethical Concerns (All badges)
Our experiment and datasets have no security/privacy issues or ethical concerns

## Basic Requirements (Only for Functional and Reproduced badges)
### Hardware Requirements
Our device configurations used to complete the experiment are as follows:
- CPU：12th Gen Intel(R) Core(TM) i7-12700 (this project is mainly completed through the CPU).
- Hard Disk: 465G
- RAM: 32G

### Software Requirements
- OS: Linux version 6.5.0-15-generic (x86_64-linux-gnu-gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0
- Software: Python 3.10.14

### Estimated Time and Storage Consumption
- Accuracy of Models 𝑀1 and 𝑀2 against The Holdout Dataset (Table 3)
    - Datasets: Abrupto; Estimated Time: 30 seconds; Storage Consumption: 550KB
- Training time, accuracy and randomized response (Table 4)
    - Dataset: Iris; Estimated Time: 75 minutes; Storage Consumption: 50K
    - Dataset: Seeds; Estimated Time: 100 minutes; Storage Consumption: 50K
    - Dataset: Wine; Estimated Time: 85 minutes; Storage Consumption: 50K
    - Dataset: Abrupto; Estimated Time: 49 hours; Storage Consumption: 550K
    - Dataset: Drebin; Estimated Time: 83 hours; Storage Consumption: 450M
- Ratio of dataset size vs ratio of model accuracy (Figure 5)
    - Dataset: Iris; Estimated Time: 3 minutes; Storage Consumption: 50K
    - Dataset: Seeds; Estimated Time: 3 minutes; Storage Consumption: 50K
    - Dataset: Wine; Estimated Time: 3 minutes; Storage Consumption: 50K
    - Dataset: Abrupto; Estimated Time: 15 minutes; Storage Consumption: 550K
    - Dataset: Drebin; Estimated Time: 230 minutes; Storage Consumption: 450M
    - Dataset: CIFAR-10; Estimated Time: 44 hours; Storage Consumption: 180M
    - Dataset: CIFAR-100; Estimated Time: 45 hours; Storage Consumption: 180M
    - Dataset: Purchase-10; Estimated Time: 45 hours;Storage Consumption: 230M
- Weights and biases of the neural network training from scratch versus neural network from PyTorch (Table 6 * Figrue 6)
    - Dataset: Iris; Estimated Time: 10 seconds; Storage Consumption: 50K
- Weights and biases of models trained on the Iris dataset in plaintext and ciphertext (Table 7)
    - Dataset: Iris; Estimated Time: 1 minute; Storage Consumption: 50K
- Extrapolated training time, accuracy and randomized response (Table 8)
    - Dataset: CIFAR-10; Estimated Time: 483 days; Storage Consumption: 180M
    - Dataset: CIFAR-100; Estimated Time: 5130 days; Storage Consumption: 180M
    - Dataset: Purchase-10; Estimated Time: 1590 days; Storage Consumption: 230M

## Environment
### Accessibility (All badges)
Everyone can access our artifacts via the link below. After the project is downloaded, it can be run directly on the local machine without the need for additional CPUs or GPUs.
[https://github.com/Ryndalf/Label-Encrypted](https://github.com/Ryndalf/Label-Encrypted)

### Set up the environment (Only for Functional and Reproduced badges)
In the experiment, since Zama is required to implement Fully Homomorphic Encryption, the toolkit concrete-numpy is needed. 
Based on the [Zama official website](https://docs.zama.ai/concrete/get-started/installing), the installation of Zama via PyPI and Docker is supported. We have chosen the former (PyPI). Note that, since Conda is a popular management tool for Python, we recommend you set up the environment following the instructions listed in [Using Conda](#instructions_conda). In case you are not a fan of Conda, we also prepare instructions for the non-conda environment in [Not Using Conda](#instructions_non_conda).

#### <a id="instructions_conda"></a> Using Conda
- Step 0: Install conda and Python environment
You can choose the right version of Conda to download from [here](https://repo.anaconda.com/archive/index.html). Install conda via the command below:
```bash
bash downloaded_conda_installer.sh
```
Once installing conda, create a conda environment for Python 3.10.
```bash
conda create -n env_label_encrypted python==3.10.14
conda activate env_label_encrypted
python --version
```
- Step 1: Clone the project, and you will get the fold named "Label-Encrypted".
```bash
git clone https://github.com/Ryndalf/Label-Encrypted.git
```
- Step 2: Install all the Python packages (including concrete-numpy) used in our experiments.
```bash
pip install -r ./Label-Encrypted/source_code/artifiacts/requirements.txt
pip list
```
#### <a id="instructions_non_conda"></a> Not Using Conda
- Step 0: Download and install Python 3.10.14. 
```bash
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
sudo apt install make -y
sudo wget https://www.python.org/ftp/python/3.10.14/Python-3.10.14.tgz
```
After completing the above instructions, you will obtain Python-3.10.14.tgz. You can execute the following instructions to get its location and then enter it.
```bash
find / -name Python-3.10.14.tgz
```
Then following the commands below can help to install Python3.10.14:
```bash
sudo mkdir -p /usr/local/python31014
tar -zvxf Python-3.10.14.tgz 
./Python-3.10.14/configure --prefix=/usr/local/python31014
make
sudo make install
```
Create a soft link and edit the environment variables.
```bash
ln -sf /usr/local/python31014/bin/python3 /usr/bin/python
ln -sf /usr/local/python31014/bin/pip3 /usr/bin/pip
vi ~/.bash_profile
or
vim ~/.bash_profile
```

After the last command is finished, Type "a", and then set the environment variable by entering 
```commandline
export PATH=$PATH:$HOME/bin:/usr/local/python31014
```

Finally, press the [ESC] key, enter ":wq" and then press the Enter key. Then the saving is completed.

- Step 1: Clone the project, and you will get the fold named "Label-Encrypted".
```bash
git clone https://github.com/Ryndalf/Label-Encrypted.git
```
- Step 2: Install the Python packages in file "requirements.txt"
```bash
pip install -r ./Label-Encrypted/source_code/artifiacts/requirements.txt
pip list
```
You will see all the packages installed. If there are different versions of Python on your machine, please ensure that you install the requirements under the Python3.10.14.

### Testing the Environment (Only for Functional and Reproduced badges)
We have prepared the ```envtest.py``` file in the ```testing_env``` folder to test the main packages used. 
If all the packages are installed successfully, the message "All key packages have been installed successfully" will be displayed at the end of the terminal.
```bash
python ./Label-Encrypted/testing_env/envtest.py
```
Note that, you might suffer from an error saying lzma (or liblzma) is missing. In this case, please install lzma manually, following the instructions below.
```bash
sudo apt install liblzma-dev
```

## Artifact Evaluation (Only for Functional and Reproduced badges)
### Main Results and Claims
#### Main Result 1: Model Improvement by Joining Datasets
Augmenting a small and unbalanced dataset with a large and balanced dataset will
increase the accuracy of the resulting model. It refers to Section 6.1 and Table 3 of the paper.
You can reproduce the result from [here](#ex1).
#### Main Result 2: Plaintext vs Ciphertext Versions of the Protocol
The effectiveness of our protocol is mainly proved by comparing the plaintext model and the random response.
It refers to Section 6.4 and Table 4 of the paper.
You can reproduce the result from [here](#ex2).
#### Main Result 3: Ratio of the Number of Samples vs Ratio of Model Accuracy
Show the effect of the size difference between $D_1$ and $D_2$ on the accuracy of the model $M_2$ over all datasets used in our
work. We can conclude that more training data samples result in better training performance.
It refers to Section G and Figrue 5 of the paper.
You can reproduce the result from [here](#ex3).
#### Main Result 4: Neural Network Weights of PyTorch vs Our Implementation
We applied our own model and PyTorch to the same dataset and set the same parameters.
Our model faithfully reproduces the results from PyTorch. We are therefore convinced that our implementation from scratch is an
accurate representation of the model from PyTorch.
It refers to Section H and Table 6 of the paper.
You can reproduce the result from [here](#ex4).
#### Main Result 5: Neural Network Weights of Our Model in Plaintext vs Ciphertext
The homomorphic operations in Zama Concrete will not have any impact on the accuracy of the experiment.
It refers to Section I and Table 7 of the paper.
You can reproduce the result from [here](#ex5).
#### Main Result 6: Plaintext vs Ciphertext Versions of the Protocol with Large Datasets
For large datasets, we obtained the same conclusion as in Experiment 2, which means that our protocol also works for large datasets.
It refers to Section J and Table 8 of the paper.
You can reproduce the result from [here](#ex6).

### Experiments 
Due to the randomness of the experiment, the results obtained cannot be exactly the same as those given in the article. 
However, they are almost the same, which does not affect drawing the same conclusion.
If there are different versions of Python on your machine, please ensure that you run the code under the Python3.10.14.
#### <a id="ex1"></a> Experiment 1:  Accuracy of Models $M_1$ and $M_2$
We set it up so that the dataset used by the M2 model is larger than that of the M1 model.
With these settings, we report the average test accuracy of training
each model 10 times. We expect that the accuracy of M2 will be significantly improved compared to M1, 
so as to prove that augmenting a small and unbalanced dataset with a large and balanced dataset will
increase the accuracy of the resulting model.

After running the following commands, you can find the saved results ```table_3_single_test.txt```in the directory of ```./source_code/others/```.
```bash
python ./Label-Encrypted/source_code/SingleTestM1AndM2.py
```
Estimated Time: 30 seconds; Storage Consumption: 550KB

#### <a id="ex2"></a> Experiment 2: Training time, accuracy in clear model, our protocol and randomized response
We set multiple ```$\epsilon$```  values of for each dataset in our experiments and report the accuracy and time. 
We expect to find a reasonable range that can not only protect the datasets but also provide the value of the datasets effectively.

Initially, we need to pre-calculate the sensitivity list (T list) and the corresponding differential privacy (DP) noise, which will be used in the following experiment. 
The results, including the running time of the T list, are saved in the "TListDPNoise" file. 
Since Zama cannot return the ciphertext alone, our computation time includes both the encryption and decryption processes.
```bash
python ./Label-Encrypted/source_code/CalculateTList.py dataset_name epsilon
```
```dataset_name``` should be replaced by "iris", "seeds", "wine", "abrupto" or "drebin".
```epsilon``` here should be replaced by 0.1, 1, 10 or 100. Other ```epsilon``` can refer to Table 4 in the paper.
For example
```bash
python ./Label-Encrypted/source_code/CalculateTList.py seeds 1
```
Next, we compared different models with different epsilon values. 
The results can be found in the ```res``` folder.
```bash
python ./Label-Encrypted/source_code/MainExperiment.py dataset_name epsilon
```
```epsilon``` here should be replaced by 0.1, 1, 10 or 100. Other ```epsilon``` can refer to Table 4 in the paper.
For example:
```bash
python ./Label-Encrypted/source_code/MainExperiment.py seeds 1
```
Finally, we also perform experiments of randomized response with the same ```epsilon```.
The results are saved as ```xx_random.txt``` in the "res" folder.
```bash
python ./Label-Encrypted/source_code/RandomRespond.py --dataset dataset_name --epsilon epsilon
```
For example:
```bash
python ./Label-Encrypted/source_code/RandomRespond.py --dataset iris --epsilon 0.1
```

- Estimated Time and Storage Consumption for each ```epsilon```
  - Dataset: Iris; Estimated Time: 75 minutes; Storage Consumption: 50K
  - Dataset: Seeds; Estimated Time: 100 minutes; Storage Consumption: 50K
  - Dataset: Wine; Estimated Time: 85 minutes; Storage Consumption: 50K
  - Dataset: Abrupto; Estimated Time: 49 hours; Storage Consumption: 550K
  - Dataset: Drebin; Estimated Time: 83 hours; Storage Consumption: 450M

#### <a id="ex3"></a> Experiment 3: Ratio of Dataset Size vs Ratio of Model Accuracy.
We set $M_1$ is trained on $D_1$, and $M_2$ is trained on $D_1 \cup D_2$.
We adjusted the sizes of the two datasets, increasing the size ratio of the two datasets from 0.1 all the way up to 1 (when the two datasets are of the same size).
```bash
python ./Label-Encrypted/source_code/MultiTestM1AndM2.py dataset_name
```
```dataset_name``` here can be replaced by all 8 datasets. For example:
```bash
python ./Label-Encrypted/source_code/MultiTestM1AndM2.py iris
```
After running all the datasets, the results will be saved in the "multiTest" folder. We can also plot the results via:
```bash
python ./Label-Encrypted/source_code/PlotMultiTestM1AndM2.py
```
**Note: Before proceeding to the plotting stage, we need to run all the datasets in this section.**
- Estimated Time and Storage Consumption
    - Dataset: Iris; Estimated Time: 3 minutes; Storage Consumption: 50K
    - Dataset: Seeds; Estimated Time: 3 minutes; Storage Consumption: 50K
    - Dataset: Wine; Estimated Time: 3 minutes; Storage Consumption: 50K
    - Dataset: Abrupto; Estimated Time: 15 minutes; Storage Consumption: 550K
    - Dataset: Drebin; Estimated Time: 230 minutes; Storage Consumption: 450M
    - Dataset: CIFAR-10; Estimated Time: 44 hours; Storage Consumption: 180M
    - Dataset: CIFAR-100; Estimated Time: 45 hours; Storage Consumption: 180M
    - Dataset: Purchase-10; Estimated Time: 45 hours;Storage Consumption: 230M

#### <a id="ex4"></a> Experiment 4: Neural Network Weights of PyTorch vs Our Implementation
We applied our own model and PyTorch to the same dataset and set the same parameters.
We expect to obtain the same weights and biases as those of the PyTorch model.
Run the command below, you can find the following files in the "others" folder,
- figure_6_np_roc.png
- figure_6_torch_roc.png
- from_scratch_weights.txt
- torch_weights.txt
```bash
python ./Label-Encrypted/source_code/PyTorchFromScratch.py
```
Estimated Time: 10 seconds; Storage Consumption: 50K

#### <a id="ex5"></a> Experiment 5: Neural Network Weights of Our Model in Plaintext vs Ciphertext
We used two networks, one without encryption and the other with homomorphic operations, 
and applied them to the same dataset to observe their network weights and biases.
We expect them to be exactly the same.
Run the command below, you can find the following files in the "others" folder:
- table_7_ciphertext.txt
- table_7_plaintext.txt
```bash
python ./Label-Encrypted/source_code/PlaintextCiphertext.py
```
Estimated Time: 1 minute; Storage Consumption: 50K

#### <a id="ex6"></a> Experiment 6: Extrapolated training time, accuracy in clear model, our protocol and randomized response
All the processes were exactly the same as those in Experiment 2. The differences lay in the datasets and the range of epsilon. 
The datasets used here were "cifar10", "cifar100", and "purchase10". 
And the values of epsilon were 1, 10, 100, and 1000.
- Estimated Time and Storage Consumption
    - Dataset: CIFAR-10; Estimated Time: 483 days; Storage Consumption: 180M
    - Dataset: CIFAR-100; Estimated Time: 5130 days; Storage Consumption: 180M
    - Dataset: Purchase-10; Estimated Time: 1590 days; Storage Consumption: 230M

## Limitations (Only for Functional and Reproduced badges)
We are unable to provide the datasets "Drebin" due to authorization issues.

## Notes on Reusability (Only for Functional and Reproduced badges)
We are the first work to explore an efficient way to securely share data between two parties under a semi-honest setting.
Researcher could take our work as a benchmark when proposing improved methods.

## License
All code in this repository is licensed under MIT license.

## Temporary Settings for Artifact 
To conveniently test the experiments, you can adjust the epoch and sampling ratio for Experiments 2, 3 and 6.
Before running the program, first run the following .sh file to adjust the parameters.
- Experiment 2:
```bash
bash exp2.sh epoch1 ratio1 epoch2 ratio2
```
The epoch1 and ratio1 are the parameters for CalculateTList.py; The epoch2 and ratio2 are the parameters for MainExperiment.py.

Note: epoch1 $\geq$ epoch2; ratio1 $\geq$ ratio2

For example:
```bash
bash exp2.sh 2 0.2 1 0.1
```

- Experiment 6:
Except for the executable file exp6.sh, everything else is the same as in Experiment 2.
For example:
```bash
bash exp6.sh 2 0.2 1 0.1
```

- Experiment 3:
```bash
bash exp3.sh avg_round ratio
```
The two parameters are for MultiTestM1AndM2.py. 
The avg_round represents the number of times the loop runs to calculate the average; the ratio represents sampling ratio.
For example:
```bash
bash exp3.sh 10 0.1 
```
