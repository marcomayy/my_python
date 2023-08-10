# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:43:55 2023

@author: Juan Carlos
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de simulación
fs = 10000  # Frecuencia de muestreo en Hz
fc = 500  # Frecuencia de la portadora en Hz
bits_per_symbol = 4  # Cantidad de bits por símbolo
symbol_rate = 100  # Tasa de símbolos en Hz
snr_db = 20  # Relación señal/ruido en dB

# Generar datos aleatorios para transmitir
np.random.seed(0)
data_bits = np.random.randint(0, 2, 1000 * bits_per_symbol)

# Crear símbolos a partir de los datos binarios
symbols = data_bits.reshape(-1, bits_per_symbol).dot(1 << np.arange(bits_per_symbol)[::-1])

# Generar la señal modulada (símbolos modulados en una portadora)
time = np.arange(0, len(symbols) / symbol_rate, 1 / fs)
carrier_wave = np.cos(2 * np.pi * fc * time)
modulated_signal = np.repeat(symbols, fs // symbol_rate) * carrier_wave

# Agregar ruido gaussiano a la señal
snr_linear = 10 ** (snr_db / 10)
noise = np.random.normal(0, 1 / np.sqrt(2 * snr_linear), len(modulated_signal))
received_signal = modulated_signal + noise

# Demodulación de la señal
demodulated_signal = received_signal * carrier_wave
demodulated_signal = np.convolve(demodulated_signal, np.ones(fs // symbol_rate) / (fs // symbol_rate), mode='valid')

# Recuperar los símbolos demodulados
recovered_symbols = np.around((demodulated_signal + np.max(demodulated_signal)) / (2 * np.max(demodulated_signal)))
recovered_bits = np.unpackbits(recovered_symbols.astype(np.uint8))[-len(data_bits):]

# Calcular la tasa de error de bits
bit_error_rate = np.sum(data_bits != recovered_bits) / len(data_bits)
print("Bit Error Rate:", bit_error_rate)

# Graficar la señal transmitida y la recibida
plt.figure(figsize=(10, 6))
plt.plot(time, modulated_signal, label='Señal Transmitida')
plt.plot(time[len(time) - len(demodulated_signal):], demodulated_signal, label='Señal Recibida')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.show()
