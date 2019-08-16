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
import array


#Variables
file_num = 0
total_files = 0
column_cursor = 0
prior_value = 0
later_value = 0
nano_freq = 0
nano_freq_list = []
samp_list = []
freq_var = 0
rows = 0
plot_array = array.array('l',[])


#Functions
def delta_lister():

	row_cursor = 0
	plot_array = array.array('l',[])

	while row_cursor <= rows-2:
		prior_value = df.iloc[row_cursor,column_cursor]
		row_cursor = row_cursor + 1
		later_value = df.iloc[row_cursor,column_cursor]
		nano_freq = later_value - prior_value
		plot_array.append(nano_freq)




def histogram():
	
	plt.hist(plot_array, bins=107000)
	plt.xlabel('File')
	plt.ylabel('Timestamp Delta Variance')


	#display
	plt.show(plt.hist)




###########
#THE CODE
###########


#directory of the files
dest_dir = "/home/fred/Desktop/g"

#number of files in directory
total_files = len(os.listdir(dest_dir))


#Create DataFrames by looping through csv files
for file_name in glob.glob(os.path.join(dest_dir, '*.csv')):
	df = pd.read_csv(file_name,dtype='int64')
	file_num = file_num + 1


	#Determine Basic File Info
	columns = len(df.columns)
	rows = len(df.index)


	#Print Basic File Info [NOTE 1]
	print('\n\nFile',file_num,'/',total_files,': ',file_name[21:])
	print('Column Count:', columns,' Row Count:', rows) 


	#Find deltas		
	delta_lister()

	#Print Histogram
	histogram()



# [NOTE 1]: In the 'while' loop, the 'rows'  is subtracted by two 
# because otherwise it produces "Index Error: single positional 
# indexer is out-of-bounds"














###########################
###The Archive of Old Code
############################


####### Making Freq. Variances #############

### under delta_lister instead of plot_array
#	nano_freq_list.insert(0 , nano_freq)



### at the end of code
#	freq_var = (np.var(nano_freq_list))
#	print('Freq Var:',freq_var)
#	nano_freq_list = []
