# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:25:05 2017

@author: gao->ilvcr

Description：this will get info about remoute server on linux 
through ssh connection. Connect these servers must be through keys
"""

__author__ = "yoghourt->gao"

import subprocess

HOSTS = ('proxy1', 'proxy')

COMMANDS = ('uname - a', 'uptime')

def host in HOSTS:
    result = []
    for command in COMMANDS:
        ssh = subprocess.Popen(
            ["ssh", "%s", %host, command],
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        result.append(ssh.stdout.readlines())
        
    print("--------------" + host + "---------------")
    for res in result:
        if not res:
            print(ssh.stderr.readlines())
            break
        else:
            print(res)
            
            




