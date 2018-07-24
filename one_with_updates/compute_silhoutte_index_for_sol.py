import pandas as pd
import csv
import math
from sklearn.metrics import silhouette_score
from scipy import sparse
import numpy as np
from scipy.spatial.distance import pdist, euclidean

def compute_label(label_file):
	dataset = pd.read_csv(label_file,sep=" ",header=None)
	csv_list = dataset.iloc[1:,0:].values
	label=[]
	for i in range(0,2545):
		label.append(int(csv_list[i,3]))
	return label

data_file='microarray_2545_17.txt'
dataset= pd.read_csv(data_file,sep=" ",header=None)
microarray= dataset.iloc[0:,0:].values
output_file='silhoutte_ee.txt'

with open(output_file,'w') as outputcsv_file:
	spamwriter = csv.writer(outputcsv_file,delimiter=' ')
	for i in range (1,13):
		col1=[]
		solution_name="view_ee_clus"+str(i)+"_multiview"
		label=compute_label(solution_name)
		score = silhouette_score(microarray, label)
		col1.append(solution_name)
		col1.append(score)
		spamwriter.writerow(col1)
