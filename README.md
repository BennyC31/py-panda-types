# PyPanda Types
Reads csv files with same headers, concatenates the data into one data frame and preserves the data types.

## Requirements
* CSV files only
* Pass one or list of csv files and column headers with data types

## Processing
* Reads csv files
* Validates files exist
* Validates column headers are the same for all files
* Concatenates the data into one DataFrame.
* Keeps the data types passed in

## Version
0.0.1

## Authors
Benjamin Calderaio, Jr.

## License
MIT License

## Available on Test PyPi
(https://test.pypi.org/project/py-panda-types/0.0.1/)

## Install
pip install -i https://test.pypi.org/simple/ py-panda-types==0.0.1

## Usage Example
import pypantypes.bundle_data as bd
### Single file
file_name = '/dir1/onedatafile.csv'
column_headers = {'col1':'int64','col2':'string'}

df = bd.bundle_file(file_list,column_headers)

### Multiple files
file_list = ['/dir1/data1.csv','/dir1/data2.csv']
column_headers = {'col1':'int64','col2':'string','col3':'float'}

df = bd.bundle_files(file_list,column_headers)
