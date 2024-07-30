


"""
Author: Sebastian Otarola-Bustos
Email: sotarolabustos@hazenandsawyer.com
Date: 7/30/2024

Description:
This script combines all the data received from City of Atlanta, combines it in a single file (i.e., df_merged.csv) and calculate summary statistics for
each water quality parameter and level (i.e., STP1, STP2, STP3, STP4, STP5, and STP6).

Each folder corresponds to a different variable type (e.g., BGA, Conductivity, Depth, ODO, ORP, and PH).
The script performs the following tasks:
1. Reads data files from each folder.
2. Renames specific columns in the data files.
3. Adds a 'parameter' column to each DataFrame.
4. Concatenates all DataFrames into a single DataFrame.
5. Calculates summary statistics for each variable type and depth.
6. Stores the summary statistics in a separate DataFrame.

The script assumes that the data files are in Excel format and that the columns to be renamed are 'Tagname', 'TimeStamp', and 'Value'.
"""

import numpy as np
import pandas as pd
import os
import openpyxl

path_data = r'C:\Users\sotarolabustos\Documents\Hazen\Projects\quarry_lakes\City of Atlanta\Data'
# Get the list of all entries in the directory
all_entries = os.listdir(path_data)
# Filter out only the directories
folders = [entry for entry in all_entries if os.path.isdir(os.path.join(path_data, entry))]

# Create empty dataframe to store all data together
df_merged = pd.DataFrame()
# Create empty dataframe to save all statistics together
df_summary = pd.DataFrame()
# List of strings to check in filenames likely corresponding to different heights
list_str = ['STP1', 'STP2', 'STP3', 'STP4', 'STP5', 'STP6']

# Each variable type (e.g., BGA, Conductivity, Depth, ODO, ORP, and PH) are saved in a different folder inside the same directory
# loop through folders (variables)
for ii in range(0,len(folders)):
    # Retrieve folder name that matches variable
    folder_tmp = folders[ii]
    folder_path_tmp = os.path.join(path_data,folder_tmp)
    # Retrieve list of files
    all_entries = os.listdir(folder_path_tmp)
    # Filter out only the files
    files = [entry for entry in all_entries if os.path.isfile(os.path.join(folder_path_tmp, entry))]
    #print(files)
    for jj in range(0,len(files)):
        # Filenames contain regular expressions e.g., STP1, STP2, STP3, STP4, STP5, and STP6
        filename_tmp = files[jj]
        filepath_tmp = os.path.join(folder_path_tmp, filename_tmp)
        # Check if any string in list_str is in the filename
        for s in list_str:
            if s in filename_tmp:
                stp_string = s
                print(stp_string)
                break
            else:
                #print("No match found")
                continue
        # Load dataframe
        df_tmp = pd.read_excel(filepath_tmp)
        # Rename columns
        df_tmp.rename(columns={'Tagname':'TAG', 'TimeStamp': 'Datetime', 'Value': 'MeasureValue'}, inplace=True)
        # Add 'parameter' column
        df_tmp['parameter'] = folder_tmp
        # Add 'depth' column
        df_tmp['depth'] = stp_string
        # Concatenate df_tmp to df_merged that will contain all data
        df_merged = pd.concat([df_merged, df_tmp], ignore_index=True)
        # Calculate df_summary with statistics for all variables
        summary_data = {
            'Parameter': [folder_tmp],
            'Depth': [stp_string],
            'Start_Date': [df_tmp['Datetime'].min()],
            'End_Date': [df_tmp['Datetime'].max()],
            'counts': [df_tmp.shape[0]],
            'min': [df_tmp['MeasureValue'].min()],
            'median': [df_tmp['MeasureValue'].median()],
            'mean': [df_tmp['MeasureValue'].mean()],
            'max': [df_tmp['MeasureValue'].max()]
        }
        df_summary_tmp = pd.DataFrame(summary_data)
        # Concatenate df_summary_tmp to df_summary
        df_summary = pd.concat([df_summary, df_summary_tmp],ignore_index=True)
# Save summary
df_summary.to_csv('./df_summary.csv', index=False)
# Save concatenated data
df_merged.to_csv('./df_merged.csv', index=False)   