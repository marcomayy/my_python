# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:46:02 2023

@author: myepez
"""

import math
pi=22/7
def sin(): #Creo función sin, pero no entra en conflicto con operación sin del módulo math
    return 9.999
print(sin()) #Imprime resultado de mi función pi y no la del módulo sin de math
print(pi)
opt=math.sin(math.pi/2) #Aquí uso el sin del módulo math
print(opt)