from sklearn.utils import shuffle
import pandas as pd
import csv
import math
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA





def randomize_dataset(input_file,output_file):
	dataset = pd.read_csv(input_file,sep=",",header=None)
	# csv_list = dataset.iloc[0:,0:].values
	# rand_csv = shuffle(csv_list, random_state=0)
	# row,col=rand_csv.shape
	rand_csv = dataset.iloc[0:,0:].values
	row,col=rand_csv.shape
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=',')
		for i in range(0,row):
			col1=[]
			for j in range(0,col-1):
				col1.append(rand_csv[i,j])
			print len(col1)
			spamwriter.writerow(col1)


randomize_dataset('iris_last_label_randomized.txt','iris_randomized.txt')

