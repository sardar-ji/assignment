#!/usr/bin/env python

#####################################################################################################################################################
# This script accepts the csv file at run time and generate a new CSV file that only includes properties sold for less than the average price / foot.
# If csv file and script is present at the same location then give the csv file name only otherwise give the absolute path of the csv.
# Make sure panda is installed.
# Eliminating the rows, which has sq__ft value zero. since denominator can't be zero while division.
# Get the average of each row i.e price/sq__ft.
# Find the mean value from line#8.
# Compare each value obtained from line#8 with with mean value i.e < mean
# Final.csv will be generated.
######################################################################################################################################################

import os
import pandas as pd
import numpy as np

#Input the csv file name.
print("###################################################################################################")
file_path=raw_input("Please enter the your csv file path: ")
assert os.path.exists(file_path),"File not found at, "+str(file_path)

#Define the dataframe object which read csv
df_data = pd.read_csv(file_path)
print("Before parsing, no. of record is: "+ str(df_data.shape[0]) )

# Delete these row indexes from dataFrame which has sq__ft 0.
indexNames = df_data[ df_data['sq__ft'] == 0 ].index
df_data.drop(indexNames , inplace=True)


#Get the average price/sqft for each row
df_data['avg_sqft'] = df_data['price'] / df_data['sq__ft'] 

#Get the mean average
meanval=df_data["avg_sqft"].mean()
print("The average per sqft value is "+str(meanval))

#Compare dataframe with avg per/sqft price
df_data = df_data.loc[df_data['avg_sqft'] < meanval] 

#Sequence the column.This step is optional.
column_order=['street','city','zip','state','beds','baths','sq__ft','type','sale_date','price','latitude','longitude','avg_sqft']

#Export the data into 'Final.csv' file.
df_data[column_order].to_csv('Final.csv',index=False)
print("After parsing, no. of record  is: "+ str(df_data.shape[0]) )
print("Completed!! 'Final.csv' is created at "+os.getcwd()+" with new column named 'avg_sqft'")
print("###################################################################################################")
