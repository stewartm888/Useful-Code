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


#directory of the files
dest_dir = "/home/fred/Desktop/g"


#number of files in directory
file_count = len(os.listdir(dest_dir))


#Create DataFrames by looping through csv files
for file_name in glob.glob(os.path.join(dest_dir, '*.csv')):
	df = pd.read_csv(file_name)


#Determine Basic File Info
	iteration = iteration + 1
	columns = len(df.columns)
	rows = len(df.index)
	prior_value = df.iloc[row_cursor,column_cursor]


#Print Basic File Info
	print('\n\nFile',iteration,'/',file_count,': ',file_name[21:])
	print('Column Count:', columns,' Row Count:', rows) 
#	print('First Timestamp:',prior_value)


#Iterate rows
	while row_cursor <= 5000:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	list_avg = np.average(freq_list)
	print('Timestamp (1) Variance:', list_var, '  Avg:',list_avg)
	
	row_cursor = 20000
	freq_list = []
	while row_cursor <= 25000:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	list_avg = np.average(freq_list)
	print('Timestamp (2) Variance:', list_var, '  Avg:',list_avg)

	row_cursor = 50000
	freq_list = []
	while row_cursor <= 55000:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	list_avg = np.average(freq_list)
	print('Timestamp (3) Variance:', list_var, '  Avg:',list_avg)

	row_cursor = 80000
	freq_list = []
	while row_cursor <= 85000:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	list_avg = np.average(freq_list)
	print('Timestamp (4) Variance:', list_var, '  Avg:',list_avg)


	row_cursor = 0
	freq_list = []
	while row_cursor <= (rows-2):
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	list_avg = np.average(freq_list)
	print('Timestam(Tot) Variance:', list_var, '  Avg:',list_avg)


	row_cursor = 0
	freq_list = []





	#except IndexError:
	#	print('freq_list:',freq_list)