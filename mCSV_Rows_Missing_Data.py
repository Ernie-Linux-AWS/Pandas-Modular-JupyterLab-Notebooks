#!/usr/bin/env python3
# coding: utf-8

# JupyterLab Notebook Exercises:
#
# Verbose REFERENTIAL material to be utilized in a LINUX environment
#
# Nonexistent directory './data' will be created in
# the Default Working Directory
#
# Nonexistent file 'Nans_2_Col_mean.csv' will be written in './data'.
# Nonexistent file 'No_Nan_only_rows.csv' will be written in './data'
# Nonexistent file 'original_rows.csv' will be written in './data'
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
    drop_rows_of_nan_inplace as
    E_drop_rows_of_nan_inplace
)
from imports import (
    num_col_nan_2_col_mean_inplace as
    E_num_col_nan_2_col_mean_inplace
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
name_file_Nans_2_Col_mean = 'Nans_2_Col_mean.csv'
name_file_No_Nan_only_rows = 'No_Nan_only_rows.csv'
name_file_original_rows = 'original_rows.csv'
name_filepath_Nans_2_Col_mean = name_dir + name_file_Nans_2_Col_mean
name_filepath_No_Nan_only_rows = name_dir + name_file_No_Nan_only_rows
name_filepath_original_rows = name_dir + name_file_original_rows
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

print('\ndf_Rows info:')
df_rows.info()

print('\nOriginal Rows:')
display(df_original)

E_drop_rows_of_nan_inplace(df_rows)
print('\nRows not containing only Nan:')
df_no_nan = df_rows.copy()
display(df_no_nan)

E_write_dataframe_to_CSV(
    name_dir, name_filepath_No_Nan_only_rows, df_no_nan)

E_num_col_nan_2_col_mean_inplace(df_rows)
df_means = df_rows.copy()

E_write_dataframe_to_CSV(
    name_dir, name_filepath_Nans_2_Col_mean, df_means)

del df_means
del df_no_nan
del df_original
del df_rows
gc.collect()

E_display_time()
#
# EOF
