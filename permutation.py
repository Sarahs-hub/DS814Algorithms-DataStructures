# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 17:24:14 2021

@author: Sarah Anne Pedersen
"""
import random 

def perm(n): 
    l=[]
    for i in range(n):
        l.append(i)
    random.shuffle(l)
    return l 
    
def cycles(l):
    cyc = 0 
    check = set()
    for i in range(l): 
        j = i
        while j not in check: 
            next_number=l[j]
            check.add(j)
            j = next_number
            if j == i: 
                cyc += 1
    return cyc 