import re
import pandas as pd
import numpy as np
from functools import reduce

import put_readings

def check_readings(readings):
    """
    Check the reading for a particular day on which the values are clubbed together without any delimeted space
    If found, split_keep_delimeter function is called.
    takes in the list with less than 24 hours values
    """
    templist = []
    for reading in readings:
        if reading.count('-') > 1:
            temp_2 = list(split_keep_delimeter(reading))
            templist = templist + temp_2
        else:
            templist.append(reading)
    return np.array(templist).astype(np.float)


def split_keep_delimeter(negative_list):
    """
    Splits and keeps the deilmeter to take into account of the values that are clubbed together
    Takes in the the a string values and splis it by -
    """
    malformed_list = reduce(lambda acc, elem: acc[:-1] + [elem + acc[-1]] if elem == "-" else acc + [elem], re.split("(-)", negative_list), [])
    malformed_list.pop(0)
    converted_list = np.array(malformed_list).astype(np.float)
    converted_list[-1] = -1 * converted_list[-1]
    return converted_list


def get_readings_array(df, year, month, put_to_database=False):
    """
    Requres a dataframe object containing the readings.
    Converts the dataframe values to numpy floats 
    """
    for i in range(5, len(df)):
        readings = df.iloc[i][0].split()
        day = readings.pop(0)
        if len(readings) == 24: #values for whole day. Delimeted by space
            final_readings = np.array(readings).astype(np.float)
        else: # values that are clubbed together by multiple "-"
            final_readings = check_readings(readings)
        if put_to_database:
            put_readings.push_to_db(year, month, day, final_readings)
        print(day, ": ", list(final_readings))

def get_dataframe(filename):
    df = pd.read_csv(filename)
    return df

if __name__ == "__main__":
    df = pd.read_csv("temp_copy.txt")
    get_readings_array(df, 1957, 12, put_to_database=True)
