#!/usr/bin/env python3
# coding: utf-8
#
# JupyterLab Notebook Exercises:
#
# Verbose REFERENTIAL material to be utilized in a LINUX environment
#
# Nonexistent directory './data' will be created in
# the Default Working Directory.
#
# Nonexistent file 'Categoric.csv' will be written in './data'.
# Nonexistent file 'Original.csv' will be written in './data'.
# Nonexistent file 'Transformed.csv' will be written in './data'.
#
'''
if CSV file './data/Original.csv' exists:
    jump to 'HouseKeepingEnded'

Create DataFrame 'df_mixed' from dictionary 'dic_mixed'.
Write file './data/Original.csv'.

            HouseKeepingEnded:

Create DataFrame 'df_mixed' by reading file
    './data/Original.csv'.

Extract columns (numeric vs object) from DataFrame 'df_mixed'

Write file './data/Categoric.csv'

Initialize the encoder, replacing deprecated
    'sparse=False' with 'sparse_output=False

Fit and transform yielding 'enc'

Get feature names

Convert transformed array to a DataFrame

Concatenate encoded DataFrame to numerical DataFrame.

Write file './data/Transformed.csv'

Delete all created DataFrames from memory
'''
#
from IPython.display import display
from imports import display_time as E_display_time
from imports import (
    does_the_CSV_file_exist as
    E_does_the_CSV_file_exist
)
from imports import one_hot_encode as E_one_hot_encode
from imports import (
    write_dataframe_to_CSV as
    E_write_dataframe_to_CSV
)
import gc
import pandas as pd
#
# Create empty DataFrame 'df_mixed'to facilitate deletion WITHOUT
#   an error if CSV file './data/Original.csv' exists and
#   DataFrame 'df_mixed' was not populated from a dynamically created
#   csv file.
name_dir = './data/'
name_file_categoric = 'Categoric.csv'
name_file_original = 'Original.csv'
name_file_transformed = 'Transformed.csv'
name_filepath_categoric = name_dir + name_file_categoric
name_filepath_original = name_dir + name_file_original
name_filepath_transformed = name_dir + name_file_transformed
flag_create = E_does_the_CSV_file_exist(name_dir, name_filepath_original)
if not flag_create:
    df_mixed = pd.DataFrame()
else:
    dic_mixed = {
        'Count': [3, 4, 5, 6, 7,],
        'Item': ['coat', 'shirt', 'coat', 'beanie', 'shirt',],
        'Size': ['large', 'medium', 'medium', 'small', 'large',],
        'Color': ['red', 'yellow', 'blue', 'yellow', 'red',],
    }
    df_mixed = pd.DataFrame(dic_mixed)

    E_write_dataframe_to_CSV(name_dir, name_filepath_original, df_mixed)

# HouseKeepingEnded:

# Create DataFrame 'df_mixed' by reading
#   './data/original.csv'.
df_mixed = pd.read_csv(name_filepath_original, index_col=0)
df_original = df_mixed.copy()

print('\ndf_original info:')
df_original.info()

print('\noriginal:')

display(df_original)

(X_categoric, df_transformed) = E_one_hot_encode(df_mixed)
E_write_dataframe_to_CSV(
    name_dir, name_filepath_categoric, X_categoric)
E_write_dataframe_to_CSV(
    name_dir, name_filepath_transformed, df_transformed)

del df_mixed
del df_transformed
del df_original
gc.collect()

E_display_time()
#
# EOF
