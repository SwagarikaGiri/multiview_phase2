from sklearn.utils import shuffle
import pandas as pd
import csv
import math
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



input_file='iris_last_label.txt'
dataset = pd.read_csv(input_file,sep=",",header=None)
csv_list = dataset.iloc[0:,0:].values
rand_csv = shuffle(csv_list, random_state=0)

