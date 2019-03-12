# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:17:48 2017

@author: gao->ilvcr

Description：This will batch rename a group of files in a given directory,
once you pass the current and new extensions
"""

__author__ = "yoghourt->gao"


import os
import argparse

def batch_rename(work_dir, old_ext, new_ext):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    '''
    
    #files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # get the file extension
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # Start of the logic to check the file extensions, if old_ext = file_ext
        if old_ext == file_ext:
            # Returns changed name of the file with new extention
            newfile = split_file[0] + new_ext
            
            #write the file 
            os.rename(
                os.path.join(work_dir, filename)
                os.path.join(work_dir, newfile)
            )
            
            
def get_parse():
    parser = argparse.ArgumentParser(
        description='change extension of files in a working directory'
    )

    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    
    parser.add_argument(
        'old_ext', 
        metavar='OLD_EXT', 
        type=str, 
        nargs=1, 
        help='old extension'
    )
    
    parser.add_argument(
        'new_ext', 
        metavar='NEW_EXT', 
        type=str, 
        nargs=1, 
        help='new extension'
    )
    
    return parser
    
    
def main():
    '''
    This will be called if the script is directly invoked.
    '''
    
    # adding command line argument
    parser = get_parse_args()
    args = vars(parser.parse_args())
    
    # Set the variable work_dir with the first argument passed
    work_dir = args['work_dir'][0]
    # Set the variable old_ext with the second argument passed
    old_ext = args['old_ext'][0]
    
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
        
    # Set the variable new_ext with the third argument passed
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext
    
    batch_rename(work_dir, old_ext, new_ext)
    
if __name__ == '__main__':
    main()
    
    
    
