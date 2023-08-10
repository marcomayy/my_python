# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:25:09 2023

@author: Juan Carlos
"""

import numpy as np

# Crear un array de sensores
sensors = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Crear un array de actuadores
actuators = np.array([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

# Obtener la lectura de los sensores
readings = sensors[0]

# Controlar los actuadores
actuators[0] = readings

# Imprimir las lecturas y los valores de los actuadores
print(readings)
print(actuators)
