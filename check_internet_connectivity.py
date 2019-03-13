# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:48:54 2018

@author: gao->ilvcr

Description：check internet connectivity use python
"""

__author__ = "yoghourt->gao"


try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
    
def check_internet_connectivity():
    try:
        urllib2.urlopen("http://baidu.com", timeout = 2)
        print("Working connection")
    except urllib2.URLError as E:
        print("Connection error:{}".format(E.reason))
        
        
if __name__ == "__main__":
    check_internet_connectivity()
    
    
    


