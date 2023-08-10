# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:09:59 2023

@author: myepez
"""

contar=input("Ingrese número a contar: ")
contar=int(contar) 
contador=1
while True:
    print(contador)
    contador+=1
    if contador > contar:  #Esto garantiza que contador se detenga alcanzado el valor buscado
        break