# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:15:23 2021

@author: Sarah Anne Pedersen
"""
import math

def merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r-q
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    
    for i in range(n1): 
        L[i] = array[ p + i ]
        
    for j in range(n2):
        R[j] = array[ q + j + 1 ]
    L[n1] = float("inf")
    R[n2] = float("inf")    
    i = 0
    j = 0
    print(L,R)
    
    for k in range(p,r + 1):
        print("comparing", L[i], R[j])
        if L[i]<=R[j]:
            print("choosing", L[i])
            array[k] = L[i]
            i = i + 1
        else: 
            print("choosing", R[j])
            array[k] = R[j]
            j = j + 1
            


asd = [8,12,16,7,9,11]

print(asd)
# merge(asd, 0, math.floor(len(asd)/2), len(asd) - 1)
merge(asd, 0, 2, 5)
print(asd)