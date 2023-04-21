"""
Bundles the data files into a pandas data frame
and preserves the data types.

Author: Benjamin Calderaio, Jr.
Date: April 17, 2023

"""
import pandas as pd
import logging as lg
# from pypantypes.data_file_mgr import get_files, get_file
# from pypantypes.validate_files import validate_csv_files
from .data_file_mgr import get_files, get_file
from .validate_files import validate_csv_files

lg.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=lg.CRITICAL)


def clean_data(concat_df, column_headers):
    """
    Cleans data frame columns and preserves data types.

    Parameters:
        concat_df (pd.DataFrame) Data frame to clean.
        column_headers (dict) Column headers dictionary to validate.

    Returns:
        pd.DataFrame: Data Frame to be used for processeing.
    """
    try:
        for k, v in column_headers.items():
            if (v == 'float'):
                s2 = pd.Series(concat_df[k])
                s2 = pd.to_numeric(s2, errors='coerce').astype('Float64')
                concat_df[k] = s2
            elif (v == 'int64'):
                s1 = pd.Series(concat_df[k])
                s1 = pd.to_numeric(s1, errors='coerce').astype('Int64')
                concat_df[k] = s1

        concat_df = concat_df.convert_dtypes()
    except Exception as e:
        lg.error(f'clean_data: {e}')
    return concat_df


def bundle_file(fpath: str, column_headers: dict):
    """
    Concatenates data file into one data frame.

    Parameters:
        fpath (str) File to validate and use.
        column_headers (dict) Column headers dictionary to validate.

    Returns:
        pd.DataFrame: Data Frame to be used for processeing.
    """
    concat_df = pd.DataFrame()
    try:
        concat_df = bundle_files([get_file(fpath)], column_headers)
    except Exception as e:
        lg.error(f'bundle_file: {e}')
    return concat_df


def bundle_files(file_list: list, column_headers: dict):
    """
    Concatenates data files into one data frame.

    Parameters:
        file_list (list) List of files to validate.
        column_headers (dict) Column headers dictionary to validate.

    Returns:
        pd.DataFrame: Data Frame to be used for processeing.
    """
    files_exist, files_not_found = get_files(file_list)
    valid_files, invalid_files = validate_csv_files(
        files_exist, column_headers)
    lst_dfs = []
    dict_errs = {}
    for i in range(len(valid_files)):
        try:
            file_df = pd.read_csv(valid_files[i])
            lst_dfs.append(file_df)
        except Exception as e:
            dict_errs[valid_files[i]] = f'Error:{e}'
    lg.warning(f'File append errors: {dict_errs}')
    lg.warning(f'Invalid files: {invalid_files}')
    lg.warning(f'Files not found: {files_not_found}')

    concat_df = pd.concat(lst_dfs)
    concat_df = concat_df.convert_dtypes()
    concat_df = concat_df.reset_index(drop=True)
    concat_df = clean_data(concat_df, column_headers)
    lg.info(concat_df.head())
    lg.info(f'rows={len(concat_df)}')
    # print(f'dtypes:\n{concat_df.dtypes}')
    lg.info(f'dtypes:\n{concat_df.dtypes}')
    return concat_df
