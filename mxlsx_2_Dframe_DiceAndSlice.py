#!/usr/bin/env python3
# coding: utf-8
#
# JupyterLab Notebook Exercises:
#
# Verbose REFERENTIAL material to be utilized in a LINUX environment.
#
# Nonexistent directory './data' will be created in
# the Default Working Directory.

#
# Files created in ./data:
#   COLUMNS_('Hyundai', 'Mazda').csv
#   COLUMNS_('Hyundai',).csv
#   COLUMNS_('Mazda', 'Hyundai').csv
#   COLUMNS_('Mazda',).csv
#   ROWS_Hyundai > 1 and Hyundai < 5.csv
#   ROWS_Mazda > 1 and Mazda < 5.csv
#   carsales.xlsx
#
from IPython.display import display
from imports import (
    create_column_based_subset_DataFrame as
    E_create_column_based_subset_DataFrame
)
from imports import (
    create_query_based_subset_DataFrame as
    E_create_query_based_subset_DataFrame
)
from imports import display_time as E_display_time
from imports import does_the_xlsx_file_exist as E_does_the_xlsx_file_exist
from imports import write_dataframe_to_xlsx as E_write_dataframe_to_xlsx
import gc
import pandas as pd
#
'''
if xlsx file './data/carsales.xlsx' exists:
    jump to 'HouseKeepingEnded'

Create DataFrame 'dic_cardata' from a dictionary
Rename the DataFrame Index.
Write file './data/carsales.xlsx'.

            HouseKeepingEnded:

Create DataFrame 'df_data' by reading file './data/carsales.xlsx'.

Create several subset DataFrames from 'df_data' varying the
    number and/or order of columns extracted.

Create several subset DataFrames by conditionally querying
    DataFrame 'df_data'.
'''
#
# Create an empty DataFrame to facilitate deletion WITHOUT an error
#   if xlsx file './data/carsales.xlsx' exists and
#   DataFrame df_carsales' was not populated from a dynamically
#   created xlsx file.
#
# If xlsx file './data/carsales.xlsx' was not found, create it then
#   rename the Index of DataFrame 'df_carsales'

name_dir = './data/'
name_file_xlsx = 'carsales.xlsx'
name_filepath = name_dir + name_file_xlsx
flag_create = E_does_the_xlsx_file_exist(name_dir, name_filepath)
if not flag_create:
    df_carsales = pd.DataFrame()
else:
    dic_cardata = {
        'Hyundai': {
            'One': 2, 'Two': 6, 'Three': 2, 'Four': 3, 'Five': 0,
            'Six': 4, 'Seven': 7,
        },
        'Mazda': {
            'One': 12, 'Two': 11, 'Three': 0, 'Four': 0, 'Five': 0,
            'Six': 4, 'Seven': 1,
        },
        'Mercedes': {
            'One': 2, 'Two': 4, 'Three': 0, 'Four': 4, 'Five': 0,
            'Six': 3, 'Seven': 3,
        },
        'Ford': {
            'One': 3, 'Two': 0, 'Three': 0, 'Four': 1, 'Five': 6,
            'Six': 12, 'Seven': 5,
        },
        'BYD': {
            'One': 9, 'Two': 3, 'Three': 4, 'Four': 1, 'Five': 0,
            'Six': 0, 'Seven': 1,
        },
        'Renault': {
            'One': 12, 'Two': 1, 'Three': 0, 'Four': 0, 'Five': 3,
            'Six': 1, 'Seven': 1,
        },
        'Volvo': {
            'One': 1, 'Two': 4, 'Three': 0, 'Four': 0, 'Five': 0,
            'Six': 11, 'Seven': 12,
        },
    }
    df_carsales = pd.DataFrame(dic_cardata)
    df_carsales.index.rename(
        'Sales Location', inplace=True
    )

    E_write_dataframe_to_xlsx(
        name_dir, name_filepath, df_carsales)

# HouseKeepingEnded:

# Create DataFrame 'df_data' by reading './data/carsales.xlsx'.
# Get the Index name via parameter'index_col=0'.
# Store the Index in 'df_data_index'.
df_data = pd.read_excel(name_filepath, index_col=0)
df_original = df_data.copy()

print('\ndf_original info:')
df_original.info()

print('\ndf_original:')
display(df_original)

# Create a column-based subset DataFrame from DataFrame 'df_data'.
column_tuple = ('Mazda',)
df_subsetM = E_create_column_based_subset_DataFrame(
    df_data, column_tuple)

# Create a query-based subset DataFrame from DataFrame 'df_data'
#   when row selection is conditional.
qstring = str('Mazda > 1 and Mazda < 5')
df_subset1 = E_create_query_based_subset_DataFrame(
    df_data, qstring)

# Create a column-based subset DataFrame from DataFrame 'df_data'.
column_tuple = ('Mazda', 'Hyundai')
df_subsetMH = E_create_column_based_subset_DataFrame(
    df_data, column_tuple)

# Create a column-based subset DataFrame from DataFrame 'df_data'.
column_tuple = ('Hyundai',)
df_subsetH = E_create_column_based_subset_DataFrame(
    df_data, column_tuple)

# Create a query-based subset DataFrame from DataFrame 'df_data'
#   when row selection is conditional.
qstring = str('Hyundai > 1 and Hyundai < 5')
df_subset2 = E_create_query_based_subset_DataFrame(
    df_data, qstring)

# Create a column-based subset DataFrame from DataFrame 'df_data'.
column_tuple = ('Hyundai', 'Mazda',)
df_subsetHM = E_create_column_based_subset_DataFrame(
    df_data, column_tuple)

del df_carsales
del df_data
del df_original
del df_subset1
del df_subset2
del df_subsetH
del df_subsetHM
del df_subsetM
del df_subsetMH
gc.collect()

E_display_time()
#
# EOF
