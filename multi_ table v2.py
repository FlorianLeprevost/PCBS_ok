# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:40:16 2019

@author: install
"""
list_test = [1,2,3]

def sum_nb(x):
    print(sum(x))
    
def sum_sq(x):
    print(sum( [i*i for i in list_test]))

def max_nb(x):
    print(max(x))
    
def table():
    chiffres = [1,2,3,4,5,6,7,8,9]
    for i in chiffres:
        list2 = [str(i*k) for k in chiffres]
        print('{:3} {:3} {:3} {:3} {:3} {:3} {:3} {:3} {:3} '.format(*list2))
        
def triangle_pascal(n):
    triangle = []
    ligne=[]
    for i in range(n):
        ligne.append(1)
    triangle.append(ligne)
    
    ligne=[]
    for i in range(n-1):
         ligne.append(i+1)
    triangle.append(ligne)
    
    n=n-2
    while n > 0:
        ligne = []
        ligne_sup = triangle[n-n-1]
        for i in range(n):
            if i-1 >= 0:
                ligne.append(ligne[i-1]+ligne_sup[i])
            else :
                ligne.append(1)

            
        triangle.append(ligne)
        n=n-1
    
    return(triangle)

def triangle_beau(n):
    triangle = triangle_pascal(n)
    espace = '{:3} '
    espace_ligne =[]
    for ligne in triangle:
        espace_form =""
        for nb in ligne:
            espace_ligne.append(espace)
            espace_form= "".join(espace_ligne)
        print(espace_form)
        print(espace_form.format(*ligne))
    
            
