# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:08:36 2023

@author: myepez
"""

#fname=input("Ingrese su primer nombre: ")
#lname=input("Ingrese su apellido: ")
#location=input("Ingrese su ubicación: ")
#age=input("Ingrese su edad: ")
age=int(input("Ingrese su edad: "))
#space=("")
#print(fname,lname,",",space,"located in",space,location,"at the age of",age)
if age >= 70:
    print("Persona mayor de edad")
elif age >=30:
    print("Persona adulta maduro")
elif age >=18:
    print("Persona es adulto jóven")
elif age >=13:
    print("Persona es adolescente")
elif age >=10:
    print("Persona en etapa de pubertad")
elif age >=3:
    print("Persona es niño")
elif age >>2:
    print("Persona es bebé")
elif age >=0:
    print("Persona es recién nacida")