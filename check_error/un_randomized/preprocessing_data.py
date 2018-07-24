import pandas as pd
import csv
import math
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#we will find the distance between them
def calculate_sym(item1,item2):
	val=0
	for i in range(0,len(item1)):
		val=((item1[i]-item2[i])**2)+val
	return round(math.sqrt(val),7)


def create_symmetry_matrix(input_file,output_file):
	dataset = pd.read_csv(input_file,sep=",",header=None)
	csv_list = dataset.iloc[0:,0:].values
	row,col=csv_list.shape
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=' ')
		for i in range(0,row):
			col1=[]
			for j in range (0,row):
				item1=csv_list[i,0:]
				item2=csv_list[j,0:]
				result=calculate_sym(item1,item2)
				res_str=str(result)
				col1.append(res_str)
			print len(col1)
			spamwriter.writerow(col1)
def create_symmetry_matrix_pca(input_file,output_file):
	dataset = pd.read_csv(input_file,sep=",",header=None)
	csv_list = dataset.iloc[0:,0:].values
	csv_list = StandardScaler().fit_transform(csv_list)
	pca = PCA(n_components=5)
	csv_list_pca = pca.fit_transform(csv_list)
	row,col=csv_list_pca.shape
	print str(row)+" "+str(col)
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=' ')
		for i in range(0,row):
			col1=[]
			for j in range (0,row):
				item1=csv_list_pca[i,0:]
				item2=csv_list_pca[j,0:]
				result=calculate_sym(item1,item2)
				res_str=str(result)
				col1.append(res_str)
			print len(col1)
			spamwriter.writerow(col1)

create_symmetry_matrix_pca('wine.txt','wine_dist_pca.txt')



