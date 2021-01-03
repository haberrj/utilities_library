# Author: Ron Haber
# Date: 3.1.2021
# Tests for functions in the library where possible

from haber_utils import utils

def test_CheckIfFileExists():
    assert utils.CheckIfFileExists('__init__.py') == True
    assert utils.CheckIfFileExists('blank.txt') == False

def test_ConvertDictToList():
    sample_dict = {
        'a':1,
        'b':2
    }
    test_list = [1,2]
    assert utils.ConvertDictToList(sample_dict) == test_list

def test_RoundValueDown():
    starting = 1.23456789
    end = 1.23456
    decimals = 5
    assert utils.RoundValueDown(starting, decimals) == end
