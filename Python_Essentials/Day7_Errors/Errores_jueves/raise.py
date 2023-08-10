# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:11:45 2021

@author: Juan Carlos
"""
def badFun(n):
    try:
        return n / 0
    except:
        print("Error en cualquier parte")
        raise 
try:
    badFun(0)
except ArithmeticError:
    print("Error lanzado por raise")
print("THE END.")
