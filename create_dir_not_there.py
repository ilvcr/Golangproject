# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:01:13 2017

@author: gao->ilvcr

Description：Checks to see if a directory exists in the users home directory, 
             if not then create it
"""

__author__ = "yoghourt->gao"


import os

MESSAGE = "The directory already exists."
TESTDIR = 'testdir'

try:
    # Set the variable home by expanding the user's set home directory
    home = os.path.expanduser("~")
    print(home) # print the location
    
    
    # os.path.join() for making a full path safely
    if not os.path.exists(os.path.join(home, TESTDIR)):
        # If not create the directory, inside their home directory
        os.makedirs(os.path.join(home, TESTDIR))
    else:
        print(MESSAGE)
except Exception as e:
    print(e)



