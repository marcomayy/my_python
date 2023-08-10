# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:43:37 2023

@author: myepez
"""

import numpy as np

unos=np.ones((3,4))
print(unos)
ceros=np.zeros((3,4))
print(ceros)
aleatorios=np.random.random((2,2))
print(aleatorios)

print("")
#Imprimir una matriz 4x4 llena de elementos =100
mt1=np.full((4,4), 100)
print(mt1)

mt3=np.arange(0,30,5)
print(mt3)

a=np.array([(1,2,3,4),
            (3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,2])