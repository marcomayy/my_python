# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:15:28 2023

@author: myepez
"""

while True:
    x=input("Enter the number to count to")
    if x=='q' or x== 'quit':
        break 
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break