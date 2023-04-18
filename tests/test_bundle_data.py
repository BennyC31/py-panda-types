import pytest
# import pandas as pd

from pypantypes.bundle_data import bundle_file, bundle_files


def test_bundle_file():
    fpath = '/Users/benc/Projects/public-packages/data/football/test_all.csv'
    concat_df = bundle_file(
        fpath, {'name': 'string', 'amount': 'int64', 'num': 'float'})
    assert len(concat_df) == 8


def test_bundle_file_dtypes():
    fpath = '/Users/benc/Projects/public-packages/data/football/test_all.csv'
    concat_df = bundle_file(
        fpath, {'name': 'string', 'amount': 'int64', 'num': 'float'})
    df_types = [x for x in concat_df.dtypes]
    test_types = ['string', 'Int64', 'Float64']
    assert df_types == test_types


def test_bundle_files():
    file_list = ['/Users/benc/Projects/public-packages/data/football/test.csv',
                 '/Users/benc/Projects/public-packages/data/football/test1.csv',
                 '/Users/benc/Projects/public-packages/data/football/test2.csv',
                 '/Users/benc/Projects/public-packages/data/football/test3.csv']
    concat_df = bundle_files(file_list, {'name': 'string', 'amount': 'int64'})
    assert len(concat_df) == 13


def test_bundle_files_invalid():
    file_list = ['/Users/benc/Projects/public-packages/data/football/test.csv',
                 '/Users/benc/Projects/public-packages/data/football/test1.csv',
                 '/Users/benc/Projects/public-packages/data/football/test2.csv',
                 '/Users/benc/Projects/public-packages/data/football/test2-nohdr.csv',
                 '/Users/benc/Projects/public-packages/data/football/nofile.csv',
                 '/Users/benc/Projects/public-packages/data/football/test_float.csv',
                 '/Users/benc/Projects/public-packages/data/football/test-nodata.csv',
                 '/Users/benc/Projects/public-packages/data/football/test3.csv']
    concat_df = bundle_files(file_list, {'name': 'string', 'amount': 'int64'})
    assert len(concat_df) == 13


def test_bundle_files_dtypes():
    file_list = ['/Users/benc/Projects/public-packages/data/football/test.csv',
                 '/Users/benc/Projects/public-packages/data/football/test1.csv',
                 '/Users/benc/Projects/public-packages/data/football/test2.csv',
                 '/Users/benc/Projects/public-packages/data/football/test3.csv']
    concat_df = bundle_files(file_list, {'name': 'string', 'amount': 'int64'})
    df_types = [str(x) for x in concat_df.dtypes]
    test_types = ['string', 'Int64']
    assert df_types == test_types


def test_bundle_files_games():
    file_list = ['/Users/benc/Projects/public-packages/data/football/game_stats_2010.csv',
                 '/Users/benc/Projects/public-packages/data/football/game_stats_2010_hdrerr.csv',
                 '/Users/benc/Projects/public-packages/data/football/game_stats_2014_dataerr.csv']
    gm_stats = {'Week': 'int64', 'HomeTeam': 'string', 'AwayTeam': 'string', 'Total': 'float', 'H-RushAtt': 'int64', 'H-RushYards': 'int64',
                'H-PassYards': 'int64', 'H-Turnover': 'int64', 'H-Score': 'int64', 'A-RushAtt': 'int64', 'A-RushYards': 'int64',
                'A-PassYards': 'int64', 'A-Turnover': 'int64', 'A-Score': 'int64', 'Result': 'int64'}
    concat_df = bundle_files(file_list, gm_stats)
    assert len(concat_df) == 261


def test_bundle_files_games_dtypes():
    file_list = ['/Users/benc/Projects/public-packages/data/football/game_stats_2010.csv',
                 '/Users/benc/Projects/public-packages/data/football/game_stats_2010_hdrerr.csv',
                 '/Users/benc/Projects/public-packages/data/football/game_stats_2014_dataerr.csv']
    gm_stats = {'Week': 'int64', 'HomeTeam': 'string', 'AwayTeam': 'string', 'Total': 'float', 'H-RushAtt': 'int64', 'H-RushYards': 'int64',
                'H-PassYards': 'int64', 'H-Turnover': 'int64', 'H-Score': 'int64', 'A-RushAtt': 'int64', 'A-RushYards': 'int64',
                'A-PassYards': 'int64', 'A-Turnover': 'int64', 'A-Score': 'int64', 'Result': 'int64'}
    concat_df = bundle_files(file_list, gm_stats)
    df_types = [str(x) for x in concat_df.dtypes]
    test_types = ['Int64', 'string', 'string', 'Float64', 'Int64', 'Int64', 'Int64', 'Int64',
                  'Int64', 'Int64', 'Int64', 'Int64', 'Int64', 'Int64', 'Int64']
    assert df_types == test_types
