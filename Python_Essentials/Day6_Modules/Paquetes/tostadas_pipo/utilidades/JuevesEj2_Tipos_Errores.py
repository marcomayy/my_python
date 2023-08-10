# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:03:02 2023

@author: myepez
"""
try:
    x=int(input("Enter a number: "))
    y=1/x 
    print(y)
except ZeroDivisionError:
    print("You connot divide by zero")
except ValueError:
    print("You must enter an integer value")
except:
    print("Something went wrong")
print("End")