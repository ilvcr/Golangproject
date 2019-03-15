# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:29:43 2018

@author: gao->ilvcr

Description： Runs checks to check my SQLITE database
"""

__author__ = "yoghourt->gao"



import sqlite3 as lite
import sys
import os

dropbox = os.getenv("dropbox")
dbfile = ("Databases\jarvis.db")
master_db = os.path.join(dropbox, dbfile)
con = None

try:
    con = lite.connect(master_db)
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print("SQLITE version: {}".format(data))
    
except lite.Error as e:
    print("Error {}:".format(e.args[0]))
    sys.exit(1)
finally:
    if con:
        con.close()
        
        
con = lite.connect(master_db)
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
rows = cur.fetchall()
for row in rows:
    print(row)
    
con = lite.connect(master_db)
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
while True:
    row = cur.fetchone()
    if row == None:
        break
    print(row[0])






