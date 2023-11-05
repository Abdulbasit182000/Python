# MyCLIProject

**Table of Contents**
- [Introduction](#introduction)
- [Installation](#installation)
- [Key Arguments](#key-arguments)
- [Usage](#usage)
- [Examples](#examples)
- [Error Handling](#error-handling)

## Introduction

MyCLIProject is a command-line tool designed to manipulate DataFrames based on user input. It leverages the argparse library to provide a versatile interface for data analysis and processing.

## Installation

Before using MyCLIProject, you need to install the required Python packages, `argparse` and `pandas`, on your system. You can do this using `pip`, the Python package manager. If you don't have Python installed, please download and install it from the [official Python website](https://www.python.org/downloads/) first.

1. **Python Installation**: If you haven't already installed Python, download the latest version from the [official Python website](https://www.python.org/downloads/).

2. **Install Dependencies**:
   Open your terminal and navigate to your project directory. Then, run the following command to install the required dependencies:

   ```bash
   pip install argparse pandas


## Key Arguments

MyCLIProject accepts the following key arguments:

1. **--file**: This argument is mandatory and is used to specify the input CSV file. The file should have a .csv extension.
   - **Error Handling**: If the `--file` argument is omitted, you'll receive an error message: "Please provide the --file argument with the path to your CSV file."

2. **--range**: (Optional) Specify a date range to filter the data. Use the format "YYYY-MM-DD to YYYY-MM-DD."
   - **Error Handling**: If the `--range` argument is specified with an invalid date range format, you'll see: "Invalid date range format. Please use 'YYYY-MM-DD to YYYY-MM-DD.'"

3. **--max**: Retrieve the maximum value for a specified column.
   - **Error Handling**: If you attempt to use multiple operation arguments such as `--max` and `--mean` together, you'll be advised: "Please use only one of --max, --min, or --mean."

4. **--min**: Retrieve the minimum value for a specified column.

5. **--mean**: Calculate the mean value for the specified column.
   - **Error Handling**: If you use the `--mean` argument without specifying columns to print using `--pr`, you'll be alerted: "Please specify the columns to print using the --pr argument."

6. **--column**: Specify the column where operations are to be performed.
   - **Error Handling**: If the `--column` argument specifies a column name that does not exist in the CSV file, you'll be informed: "The column name specified is not found in the DataFrame."

7. **--pr**: Choose specific columns to print.
   - **Error Handling**: If you use the `--pr` argument without specifying any columns, you'll see: "Please specify the columns to print using the --pr argument."

8. **--export**: Provide a file name to export the results of your operations.
   - **Error Handling**: If the provided file does not have the .csv extension, you'll receive an error: "Please provide a CSV file with the .csv extension."


#Usage

To use MyCLIProject, open your terminal, navigate to the project directory, and run the following command to display available options the file that i am using is `Args.py`:

      $ python Args.py -h

#Examples

Here are some examples of how to use MyCLIProject and their explanations:


Example: Print specific columns from the `weather_1.csv` file.

     $ python Args.py --file weather_1.csv --pr "Data.Temperature.MinTemp,Data.Temperature.MaxTemp,Data.Wind.Direction,Data.Wind.Speed"

Example: Print specific columns with a `date range` filter.
      
      $ python Args.py --file weather_1.csv --pr "Date.Full,Data.Temperature.MinTemp,Data.Temperature.MaxTemp,Data.Wind.Direction,Data.Wind.Speed" --range "2016-01-03 to 2017-01-03"

Example: Calculate the `mean` of specified columns and print them.
      
      $ python Args.py --file weather_1.csv --mean --pr "Data.Temperature.MinTemp,Data.Temperature.MaxTemp,Data.Wind.Direction,Data.Wind.Speed"

Example: Calculate the mean and export the table to a file named `v.csv`

      $ python Args.py --file weather_1.csv --mean --pr "Data.Temperature.MaxTemp,Data.Temperature.MinTemp" --export v.csv

Example: Find the maximum value of "Data.Temperature.MaxTemp" and print associated columns within a specified date range.


      $ python Args.py --file weather_1.csv --column Data.Temperature.MaxTemp --max --pr "Date.Weekof,Date.Full" --range "2016-01-03 to 2016-05-06"

Example: Print the maximum value of "Data.Temperature.MaxTemp."

     $ python Args.py --file weather_1.csv --column Data.Temperature.MaxTemp --max

#Error Handling

MyCLIProject includes robust error handling to guide users when issues arise:

1. **Missing Required File Argument**:
   - **Error Message**: If the `--file` argument is omitted, you'll receive an error message: "Please provide the --file argument with the path to your CSV file."

2. **Invalid Date Range Format**:
   - **Error Message**: If the `--range` argument is specified with an invalid date range format, you'll see: "Invalid date range format. Please use 'YYYY-MM-DD to YYYY-MM-DD'."

3. **File Not Found**:
   - **Error Message**: If the specified CSV file doesn't exist in the provided path, you'll get: "The file 'your_file.csv' was not found. Please ensure the file exists and provide the correct path."

4. **Invalid Column Name**:
   - **Error Message**: If the `--column` argument specifies a column name that does not exist in the CSV file, you'll be alerted with: "The column name specified is not found in the DataFrame."

5. **Invalid Operation Combination**:
   - **Error Message**: If you attempt to use multiple operation arguments such as `--max` and `--mean` together, you'll be advised: "Please use only one of --max, --min, or --mean."

6. **File Format Mismatch**:
   - **Error Message**: If the provided file does not have the .csv extension, you'll receive an error: "Please provide a CSV file with the .csv extension."

7. **Date Range Misalignment**:
   - **Error Message**: If the specified date range does not align with the data in the CSV file, you'll be informed: "The specified date range does not align with the available data."

8. **No Column for Printing**:
   - **Error Message**: If you use the `--pr` argument without specifying any columns, you'll see: "Please specify the columns to print using the --pr argument."

These error messages will help you troubleshoot and resolve issues that may arise during the usage of MyCLIProject.
