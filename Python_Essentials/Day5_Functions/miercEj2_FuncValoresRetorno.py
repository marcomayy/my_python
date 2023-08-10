# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:50:59 2023

@author: myepez
"""

def multiply(a=5,b=3):
    print("El resultado de multiplicar ",a," por ",b," es: ")
    print(a*b)
    return (a*b)

print(multiply())

resultado=multiply(10,5)
print("Resultado es = ",resultado)
print(type(resultado))   #Esta línea nos dice que tipo de dato es: el resultado
opt=resultado+1
print(opt)