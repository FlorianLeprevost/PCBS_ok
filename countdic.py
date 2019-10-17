# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:36:01 2019

@author: install
"""
noms=["bob", "bill", "bob", "bill", 'jack', 'joe', 'joe']
countdic = {}
for i in noms:
    if i not in countdic:
        countdic[i]=1
    else:
        countdic[i] +=1
        
print(countdic)
    