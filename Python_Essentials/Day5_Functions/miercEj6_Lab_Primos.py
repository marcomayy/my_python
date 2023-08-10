# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:00:15 2023

@author: myepez
"""

def EsPrimo(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n=4
if EsPrimo(n):
    print(n," es número primo")
else:
    print(n," no es primo")