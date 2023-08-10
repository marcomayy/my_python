# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 20:17:08 2023

@author: myepez
"""

archivo=open("C:/Users/myepez/Documents/PythonDocs/devices.txt")
for item in archivo:
    item=item.strip("Cisco")
    print(item)

archivo.close()