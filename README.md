# water-quality-ATL
See script 'process_wq_data_Atlanta.py'

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
