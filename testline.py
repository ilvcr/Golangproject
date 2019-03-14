# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:41:44 2017

@author: gao->ilvcr

Description：This is a very simple script that opens up 
             a file and writes whatever is set "
"""

__author__ = "yoghourt->gao"


def write_to_file(filename, txt):
    with open(filename, 'w') as file_object:
        s = file_object.write(txt)
        
if __name__ == '__main__':
    write_to_file('test.txt', 'I am beven')


