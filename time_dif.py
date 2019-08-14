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
samp1 = 0
samp2 = 0
samp3 = 0
samp4 = 0
samp5 = 0
samp6 = 0
samp_list = []
samp_var = 0


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
	samp1 = list_var
	
	row_cursor = 20000
	freq_list = []
	while row_cursor <= 25000:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	samp2 = list_var


	row_cursor = 40000
	freq_list = []
	while row_cursor <= 45000:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	samp3 = list_var


	row_cursor = 60000
	freq_list = []
	while row_cursor <= 65000:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	samp4 = list_var

	row_cursor = 80000
	freq_list = []
	while row_cursor <= 85000:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	samp5 = list_var


	row_cursor = 100000
	freq_list = []
	while row_cursor <= 105000:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	samp6 = list_var


	row_cursor = 0
	freq_list = []
	while row_cursor <= (rows-2):
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		freq_list.insert(0 , nano_freq)
		
	list_var = np.var(freq_list)
	samp_list = [samp1,samp2,samp3,samp4,samp5,samp6]
	samp_var = np.var(samp_list)


	print('Samp1:',samp1)
	print('Samp2:', samp2)
	print('Samp3:', samp3)
	print('Samp4:',samp4)
	print('Samp5:',samp5)
	print('Samp6:',samp6)		
	print('Total:',list_var)
	print('Samp Var:', samp_var)



	row_cursor = 0
	freq_list = []
	samp_list = []




	#except IndexError:
	#	print('freq_list:',freq_list)