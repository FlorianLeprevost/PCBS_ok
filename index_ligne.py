# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:20:18 2019

@author: install
"""
import sys
with open(sys.argv[1]) as file:
    compt=1
    for line in file:
        print(compt, " ", line)
        compt+=1