# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:44:36 2017

@author: gao->ilvcr

Description：start server
"""

__author__ = "yoghourt->gao"


from __future__ import print_function
import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()






