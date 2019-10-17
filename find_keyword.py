# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:20:18 2019

@author: install
"""
import sys
with open(sys.argv[1]) as file:
    compt=1
    for line in file:
        line = line.lower()
        list_line = line.split(" ")
        if "cogmaster" in list_line:
            print(line)
