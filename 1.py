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

#number of files in directory
file_count = len(os.listdir(dest_dir))


#Create DataFrames by looping through csv files
for file_name in glob.glob(os.path.join(dest_dir, '*.csv')):
	df = pd.read_csv(file_name)

#file count
	iteration = iteration + 1
	print('File:',iteration,'/',file_count)

#file name
	print(file_name)

#column count
	print('Column Count:', len(df.columns))


#Variance between uuids
	print('Rows with non-zero variances between UUIDs:')
	if np.var(df,axis=1).any() != 0:
		print(np.var(df,axis=1))

#Empty line for next iteration
	print('\n')





##############################
### THE ARCHIVE - old code ###
##############################



"""
#Null count - TESTED: NO NULLS
	print('Nulls in file:', df.isnull().sum().sum())
	total_nulls = total_nulls + df.isnull().sum().sum()
	print('Total nulls so far:', total_nulls)
"""


"""
#Counting variances for files with multiple columns

#file count
	iteration = iteration +1
	print('File:',iteration,'/',file_count)
	if len(df.columns)>1 and np.var(df,axis=1).any() == 0:

	#file name
		print(file_name)

	#column count
		print('Column Count:', len(df.columns))


	#Variance between uuids
		if np.var(df,axis=1).any() != 0:
			print('Variances between UUIDs per row:')
			print(np.var(df,axis=1))
		else:
			print('This device has no variances between its UUIDs')
	#Empty line for next iteration
		print('\n')
"""




"""
#Variances and concat

d1 = ("dfr-DFRPMU-MT1_300")
d2 = ("dfr-DFRPMU-SUR2_535")
d3 = ("dfr-DFRBATH_COUNTY_DFR_3")

df1 = (pd.read_csv("/home/fred/Desktop/Workplace/variance_code/dfr-DFRPMU-MT1_300.csv"))
df2 = (pd.read_csv("/home/fred/Desktop/Workplace/variance_code/dfr-DFRPMU-SUR2_535.csv"))
df3 = (pd.read_csv("/home/fred/Desktop/Workplace/variance_code/dfr-DFRBATH_COUNTY_DFR_3.csv"))

df_list = [df1,df2,df3]
d_list = [d1,d2,d3]

for i in df_list:
	print('\n','\n','\n','Column Variances for',d_list[a],'\n')
	a=a+1
	print(np.var(i,axis=0))


dfcombo = pd.concat([df1,df2,df3], axis = 1)
print('\n','\n','\n','Column Variances Across all sensors\n')
print(np.var(dfcombo,axis=0))
"""

