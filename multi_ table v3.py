# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:40:16 2019

@author: install
"""
import random
list_test = [1,2,3]
list_random = [random.randint(1,10) for i in range(10)]

def sum_nb(x):
    print(sum(x))
    
def sum_sq(x):
    print(sum( [i*i for i in list_test]))

def max_nb(x):
    print(max(x))
    
def table():
    chiffres = list(range(1,10))
    for i in chiffres:
        list2 = [str(i)+"x"+str(k)+"="+str(i*k) for k in chiffres]
        print('{:7} {:7} {:7} {:7} {:7} {:7} {:7} {:7} {:7} '.format(*list2))
        
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
        ligne_sup = triangle[-1]
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
    espace = '{:4} '
    espace_ligne =[]
    for ligne in triangle:
        espace_ligne =[]
        espace_form =""
        for nb in ligne:
            espace_ligne.append(espace)
            espace_form= "".join(espace_ligne)
        print(espace_form.format(*ligne))


def triangle_bon_sens(n) :
    triangle = triangle_pascal(n)
    nv_triangle = []
    for lg_li in range(n):
        nv_li=[]
        for elmt in range(lg_li):
            nv_li.append(triangle[lg_li-elmt][elmt])    #selectione dans autre triangle quel elemt ajouter
        nv_li.append(1)
        nv_triangle.append(nv_li)
    for i in range(n):
        print(nv_triangle[i])