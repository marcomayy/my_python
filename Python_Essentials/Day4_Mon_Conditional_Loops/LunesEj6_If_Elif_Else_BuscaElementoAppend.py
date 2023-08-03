# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:48:56 2023

@author: myepez
"""
listar_R=[]
listar_S=[]
listar_AP=[]
listar_FW=[]
listar_Va=[]
lista=["R1","R2","R3",
       "S1","S2","S3",
       "AP1","AP2","AP3",
       "FW2","PC1","PC2"]
for elemento in lista:
    if "R" in elemento:
        print(elemento)
        listar_R.append(elemento)
        
    elif "S" in elemento:
        print(elemento)
        listar_S.append(elemento)
        
    elif "AP" in elemento:
        print(elemento)
        listar_AP.append(elemento)
        
    else:
        print(elemento)
        listar_Va.append(elemento)
        
print("Router: ",listar_R)
print("Switch: ",listar_S)
print("Ac Pnt: ",listar_AP)
print("Varios: ",listar_Va)
