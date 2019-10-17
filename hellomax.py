# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:36:14 2019

@author: install
"""

with open("hello.txt", "a") as file:
    file.write("\nHello world!")
    file.close    

with open("hello.txt", "r") as file:
    print(file.read())