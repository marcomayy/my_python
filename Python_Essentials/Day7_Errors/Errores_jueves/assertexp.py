# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:51:11 2020

@author: Juan Carlos
"""

from math import tan, radians
angle = int(input('Ingresa el angulo entero en grados: '))

# debemos estar seguros de ese angulo != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))