# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:31:57 2017

@author: gao->ilvcr

Description：A simple program illustrating chaotic behaviour
"""

__author__ = "yoghourt->gao"


def main():
    
    print("This program illustrating chaotic behaviour")
    
    whilr True:
        try:
            x = float((input("Enter a number between 0 and 1: ")))
            if(0 < x and x < 1):
                break
            else:
                print("Please enter correct number")
        except Exception as e:
            print("Please enter correct number")
            
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
        
        
if __name__ == '__main__':
    main()


