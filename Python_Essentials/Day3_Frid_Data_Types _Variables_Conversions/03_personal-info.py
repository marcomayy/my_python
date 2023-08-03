# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 20:34:19 2023

@author: myepez
"""

fname=input("Ingrese su primer nombre: ")
lname=input("Ingrese su apellido: ")
location=input("Ingrese su ubicación: ")
age=str(input("Ingrese su edad: ")) #Convierto integer a string para el uso en print
space=(" ")
print(fname,lname +"," +space +"located in" +space +location +" at the age of " +age)