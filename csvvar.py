#Imports
import os
import gzip
import glob
import os.path
import pandas as pd
import numpy as np


#iterations
total_count = 0
iteration = 0
row_cursor = 0
column_cursor = 0
DF_End_Flag = 0
prior_value = 0
later_value = 0
nano_freq = 0
freq_list = []
list_var = 0
list_avg = 0
samp_list = []
freq_var = 0
rows = 0
a = 0

#directory of the files
dest_dir = "/home/fred/Desktop/g"


#number of files in directory
file_count = len(os.listdir(dest_dir))


#Create DataFrames by looping through csv files
for file_name in glob.glob(os.path.join(dest_dir, '*.csv')):
	df = pd.read_csv(file_name,dtype='int64')
	iteration = iteration + 1



	#Determine Basic File Info
	columns = len(df.columns)
	rows = len(df.index)


	#Print Basic File Info
	print('\n\nFile',iteration,'/',file_count,': ',file_name[21:])
	print('Column Count:', columns,' Row Count:', rows) 
		
	while row_cursor <= rows-2:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		#print(nano_freq)
		freq_list.insert(0 , nano_freq)

	row_cursor = 0
	freq_var = (np.var(freq_list))
	print('Freq Var:',freq_var)
	freq_list = []
