# Author: Ron Haber
# Date: 3.1.2021
# This library is to be used for the purposes of reducing the amount of code that I rewrite and copy

import os, sys
import json, csv
import math

def CreateNewDirec(base_direc: str, name: str):
    if(base_direc[-1] == '/' or base_direc[-1] == '\\'):
        base_direc = base_direc[:-1] # will remove the final slash
    new_direc = os.path.join(base_direc, name)
    if(os.path.isdir(new_direc)):
        for f in os.listdir(new_direc):
            os.remove(os.path.join(new_direc, f))
        # return False # Temporary for the purposes of pausing the script
    else:
        os.mkdir(new_direc)
    return new_direc # without the final slash

def UpdateProgress(progress: float, symbol):
    '''If no symbol is present then it can be set to null'''
    bar_length = 25
    status = ""
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(bar_length*progress))
    text = "\rPercent Complete: [{0}] {1}% {2}".format( "#"*block + "-"*(bar_length-block), progress*100, str(symbol), " ",status)
    sys.stdout.write(text)
    sys.stdout.flush()

def WriteDictToCSV(base_direc: str, details, csv_name: str):
    if(base_direc[-1] == '/' or base_direc[-1] == '\\'):
        base_direc = base_direc[:-1] # will remove the final slash
    csv_name = csv_name + '.csv'
    new_csv = os.path.join(base_direc, csv_name)
    data = list(details)
    try:
        keys = data[0].keys()
    except TypeError:
        print("TypeError: the data passed is not of dictionary type.")
        return
    with open(new_csv, 'w') as new_file:
        writer = csv.DictWriter(new_file, keys)
        writer.writeheader()
        writer.writerows(data)
    return new_csv

def CheckIfFileExists(filename: str):
    return os.path.isfile(filename)

def ConvertDictToList(details: dict):
    mid_list = list(details.items())
    output_list = []
    for item in mid_list:
        output_list(item[1]) # This gets the value not the keys
    return output_list

def WriteOrAppendCSV(csv_file: str, details: dict):
    '''If appending then details must be of dict type'''
    if(type(details) != dict):
        raise TypeError("Details must be of dict type")
    if(CheckIfFileExists(csv_file)):
        # Append
        list_to_append = CreateNewDirec(details)
        with open(csv_file, 'a') as old_file:
            writer = csv.writer(old_file)
            writer.writerow(list_to_append)
    else:
        keys = details.keys()
        with open(csv_file, 'w') as new_file:
            writer = csv.DictWriter(new_csv, keys)
            writer.writeheader()
            writer.writerow(details)
    return csv_file

def RoundValueDown(number: float, decimals: int):
    if(decimals == 0):
        return math.floor(number)
    factor = 10 ** decimals
    new_val = math.floor(number * factor)/factor
    return new_val