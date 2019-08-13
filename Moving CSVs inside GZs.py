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


#Where the .gz files are stored and where the .csv files need to go
source_dir = "/home/fred/Desktop/df"
dest_dir = "/home/fred/Desktop/g"


#Code to move .csv files into the same directory
for src_name in glob.glob(os.path.join(source_dir, '*.gz')):
    base = os.path.basename(src_name)
    dest_name = os.path.join(dest_dir, base[:-3])
    with gzip.open(src_name, 'rb') as infile:
        with open(dest_name, 'wb') as outfile:
            for line in infile:
                outfile.write(line)


#Delete empty files
for file_name in glob.glob(os.path.join(dest_dir, '*.csv')):
	total_count = total_count+1
	statinfo = os.stat(file_name)
	if statinfo.st_size<1000000:
		deleted_count = deleted_count+1
		os.remove(file_name)
print('Out of',total_count,'csv files,',deleted_count,'were empty and removed.')

"""
#Create DataFrames of remaining .csv files
for file_name in glob.glob(os.path.join(dest_dir, '*.csv')):
	df = pd.read_csv(file_name)
	print('\n\n',file_name,'\n',df.head())
	print('\n',df.info())
"""
