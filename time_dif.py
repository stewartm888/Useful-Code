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
	print('\n\nFile',iteration,'/',file_count,': ',file_name)
	print('Column Count:', columns,' Row Count:', rows) 
	print('First Timestamp:',prior_value,'\n')


#Iterate rows
	while DF_End_Flag == 0:
		try:
			prior_value = df.iloc[row_cursor,column_cursor]
			row_cursor = row_cursor + 1
			later_value = df.iloc[row_cursor,column_cursor]
			nano_freq = later_value - prior_value
			print('File:',iteration,'Row',row_cursor,'/',rows,' -- jump (ns):',nano_freq)
			freq_list.insert(0 , nano_freq)
		except IndexError:
			row_cursor = 0
			prior_value = 0
			later_value = 0
			nano_freq = 0
			DF_End_Flag = 1

	DF_End_Flag = 0


	#except IndexError:
	#	print('freq_list:',freq_list)