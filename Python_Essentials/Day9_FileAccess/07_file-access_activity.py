# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:26:58 2023

@author: myepez
"""

file=open("devices.txt","r")
#print(f.read())
while True:
    newitem=input("Ingrese un nuevo dispositivo: ")
    if newitem == "exit":
        print("All done!")
        break
    file.write(newitem + "\n")
file.close()
    
    
    
