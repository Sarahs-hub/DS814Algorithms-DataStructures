# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 14:56:17 2021

@author: Sarah Anne Pedersen
"""
# Returnerer true hvis nøglen findes og false hvis nøglen ikke findes 
def search(T,k):
    return find(T[0], k)
    
#Arbejdende rekursive funktion som undersøger hver knude isoleret  
def find(node,k): 
    if node == None: 
        return False 
    else: 
        #Nøglen fundet
        if node[0] == k: 
            return True
        #Kigger mod venstre
        elif node[0]>k:
            return find(node[1],k)
        #Kigger mod højre
        else:
            return find(node[2],k)
               
# Sætter nøgle ind på rodens plads ellers kalder addNode for at finde rette plads     
def insert(T,k):
    root = T[0]
    if root == None: 
        T[0] = [k, None, None]
    else: 
        addNode(root,k)
    
#Arbejdende rekursive funktion som undersøger hvor nøglen skal indsættes      
def addNode(node,k):
    # Kig mod højre
    if k>node[0]:
        #Indsætter nøgle på højre barn
        if node[2] == None: 
            node[2] = [k,None,None]
        #Forsætter til højre ned gennem træet
        else: 
            addNode(node[2],k)
    # Kig mod venstre
    elif k <= node[0]: 
        # Indsætter nøgle på venstre barn
        if node[1]== None:
            node[1] = [k,None,None]
        #Forsætter til venstre ned gennem træet
        else: 
            addNode(node[1],k)
    
        
    
# Returnerer sorteret liste af træets indhold 
def orderedTraversal(T):
    return traversal(T[0]) 

#Arbejdende rekursive funktion som sorterer knude fra venstre til højre    
def traversal(node): 
    #Hvis knuden er tom returneres tom liste
    if node == None: 
        return []
    else: 
        # Liste kun indehold knudens nøgle
        parent = [node[0]]
        # Sorteret liste for venstre underdel af træet
        left = traversal(node[1])
        # Sorteret liste for højre underdel af træet
        right = traversal(node[2])
        return left + parent + right  
    
        
    

# Laver nyt tomt træ    
def createEmptyDict():
    return [None]





#tree = createEmptyDict()
#insert(tree,5)
#insert(tree,3)
#insert(tree,7)
#insert(tree,6)
#insert(tree,5)

#print(tree)
#print(orderedTraversal(tree))
#print(search(tree,6))
#print(search(tree,2))


