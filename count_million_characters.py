# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:56:21 2017

@author: gao->ilvcr

Description：Get the number of each character in any given text.
"""

__author__ = "yoghourt->gao"


import pprint
import collections

def count_million_characters():
    '''
        Inputs:
            A txt file -- You will be asked for an input file. Simply input the name
            of the txt file in which you have the desired text.
    '''
    file_input = input("File Name: ")
    try:
        with open(file_input, 'r') as info:
            count = collections.Counter(info.read().upper())
    except FileNotFoundError:
        print("PLS enter a valid file name.")
        count_million_characters()
        
        

if __name__ == '__main__':
    count_million_characters()
    



