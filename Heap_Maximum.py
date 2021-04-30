# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:56:04 2021

@author: Sarah Anne Pedersen
"""

#%%

def parent(i):
    
    return int((i-1)/2)

#%% Left
def left(i):
    
    return 2*i+1

#%% Right
def right(i):
    
    return 2*i+2

#%% Return empty list
def createEmptyPQ():
    
    l = []
    
    return l
#%%

def extract_min(A): 
    min_element = A[0]
    A[0] = A[-1] 
    A.pop() 
    minHeapify(A,0)
    return min_element 
    
#%%

def minHeapify(A,i):
    
    l = left(i)
    r = right(i)
    
    if l <= len(A)-1 and A[l] < A[i]:
        smallest = l
        
    else:
        smallest = i
        
    if r <= len(A)-1 and A[r] < A[smallest]:
        smallest = r
        
    if smallest != i:
        print(f"Im i: {i}")
        A[i], A[smallest] = A[smallest], A[i]
        minHeapify(A, smallest)

#%%        
def insert(A, e):
    #A.len(A) = A.len(A) + 1
    i = len(A)
    A.append(e)
    while i > 0 and A[PARENT(i)] > A[i]:
        A[i], A[PARENT(i)] = A[PARENT(i)], A[i]
        i = PARENT(i)