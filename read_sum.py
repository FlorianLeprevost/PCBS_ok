# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:42:29 2019

@author: install
"""

import sys
somme=0
with open(sys.argv[1]) as file:
    for line in file:
        somme+= int(line)
        
    print(somme)
    
         