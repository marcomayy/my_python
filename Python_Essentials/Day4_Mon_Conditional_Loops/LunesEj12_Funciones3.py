# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:59:13 2023

@author: myepez
"""

def direccion(ciudad,barrio,calle):
    print("La dirección de entrega es: ")
    print("La ciudad es: ",ciudad)
    print("El barrio es: ",barrio)
    print("Y la calle es: ",calle)

ci=input("Ingrese la ciudad de entrega: ")
ca=input("Ingrese la calle de referencia: ")
ba=input("Ingrese el barrio:")
direccion(ci,ba,ca)