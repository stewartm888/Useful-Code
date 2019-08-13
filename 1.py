#Imports
import os
import gzip
import glob
import os.path
import pandas as pd
import numpy as np

#Increment counters
total_count = 0
deleted_count = 0
iteration = 0
total_nulls = 0

#directory of the files
dest_dir = "/home/fred/Desktop/g"

#number of files being measursed
file_count = len(os.listdir(dest_dir))


#Create DataFrames of remaining .csv files
for file_name in glob.glob(os.path.join(dest_dir, '*.csv')):
	df = pd.read_csv(file_name)

#file count
	iteration = iteration +1
	print(iteration,'/',file_count)

#file name
	print('\n',file_name)

#Null count
	print('Nulls in file:', df.isnull().sum().sum())
	total_nulls = total_nulls + df.isnull().sum().sum()
	print('Total nulls so far:', total_nulls)


