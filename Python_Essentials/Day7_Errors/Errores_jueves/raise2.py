# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:19:38 2021

@author: Juan Carlos
"""
numero = 10
maximo=5
if numero > maximo:
    raise Exception('El número a ingresar no debe ser mayor que {} . el valor ingresado fue: {}'.format(maximo,numero))