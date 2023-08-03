# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:59:40 2023

@author: myepez
"""
#Uso de comando ELIF
acl=int(input("Ingrese el # de ACL: "))
if acl >= 1 and acl <= 99:
    print("Es una ACL estándar")
elif acl >= 100 and acl <= 199:    #Elif actúa con el valor de "FALSO" del IF
    print("Es una ACL Extendida")
else:
    print("El # ingresado no es una ACL")