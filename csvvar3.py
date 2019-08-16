#######################################
#FINDING ROW DELTAS IN DEVICE CSV FILES
#######################################


#Imports
import os
import gzip
import glob
import os.path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Variables
file_num = 0
total_files = 0
column_cursor = 0
prior_value = 0
later_value = 0
nano_freq = 0
nano_freq_list = []
freq_var = 0
rows = 0
unique_deltas = []
unique_counts = []
unique_deltas_dict = []
errors = []
first_timestamp_list = []
avg_delta_list = []
rows_list = []
x=0



#Functions

def delta_lister(): #outputs "nano_freq_list"

	unique_deltas = []
	unique_counts = []
	row_cursor = 0

	while row_cursor <= rows - 2: #[NOTE 1]
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		nano_freq_list.insert(0 , nano_freq)



def unique_deltas_df(): #inputs "nano_freq_list", outputs "unique_deltas_df" dataframe

	unique_deltas = np.unique(nano_freq_list)

	for x in unique_deltas:
		unique_counts.insert(len(unique_counts),nano_freq_list.count(x))

	unique_deltas_dict = {'Unique Deltas':unique_deltas, 'Count':unique_counts}

	unique_deltas_df = pd.DataFrame(unique_deltas_dict)	

	print(unique_deltas_df)




def historigram(): #inputs "nano_freq_list"
	plt.hist(nano_freq_list, bins=170,range=[33332600,33334500])
	plt.yscale('log')
	plt.xlabel('Timestamp Deltas (ns)')
	plt.ylabel('# of Timestamps')
	
	display
	plt.show(plt.hist)



def displays(): #inputs "nano_freq_list", cleans up lists, outputs "1st timestamp list", "avg timestamp delta"
	global nano_freq_list
	global unique_deltas_dict
	global unique_deltas_df
	global unique_counts
	global deltas

	first_timestamp_list.insert(len(first_timestamp_list),df.iloc[0,0])
	avg_delta_list.insert(len(avg_delta_list),np.average(nano_freq_list))

	print('First timestamp (ns):',df.iloc[0,0])
	print('Average timestamp delta (ns):',np.average(nano_freq_list))
	
	nano_freq_list = []
	unique_deltas = []
	unique_counts = []
	unique_deltas_dict = []
	print()



def endgame():
	global first_timestamp_list
	global avg_delta_list
	global rows
	global rows_list

	unique_timestamp_counts = []
	unique_avg_delta_counts = []
	rows_counts = []

	#Unique First Timpstamps
	unique_first_timestamps = np.unique(first_timestamp_list)
	for x in unique_first_timestamps:
		unique_timestamp_counts.insert(len(unique_timestamp_counts),first_timestamp_list.count(x))
	unique_first_timestamp_dict = {'Unique 1st Timestamps':unique_first_timestamps, 'Count':unique_timestamp_counts}
	unique_first_timestamp_df = pd.DataFrame(unique_first_timestamp_dict)	
	print('UNIQUE FIRST TIMESTAMPS\n',unique_first_timestamp_df,'\n\n')


	#Unique Rows
	unique_rows = np.unique(rows_list)
	for x in unique_rows:
		rows_counts.insert(len(rows_counts),rows_list.count(x))
	rows_dict = {'Unique # of Rows': unique_rows, 'Count':rows_counts}
	rows_df = pd.DataFrame(rows_dict)
	print('UNIQUE NUMBER OF ROWS\n',rows_df,'\n\n')




	#Unique Avg Deltas
	unique_avg_deltas = np.unique(avg_delta_list)
	for x in unique_avg_deltas:
		unique_avg_delta_counts.insert(len(unique_avg_delta_counts),avg_delta_list.count(x))
	unique_avg_delta_dict = {'Unique Avg Deltas':unique_avg_deltas, 'Count':unique_avg_delta_counts}
	unique_avg_delta_df = pd.DataFrame(unique_avg_delta_dict)
	print('UNIQUE AVG DELTAS (ie, idential files)\n',unique_avg_delta_df,'\n\n')





########################
#THE CODE
#########################


#directory of the files
dest_dir = "/home/fred/Desktop/g"

#number of files in directory
total_files = len(os.listdir(dest_dir))


#Create DataFrames by looping through csv files
for file_name in glob.glob(os.path.join(dest_dir, '*.csv')):
	while x < 2:

		x = x + 1
		df = pd.read_csv(file_name,dtype='int64')
		file_num = file_num + 1

		#Determine Basic File Info
		columns = len(df.columns)
		rows = len(df.index)
		rows_list.insert(len(rows_list),rows)

		#Print Basic File Info 
		print('\n\nFile',file_num,'/',total_files,': ',file_name[21:])
		print('Column Count:', columns,' Row Count:', rows) 


		try:
			delta_lister()

			unique_deltas_df()

			displays()

		except:
			print("Error recorded at file",file_num,'-',file_name[21:])
			errors.insert(len(errors),[file_num, file_name])


endgame()

print('Here were the errors:', errors)





