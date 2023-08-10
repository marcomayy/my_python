# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:55:16 2023

@author: myepez
"""

#Manejo de errores
#La división para cero no es posible, por tanto causa un error
print("INICIO")
try:
    print("1")
    x=1/0
    print("2")
except:     # este es una declaración de error general
    print("Hay un error")

print("3")
print("FIN")