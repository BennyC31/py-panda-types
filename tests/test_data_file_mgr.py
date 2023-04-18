import pytest

from pypantypes.data_file_mgr import get_file, get_files


def test_get_file():
    fpath = '/Users/benc/Projects/public-packages/data/football/game_stats_2010.csv'
    assert get_file(fpath) == fpath


def test_get_file_fail():
    fpath = '/Users/benc/Projects/public-packages/data/football/game_stats_20101.csv'
    with pytest.raises(FileNotFoundError, match=r'File /Users/benc/Projects/public-packages/data/football/game_stats_20101.csv not found!'):
        get_file(fpath)


def test_get_files():
    file_lst = ['/Users/benc/Projects/public-packages/data/football/game_stats_2010.csv',
                '/Users/benc/Projects/public-packages/data/football/game_stats_2011.csv',
                '/Users/benc/Projects/public-packages/data/football/game_stats_2015.csv']
    good_lst, error_list = get_files(file_lst)
    assert len(good_lst) == 3
    assert len(error_list) == 0


def test_get_files_diff():
    file_lst = ['/Users/benc/Projects/public-packages/data/football/game_stats_2010.csv',
                '/Users/benc/Projects/public-packages/data/football/game_stats_20101.csv',
                '/Users/benc/Projects/public-packages/data/football/game_stats_2018.csv']
    good_lst, error_list = get_files(file_lst)
    assert len(good_lst) == 2
    assert len(error_list) == 1
