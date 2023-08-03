# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:30:14 2023

@author: myepez
"""

listar=[]
lista=["R1","R2","R3",
       "S1","S2","S3",
       "AP1","AP2","AP3",
       "FW2","PC1","PC2"]
for elemento in lista:
    if "R" in elemento:
        print(elemento)
        listar.append(elemento)
print(listar)