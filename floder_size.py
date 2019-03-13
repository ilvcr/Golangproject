# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:06:26 2017

@author: gao->ilvcr

Description：This will scan the current directory and 
             all subdirectories and display the size.
"""

__author__ = "yoghourt->gao"

import os
import sys
try:
    #Set the variable directory to be the argument supplied by user.
    directory = sys.argv[1]
except IndexError:
    sys.exit("Must provide an argument.")
    
dir_size = 0 # Set the size to 0


fsizedicr = {'Bytes': 1,
             'Kilobytes': float(1) / 1024,
             'Megabytes': float(1) / (1024 * 1024),
             'Gigabytes': float(1) / (1024 * 1024 * 1024)
}

# Walk through all the directories. For each iteration, os.walk returns the folders, subfolders and files in the dir.
for (path, dirs, files) in os.walk(directory):     
    # Get all the files    
    for file in files:                              
        filename = os.path.join(path, file)
        # Add the size of each file in the root dir to get the total size.
        dir_size += os.path.getsize(filename)       
        
fsizeList = [str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr] # List of units

# Sanity check to eliminate corner-case of empty file.
if dir_size == 0: 
    print ("File Empty") 
else:
    # Reverse sort list of units so smallest magnitude units print first.
    for units in sorted(fsizeList)[::-1]: 
        print ("Folder Size: " + units)


