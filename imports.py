#!/usr/bin/env python3
# coding: utf-8
'''
Suggested import statements to used by a caller:

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
from imports import (
    does_the_CSV_file_exist as
    E_does_the_CSV_file_exist
)
from imports import (
    drop_cols_of_nan_inplace as
    E_drop_cols_of_nan_inplace
)
from imports import (
    drop_cols_of_nan_not_inplace as
    E_drop_cols_of_nan_not_inplace
)
from imports import (
    drop_rows_of_nan_inplace as
    E_drop_rows_of_nan_inplace
)
from imports import (
    drop_rows_of_nan_not_inplace as
    E_drop_rows_of_nan_not_inplace
)
from imports import (
    insert_column_dupes_NO as
    E_insert_column_dupes_NO
)
from imports import (
    insert_column_dupes_YES as
    E_insert_column_dupes_YES
)
from imports import (
    num_col_nan_2_col_mean_inplace as
    E_num_col_nan_2_col_mean_inplace
)
from imports import (
    num_col_nan_2_col_mean_not_inplace as
    E_num_col_nan_2_col_mean_not_inplace
)
from imports import one_hot_encode as E_one_hot_encode
from imports import (
    remove_duplicate_columns as
    E_remove_duplicate_columns
)
from imports import (
    remove_duplicate_rows as
    E_remove_duplicate_rows
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
    set_display_precision as
    E_set_display_precision
)
from imports import (
    write_dataframe_to_CSV as
    E_write_dataframe_to_CSV
)
import gc
import pandas as pd
'''
#
from IPython.display import display
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder
import os
import pandas as pd
import time
#


def write_dataframe_to_CSV(name_dir, name_filepath, df_frame):
    # Save the DataFrame as a CSV file while
    #   including the Index and Index Labels (default)
    # Update './data' datetime stamp
    if os.path.exists(name_filepath):
        os.chmod(name_filepath, 0o644)
    with open(
        name_filepath, 'w', encoding='utf-8'
    ) as writer:
        df_frame.to_csv(writer)
        if os.path.exists(name_filepath):
            os.chmod(name_filepath, 0o444)

            # Get then display modified time info
            ti_m = os.path.getmtime(name_filepath)
            m_ti = time.ctime(ti_m)
            Path(name_dir).touch()
            print(
                f'\nDynamically generated CSV file:\n'
                f"'{name_filepath}'\nwas CREATED: {m_ti}")
    return


def write_dataframe_to_xlsx(name_dir, name_filepath, df_frame):
    '''
    Install required Python components:

    sudo dnf install pip

    pip install xlswriter --user
    '''
    # Save the DataFrame as an xlsx file while
    #   including the Index and Index Labels (default)
    # Update './data' datetime stamp
    if os.path.exists(name_filepath):
        os.chmod(name_filepath, 0o644)
    with pd.ExcelWriter(
        name_filepath
    ) as writer:
        df_frame.to_excel(writer)
        if os.path.exists(name_filepath):
            os.chmod(name_filepath, 0o444)

            # Get then display modified time info
            ti_m = os.path.getmtime(name_filepath)
            m_ti = time.ctime(ti_m)
            Path(name_dir).touch()
            print(
                f'\nDynamically generated xlsx file:\n'
                f"'{name_filepath}'\nwas CREATED: {m_ti}")
    return


def create_column_based_subset_DataFrame(df_frame, column_tuple):
    name_dir = './data/'
    name_file = f'COLUMNS_{column_tuple}.csv'
    name_filepath = name_dir + name_file
    df_frame_out = pd.DataFrame(df_frame, columns=column_tuple)
    write_dataframe_to_CSV(
        name_dir, name_filepath, df_frame_out)
    print(f'\nColumn-based subset COLUMNS: {column_tuple}')
    display(df_frame_out)
    return df_frame_out


def create_query_based_subset_DataFrame(df_frame, query_string):
    name_dir = './data/'
    name_file = f'ROWS_{query_string}.csv'
    name_filepath = name_dir + name_file
    df_subset = df_frame.query(query_string)
    write_dataframe_to_CSV(
        name_dir, name_filepath, df_subset)
    print(f'\nQuery-based subset ROWS: {query_string}')
    display(df_subset)
    return df_subset


def display_time():
    # Get time info.
    time_local = time.localtime()
    time_string = time.strftime(
        '%Y-%m-%d %H:%M:%S %Z %z', time_local)
    print(f'\n{time_string}')
    return


def does_the_CSV_file_exist(name_dir, name_filepath):
    # Ensure that the target directory exists.
    # If the target file exists force it to be read only.
    os.makedirs(name_dir, exist_ok=True)
    if os.path.exists(name_dir):
        os.chmod(name_dir, 0o755)
    if os.path.exists(name_filepath):
        flag_create_CSV = False
        os.chmod(name_filepath, 0o444)
    else:
        flag_create_CSV = True
    return flag_create_CSV


def does_the_xlsx_file_exist(name_dir, name_filepath):
    # Ensure that the target directory exists.
    # If the target file exists force it to be read only.
    os.makedirs(name_dir, exist_ok=True)
    if os.path.exists(name_dir):
        os.chmod(name_dir, 0o755)
    if os.path.exists(name_filepath):
        flag_create_xlsx = False
        os.chmod(name_filepath, 0o444)
    else:
        flag_create_xlsx = True
    return flag_create_xlsx


def drop_cols_of_nan_inplace(df_frame):
    # Drop columns containing only 'Nan'
    df_frame.dropna(how='all', axis='columns', inplace=True)
    return


def drop_cols_of_nan_not_inplace(df_frame):
    # Drop columns containing only 'Nan'
    df_new = df_frame.dropna(how='all', axis='columns')
    return df_new


def drop_rows_of_nan_inplace(df_frame):
    # Drop rows containing only 'Nan'
    df_frame.dropna(how='all', axis='index', inplace=True)
    # Resequence row numbers.
    df_frame.index = range(0, len(df_frame))
    return


def drop_rows_of_nan_not_inplace(df_frame):
    # Drop rows containing only 'Nan'
    df_new = df_frame.dropna(how='all', axis='index')
    # Resequence row numbers.
    df_frame.index = range(0, len(df_frame))
    return df_new


def insert_column_dupes_NO(
        df_frame, col_number_0_n,
        col_name, row_values_list):
    df_frame.insert(
        loc=col_number_0_n, column=col_name,
        value=row_values_list, allow_duplicates=False
     )
    return


def insert_column_dupes_YES(
        df_frame, col_number_0_n,
        col_name, row_values_list):
    df_frame.insert(
        loc=col_number_0_n, column=col_name,
        value=row_values_list, allow_duplicates=True
     )
    return


def num_col_nan_2_col_mean_inplace(df_frame):
    # Replace 'Nan' in all numeric columns with the column 'mean'.
    #   Data will be displayed with two decimal digits of precision.
    #   Columns containing only 'Nan' will not be affected.

    # Obtain original display precision
    original = pd.get_option('display.precision')
    # print(f'\nprecision = {original}')

    # Force display to use a specific number of decimal digits.
    desired_decimal_precision = 2
    pd.set_option('display.precision', desired_decimal_precision)
    # current = pd.get_option('display.precision')
    # print(f'\nprecision = {current}')

    df_frame.fillna(
        df_frame.mean(numeric_only=True), inplace=True)
    df_mean_4_nan = df_frame.copy()
    print(
        '\nNans in numeric columns were replaced '
        'with the column mean:')
    display(df_mean_4_nan)

    # Reset display precision to saved value
    # Display current display precision
    pd.set_option('display.precision', original)
    # current = pd.get_option('display.precision')
    # print(f'\nprecision = {current}')
    return


def num_col_nan_2_col_mean_not_inplace(df_frame):
    # Replace 'Nan' in all numeric columns with the column 'mean'.
    #   Data will be displayed with two decimal digits of precision.
    #   Columns containing only 'Nan' will not be affected.

    # Obtain original display precision
    original = pd.get_option('display.precision')
    # print(f'\nprecision = {original}')

    # Force display to use a specific number of decimal digits.
    desired_decimal_precision = 2
    pd.set_option('display.precision', desired_decimal_precision)
    # current = pd.get_option('display.precision')
    # print(f'\nprecision = {current}')

    df_mean_4_nan = df_frame.fillna(df_frame.mean(numeric_only=True))
    print(
        '\nNans in numeric columns were replaced '
        'with the column mean:')
    display(df_mean_4_nan)

    # Reset display precision to saved value
    # Display current display precision
    pd.set_option('display.precision', original)
    # current = pd.get_option('display.precision')
    # print(f'\nprecision = {current}')
    return df_mean_4_nan


def one_hot_encode(df_frame):
    '''
    Return

    'X_categoric' selected from 'df_frame'

    'df_transformed' generated by one hot encoding
    categorical features from 'df_frame'.
    '''
    # Obtain original display max_columns
    original = pd.get_option('display.max_columns')
    # print(f'\nmax_columns = {original}')

    # Change display max_columns
    pd.set_option('display.max_columns', 11)
    # current = pd.get_option('display.max_columns')
    # print(f'\nmax_columns = {current}')

    # Change display max_columns via parameter 0 or None)
    # pd.set_option('display.max_columns', 0)
    # current = pd.get_option('display.max_columns')
    # print(f'\nmax_columns = {current}')

    # Extract columns (numeric vs object) from DataFrame 'df_frame'.
    X_numeric = df_frame.select_dtypes(exclude='object')
    X_categoric = df_frame.select_dtypes(include='object')

    print('\ncategoric:')
    display(X_categoric)

    # Initialize the encoder, replacing deprecated
    #   'sparse=False' with 'sparse_output=False.
    # Fit and transform yielding 'enc'.
    enc = OneHotEncoder(
        handle_unknown='ignore', sparse_output=False)
    X_encoded = enc.fit_transform(X_categoric)

    # Get feature names.
    # Convert transformed array to a DataFrame.
    # Create a new DataFrame.
    feature_names = enc.get_feature_names_out(X_categoric.columns)
    df_X_encoded = pd.DataFrame(
        X_encoded, columns=feature_names)

    # df_transformed = pd.concat([X_numeric, df_X_encoded], axis=1)
    df_transformed = pd.concat(
        [X_numeric, df_X_encoded], axis='columns')
    print('\ntransformed:')
    display(df_transformed)

    # Reset display precision to saved value
    pd.set_option('display.max_columns', original)
    # current = pd.get_option('display.max_columns')
    # print(f'\nmax_columns = {current}')
    return X_categoric, df_transformed


def remove_duplicate_columns(df_frame):
    # Locate and remove duplicate columns.
    # '.copy()' used to avoid complaints concerning modification
    # of an existing dataframe.
    # Invert the returned Boolean list.
    print(
        f'\nDuplicate Cols boolean list:\n'
        f'{df_frame.columns.duplicated()}')
    df_new = df_frame.loc[:, ~df_frame.columns.duplicated()].copy()
    print('\nUnique Cols:')
    display(df_new)
    return df_new


def remove_duplicate_rows(df_frame):
    # Locate and remove duplicate rows.
    # '.copy()' used to avoid complaints concerning modification
    # of an existing dataframe.
    # Invert the returned Boolean list.
    print(
        f'\nDuplicate Rows boolean list:\n'
        f'{df_frame.duplicated()}')
    df_new = df_frame.loc[~df_frame.duplicated(), :].copy()
    # Resequence row numbers.
    df_new.index = range(0, len(df_new))
    print('\nUnique Rows:')
    display(df_new)
    return df_new


def rename_columns_inplace(df_frame, columns_dic):
    df_frame.rename(columns=columns_dic, inplace=True)
    return


def rename_columns_not_inplace(df_frame, columns_dic):
    return df_frame.rename(columns=columns_dic, inplace=False)


def set_display_precision(desired_decimal_precision):
    # Force display to use a specific number of decimal digits.
    pd.set_option('display.precision', desired_decimal_precision)
    return
#
# EOF
