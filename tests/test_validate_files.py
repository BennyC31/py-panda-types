import pytest

from pypantypes.validate_files import validate_csv_files


def test_validate_csv_files_all_valid():
    file_list = ['/Users/benc/Projects/public-packages/data/football/test.csv',
                 '/Users/benc/Projects/public-packages/data/football/test1.csv',
                 '/Users/benc/Projects/public-packages/data/football/test2.csv',
                 '/Users/benc/Projects/public-packages/data/football/test3.csv']
    valid_files, invalid_files = validate_csv_files(
        file_list, {'name': 'string', 'amount': 'int64'})
    assert len(valid_files) == 4
    assert len(invalid_files) == 0


def test_validate_csv_files_mixed_valid():
    file_list = ['/Users/benc/Projects/public-packages/data/football/test.csv',
                 '/Users/benc/Projects/public-packages/data/football/test1.csv',
                 '/Users/benc/Projects/public-packages/data/football/test2-nohdr.csv',
                 '/Users/benc/Projects/public-packages/data/football/test3.csv']
    valid_files, invalid_files = validate_csv_files(
        file_list, {'name': 'string', 'amount': 'int64'})
    assert len(valid_files) == 3
    assert len(invalid_files) == 1


def test_validate_csv_files_list_error():
    file_list = '/Users/benc/Projects/public-packages/data/football/test.csv'
    with pytest.raises(TypeError, match=r'File list is not a list!'):
        validate_csv_files(file_list, {'name': 'string', 'amount': 'int64'})


def test_validate_csv_files_dict_error():
    file_list = ['/Users/benc/Projects/public-packages/data/football/test.csv']
    with pytest.raises(TypeError, match=r'Column headers are not a dict!'):
        validate_csv_files(file_list, ['name', 'amount'])
