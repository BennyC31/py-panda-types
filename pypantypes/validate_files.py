"""
Validates the files have the same headers
and prepares them for processing.

Author: Benjamin Calderaio, Jr.
Date: April 15, 2023

"""
import pandas as pd
import logging as lg

lg.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=lg.CRITICAL)


def validate_csv_files(file_list: list, column_headers: dict):
    """
    Validates column headers are the same for each file.

    Parameters:
        file_list (list) List of files to validate.
        column_headers (dict) Column headers dictionary to validate.

    Returns:
        list: The valid files to be used for processeing.
        list: The files not to be used.
    """
    try:
        valid_files = []
        invalid_files = []
        if type(file_list) != list:
            raise TypeError(f'File list is not a list!')
        elif type(column_headers) != dict:
            raise TypeError(f'Column headers are not a dict!')

        hdrs = list(column_headers.keys())
        __handle_files(file_list, hdrs, valid_files, invalid_files)
    except TypeError as e:
        lg.error(f'validate_csv_files TypeError: {e}')
        raise
    except Exception as e:
        lg.error(f'validate_csv_files Exception: {e}')

    return valid_files, invalid_files


def __handle_files(file_list: list, hdrs: list, valid_files: list, invalid_files: list):
    for i in range(len(file_list)):
        try:
            csv_file_df = pd.read_csv(file_list[i])
            cols = list(csv_file_df.columns)
            if cols == hdrs:
                valid_files.append(file_list[i])
            else:
                invalid_files.append(file_list[i])
        except Exception as e:
            lg.error(f'File Exception: {file_list[i]}')
            invalid_files.append(file_list[i])
