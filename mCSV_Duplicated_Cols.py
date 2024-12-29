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
# Nonexistent file 'original_cols.csv' will be written in './data'.
# Nonexistent file 'duplicated_cols.csv' will be written in './data'.
# Nonexistent file 'unique_cols.csv' will be written in './data'.
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
    insert_column_dupes_YES as
    E_insert_column_dupes_YES
)
from imports import (
    remove_duplicate_columns as
    E_remove_duplicate_columns
)
from imports import (
    rename_columns_inplace as
    E_rename_columns_inplace
)
from imports import (
    rename_columns_not_inplace as
    E_rename_columns_not_inplace
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
name_file_dupe_cols = 'duplicated_cols.csv'
name_file_original_cols = 'original_cols.csv'
name_file_unique_cols = 'unique_cols.csv'
name_filepath_dupe_cols = name_dir + name_file_dupe_cols
name_filepath_original_cols = name_dir + name_file_original_cols
name_filepath_unique_cols = name_dir + name_file_unique_cols
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

# Append duplicate columns
BYD = [9, 9, nan_, 4, 1, 0, 1, 1,]
Hyundai = [2, 2, nan_, 6, 3, 0, 7, 7,]
Mazda = [12, 12, nan_, 0, 0, 0, 4, 4,]
E_insert_column_dupes_YES(
    df_cols, len(df_cols.columns), 'BYD', BYD)
E_insert_column_dupes_YES(
    df_cols, len(df_cols.columns), 'Hyundai', Hyundai)
E_insert_column_dupes_YES(
    df_cols, len(df_cols.columns), 'Mazda', Mazda)

# Rename duplicate columns
if 'BYD.1' in df_cols.columns:
    df_cols = E_rename_columns_not_inplace(
        df_cols, columns_dic={'BYD.1': 'BYD'})
if 'Hyundai.1' in df_cols.columns:
    E_rename_columns_inplace(
        df_cols, columns_dic={'Hyundai.1': 'Hyundai'})
if 'Mazda.1' in df_cols.columns:
    E_rename_columns_inplace(
        df_cols, columns_dic={'Mazda.1': 'Mazda'})
df_duplicated = df_cols.copy()

print('\ndf_cols info:')
df_cols.info()

print('\nOriginal_Cols:')
display(df_original)

print('\nOriginal and added Duplicate Cols:')
display(df_cols)

E_write_dataframe_to_CSV(
    name_dir, name_filepath_dupe_cols, df_duplicated)

df_unique = E_remove_duplicate_columns(df_cols)
E_write_dataframe_to_CSV(
    name_dir, name_filepath_unique_cols, df_unique)

del df_cols
del df_duplicated
del df_original
del df_unique
gc.collect()

E_display_time()
#
# EOF
