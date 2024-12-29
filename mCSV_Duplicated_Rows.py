#!/usr/bin/env python3
# coding: utf-8

# JupyterLab Notebook Exercises:
#
# Verbose REFERENTIAL material to be utilized in a LINUX environment
#
# Nonexistent directory './data' will be created in
# the Default Working Directory
#
# Nonexistent file 'original_rows.csv' will be written in './data'
# Nonexistent file 'duplicated_rows.csv' will be written in './data'
# Nonexistent file 'unique_rows.csv' will be written in './data'
#
'''
if CSV file './data/original_rows.csv' exists:
    jump to 'HouseKeepingEnded'

Create DataFrame 'df_rows' from dictionary 'dic_rows'
Write file './data/original_rows.csv'

            HouseKeepingEnded:

Create DataFrame 'df_rows' by reading file
    './data/original_rows.csv'.

Append duplicate rows
Locate and remove duplicate rows.
Resquence row numbers.

Delete all created DataFrames from memory.
'''
#
from IPython.display import display
from imports import display_time as E_display_time
from imports import (
    does_the_CSV_file_exist as
    E_does_the_CSV_file_exist
)
from imports import (
    remove_duplicate_rows as
    E_remove_duplicate_rows
)
from imports import (
    write_dataframe_to_CSV as
    E_write_dataframe_to_CSV
)
import gc
import numpy as np
import pandas as pd
#
#
# Create empty DataFrame 'df_rows'to facilitate deletion WITHOUT
#   an error if CSV file './data/duplicated_rows.csv' exists and
#   DataFrame 'df_rows' was not populated from a dynamically created
#   csv file.
df_rows = pd.DataFrame()
name_dir = './data/'
name_file_dupe_rows = 'duplicated_rows.csv'
name_file_original_rows = 'original_rows.csv'
name_file_unique_rows = 'unique_rows.csv'
name_filepath_dupe_rows = name_dir + name_file_dupe_rows
name_filepath_original_rows = name_dir + name_file_original_rows
name_filepath_unique_rows = name_dir + name_file_unique_rows
flag_create = E_does_the_CSV_file_exist(
    name_dir, name_filepath_original_rows)

nan_ = np.nan
if not flag_create:
    df_rows = pd.DataFrame()
else:
    nan_ = np.nan
    dic_rows = {
        'BYD': [9, 9, nan_, 4, 1, 0, 1, 1,],
        'Ford': [3, 2, nan_, nan_, 1, 6, 11, 12,],
        'Hyundai': [2, 3, nan_, 6, 3, 0, 7, 7,],
        'Jaguar': [nan_, nan_, nan_, nan_, nan_, nan_, nan_, nan_,],
        'Mazda': [12, 12, nan_, 0, 0, 0, 4, 4,],
        'Volvo': [1, 1, nan_, nan_, nan_, nan_, 12, 11,],
    }
    # Create DataFrame 'df_rows' from dictionary
    #  'dic_rows'
    df_rows = pd.DataFrame(dic_rows)
    df_original = df_rows

    E_write_dataframe_to_CSV(
        name_dir, name_filepath_original_rows, df_rows)

# HouseKeepingEnded:

# Create DataFrame 'df_rows' by reading
#   './data/columns_duplicated.CSV'.
    # Copy it to 'df_original'
df_rows = pd.read_csv(
    name_filepath_original_rows, index_col=0)
df_original = df_rows.copy()

# Append "duplicate" rows
new_row_1 = [9, 3, 2, nan_, 12, 1]
new_row_2 = [9, 2, 3, nan_, 12, 1]
new_row_3 = [0, 6, 0, nan_, 0, nan_]
df_rows.loc[len(df_rows)] = new_row_1
df_rows.loc[len(df_rows)] = new_row_2
df_rows.loc[len(df_rows)] = new_row_3
df_duplicated = df_rows.copy()
print('\ndf_rows info:')
df_rows.info()

print('\nOriginal Rows:')
display(df_original)

print('\nOriginal and added Duplicate Rows:')
display(df_rows)

E_write_dataframe_to_CSV(
    name_dir, name_filepath_dupe_rows, df_duplicated)

df_unique = E_remove_duplicate_rows(df_rows)
E_write_dataframe_to_CSV(
    name_dir, name_filepath_unique_rows, df_unique)

del df_duplicated
del df_original
del df_rows
del df_unique
gc.collect()

E_display_time()
# EOF
