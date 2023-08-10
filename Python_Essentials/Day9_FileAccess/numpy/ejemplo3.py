# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:28:16 2023

@author: Juan Carlos
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulación de datos de un dispositivo IoT
tiempo = np.arange(0, 10, 0.1)  # Intervalo de tiempo de 0 a 10 segundos con paso de 0.1 segundos
temperatura = 25 + 2 * np.sin(tiempo) + np.random.normal(0, 1, len(tiempo))  # Datos de temperatura simulados

# Creación de un gráfico con Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(tiempo, temperatura, label='Temperatura', color='blue')
plt.title('Datos de Temperatura de un Dispositivo IoT')
plt.xlabel('Tiempo (s)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
