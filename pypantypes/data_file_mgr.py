"""
Validates the files exist and stores the 
file paths in a collection for processing.

Author: Benjamin Calderaio, Jr.
Date: April 14, 2023

"""
import os
# import logging as lg

# lg.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=lg.CRITICAL)


def get_file(fpath: str):
    """
    Validate file exists and returns file.

    Parameters:
        fpath (str) File to validate and use.

    Returns:
        str: The file path.
    """
    try:
        if (os.path.isfile(fpath)):
            return fpath
        else:
            raise FileNotFoundError(f'File {fpath} not found!')
    except FileNotFoundError as e:
        # lg.error(f'get_file: {e}')
        raise


def get_files(file_list: list):
    """
    Validate file list and returns list of files.

    Parameters:
        file_list (list) File list to validate and use.

    Returns:
        list: The files found to be used for processeing.
        list: The files not found.
    """
    files_exist = []
    files_not_exist = []
    for i in range(len(file_list)):
        try:
            if (os.path.isfile(file_list[i])):
                files_exist.append(file_list[i])
            else:
                files_not_exist.append(file_list[i])
        except Exception as e:
            # lg.error(f'get_files: {e}')
            print(e)
    return files_exist, files_not_exist
