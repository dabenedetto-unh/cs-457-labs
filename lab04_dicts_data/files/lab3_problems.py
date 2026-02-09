import json
import os

## STRINGS

def phone_cleaner(phone_list):
    '''
    Take a list of phone numbers in various formats (e.g., `"555-123-4567"`, `"(555) 123 4567"`, `"555.123.4567"`) and 
    return a list of strings containing only the digits.
    '''

def parse_currency(price_strings):
    '''take a list of price strings (with $ and ,) and return a list of floats'''

## DICTS

def unique(categories):
    '''
    take a list of categories and 
    return a list of the unique values
    '''

def frequency_counter(categories):
    '''
    Take a list of categories (e.g., product types or sentiment labels) and 
    return a dictionary where keys are the labels and values are the counts of how often they appear.
    '''

## FILE I/O, data lists

def read_csv(filepath):
    '''
    Read a small `.csv` file (using the standard `open()` and `split(',')` methods) 
    return a list of lists
    '''

def get_col(data,col_num):
    '''
    given a list of lists, get the given col_num
    returns a list
    '''

## Data dicts

def lol_to_lod(rows):
    '''
    given a list of lists, return a list of dicts
    assumes that the first row has the headers.
    returns dict
    '''
