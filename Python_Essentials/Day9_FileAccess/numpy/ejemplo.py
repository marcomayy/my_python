# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:21:22 2023

@author: Juan Carlos
"""

# Importamos el módulo NumPy
import numpy as np

# Creamos un array de NumPy con 10 elementos
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Imprimimos el array
print(array)

# Calculamos la suma de los elementos del array
sum = np.sum(array)

# Imprimimos la suma
print(sum)

# Calculamos el promedio de los elementos del array
average = np.mean(array)

# Imprimimos el promedio
print(average)

# Calculamos la desviación estándar de los elementos del array
stddev = np.std(array)

# Imprimimos la desviación estándar
print(stddev)

# Calculamos la varianza de los elementos del array
variance = np.var(array)

# Imprimimos la varianza
print(variance)

# Calculamos el máximo de los elementos del array
maximum = np.amax(array)

# Imprimimos el máximo
print(maximum)

# Calculamos el mínimo de los elementos del array
minimum = np.amin(array)

# Imprimimos el mínimo
print(minimum)

# Calculamos la mediana de los elementos del array
median = np.median(array)

# Imprimimos la mediana
print(median)

# Calculamos la moda de los elementos del array
mode = np.argmax(np.bincount(array))

print(mode)
