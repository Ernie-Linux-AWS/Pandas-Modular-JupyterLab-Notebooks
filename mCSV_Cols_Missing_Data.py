#!/usr/bin/env python3
# coding: utf-8
#
# JupyterLab Notebook Exercises:
#
# Verbose REFERENTIAL material to be utilized in a LINUX environment
#
# Nonexistent directory './data' will be created in
# the Default Working Directory
#
# Nonexistent file 'Nans_2_Col_mean.csv' will be written in './data'.
# Nonexistent file 'No_Nan_only_cols.csv' will be written in './data'.
# Nonexistent file 'original_cols.csv' will be written in './data'.
#
'''
if CSV file './data/original_cols.csv' exists:
    jump to 'HouseKeepingEnded'

Create DataFrame 'df_cols' from dictionary 'dic_cols'
Write file './data/original_cols.csv'.

            HouseKeepingEnded:

Create DataFrame 'df_cols' by reading file
    './data/original_cols.csv'.

Append duplicate columns
Locate and remove duplicate columns

Delete all created DataFrames from memory
'''
#
from IPython.display import display
from imports import display_time as E_display_time
from imports import (
    does_the_CSV_file_exist as
    E_does_the_CSV_file_exist
)
from imports import (
    drop_cols_of_nan_inplace as
    E_drop_cols_of_nan_inplace
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
# Create empty DataFrame 'df_cols'to facilitate deletion WITHOUT
#   an error if CSV file './data/duplicated_cols.csv' exists and
#   DataFrame 'df_cols' was not populated from a dynamically created
#   csv file.
name_dir = './data/'
name_file_Nans_2_Col_mean = 'Nans_2_Col_mean.csv'
name_file_No_Nan_only_cols = 'No_Nan_only_cols.csv'
name_file_original_cols = 'original_cols.csv'
name_filepath_Nans_2_Col_mean = name_dir + name_file_Nans_2_Col_mean
name_filepath_No_Nan_only_cols = name_dir + name_file_No_Nan_only_cols
name_filepath_original_cols = name_dir + name_file_original_cols
flag_create = E_does_the_CSV_file_exist(
    name_dir, name_filepath_original_cols)

nan_ = np.nan
if not flag_create:
    df_cols = pd.DataFrame()
else:
    dic_cols = {
        'BYD': [9, 9, nan_, 4, 1, 0, 1, 1,],
        'Ford': [3, 3, nan_, nan_, 1, 6, 12, 12,],
        'Hyundai': [2, 2, nan_, 6, 3, 0, 7, 7,],
        'Jaguar': [nan_, nan_, nan_, nan_, nan_, nan_, nan_, nan_,],
        'Mazda': [12, 12, nan_, 0, 0, 0, 4, 4,],
        'Volvo': [1, 1, nan_, nan_, nan_, nan_, 11, 11,],
    }
    # Create DataFrame 'df_cols' from dictionary
    #  'dic_cols'
    df_cols = pd.DataFrame(dic_cols)

    E_write_dataframe_to_CSV(
        name_dir, name_filepath_original_cols, df_cols)

# HouseKeepingEnded:

# Create DataFrame 'df_cols' by reading
#   './data/original_columns.CSV'
# Copy it to 'df_original'
df_cols = pd.read_csv(
    name_filepath_original_cols, index_col=0)
df_original = df_cols.copy()

print('\ndf_cols info:')
df_cols.info()

print('\nOriginal_Cols:')
display(df_original)

E_drop_cols_of_nan_inplace(df_cols)
print('\nColumns not containing only Nan:')
df_no_nan = df_cols.copy()
display(df_no_nan)

E_write_dataframe_to_CSV(
    name_dir, name_filepath_No_Nan_only_cols, df_no_nan)

E_num_col_nan_2_col_mean_inplace(df_cols)
df_means = df_cols.copy()

E_write_dataframe_to_CSV(
    name_dir, name_filepath_Nans_2_Col_mean, df_means)

del df_cols
del df_means
del df_no_nan
del df_original
gc.collect()

E_display_time()
#
# EOF
