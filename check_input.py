# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:41:13 2019

@author: gao->ilvcr

Description：reads from command-line a integer in the given bounds. 
while input invalid asks user again
"""

__author__ = "yoghourt->gao"


def get_user_input(start, end):
    '''
        input: two integer values
               lower limit 'start' and maximum 'end'
               the arguments aren't inclusive.

        output: if reading successful then returns the read integer.
    '''
    loop = True
    while loop:
        try:
            #reads and converts the input from the console.
            user_input = int(input("Enter Your choice: "))
            
            #checks whether input is in the given bounds.
            if user_input > end or user_input < start:
                #error case
                print("Please try again. Not in valid bounds.")
            else:
                #valid cse
                loop = False #aborts while-loop
        except ValueError:
            #error case
        print("PLS try again, Only numbers")
    return user_input
    
if __name__ == '__main__':
    x = get_user_input(1, 6)
    print(x)
    

# Asks user to enter something, ie. a number option from a menu.
# While type != interger, and not in the given range,
# Program gives error message and asks for new input.