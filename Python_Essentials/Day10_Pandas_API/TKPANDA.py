# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 08:51:33 2023

@author: Juan Carlos
"""

import tkinter as tk
import pandas as pd

# Cargar los datos
titulos = pd.read_csv('data/titles.csv')
elenco = pd.read_csv('data/cast.csv', encoding='utf-8')

# Crear la interfaz gráfica
window = tk.Tk()
window.title("Consulta de Dataframe")
window.geometry("600x400")

# Funciones de consulta
def mostrar_titulos():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, titulos.head(100))

def mostrar_elenco():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, elenco.head(10))

def contar_peliculas():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, len(titulos))

def buscar_pelicula():
    pelicula = entry_input.get()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, titulos[titulos.title == pelicula].sort_values('year').head(5))

def buscar_contiene():
    palabra = entry_input.get()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, titulos[titulos.title.str.contains(palabra)].sort_values('year'))

def contar_peliculas_anio():
    anio = entry_input.get()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, len(titulos[titulos.year == int(anio)]))

def contar_peliculas_rango():
    anio_inicio = entry_input.get()
    anio_fin = entry_input2.get()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, len(titulos[(titulos.year >= int(anio_inicio)) & (titulos.year <= int(anio_fin))]))

def buscar_pelicula_titulo():
    titulo = entry_input.get()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, titulos[titulos.title == titulo])

def buscar_pelicula_star_wars():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, titulos[titulos.title == "Star Wars"])

def buscar_pelicula_star_wars_contiene():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, titulos[titulos.title.str.contains("Star War")].sort_values('year'))

def buscar_pelicula_1973():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, titulos[titulos.year == 1973].head(1))

def contar_peliculas_1980_2000():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, len(titulos[(titulos.year >= 1980) & (titulos.year <= 2000)]))

def contar_roles_godfather():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, len(elenco[elenco.title == "The Godfather"]))

def contar_roles_godfather_no_clasificados():
    c = elenco[elenco.title == "The Godfather"]
    c = c[c.n.isnull()]
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, len(c))

# Elementos de la interfaz
frame_input = tk.Frame(window)
frame_input.pack(pady=10)

label_input = tk.Label(frame_input, text="Consulta:")
label_input.pack(side=tk.LEFT)

entry_input = tk.Entry(frame_input, width=50)
entry_input.pack(side=tk.LEFT)

frame_input2 = tk.Frame(window)
frame_input2.pack(pady=10)

label_input2 = tk.Label(frame_input2, text="Segundo valor (si es necesario):")
label_input2.pack(side=tk.LEFT)

entry_input2 = tk.Entry(frame_input2, width=50)
entry_input2.pack(side=tk.LEFT)

button_mostrar_titulos = tk.Button(window, text="Mostrar títulos", command=mostrar_titulos)
button_mostrar_titulos.pack(pady=5)

button_mostrar_elenco = tk.Button(window, text="Mostrar elenco", command=mostrar_elenco)
button_mostrar_elenco.pack(pady=5)

button_contar_peliculas = tk.Button(window, text="Contar películas", command=contar_peliculas)
button_contar_peliculas.pack(pady=5)

button_buscar_pelicula = tk.Button(window, text="Buscar película", command=buscar_pelicula)
button_buscar_pelicula.pack(pady=5)

button_buscar_contiene = tk.Button(window, text="Buscar películas que contengan", command=buscar_contiene)
button_buscar_contiene.pack(pady=5)

button_contar_peliculas_anio = tk.Button(window, text="Contar películas por año", command=contar_peliculas_anio)
button_contar_peliculas_anio.pack(pady=5)

button_contar_peliculas_rango = tk.Button(window, text="Contar películas por rango de años", command=contar_peliculas_rango)
button_contar_peliculas_rango.pack(pady=5)

button_buscar_pelicula_titulo = tk.Button(window, text="Buscar película por título", command=buscar_pelicula_titulo)
button_buscar_pelicula_titulo.pack(pady=5)

button_buscar_pelicula_star_wars = tk.Button(window, text="Buscar película 'Star Wars'", command=buscar_pelicula_star_wars)
button_buscar_pelicula_star_wars.pack(pady=5)

button_buscar_pelicula_star_wars_contiene = tk.Button(window, text="Buscar películas que contengan 'Star War'", command=buscar_pelicula_star_wars_contiene)
button_buscar_pelicula_star_wars_contiene.pack(pady=5)

button_buscar_pelicula_1973 = tk.Button(window, text="Buscar película del año 1973", command=buscar_pelicula_1973)
button_buscar_pelicula_1973.pack(pady=5)

button_contar_peliculas_1980_2000 = tk.Button(window, text="Contar películas entre 1980 y 2000", command=contar_peliculas_1980_2000)
button_contar_peliculas_1980_2000.pack(pady=5)

button_contar_roles_godfather = tk.Button(window, text="Contar roles en 'The Godfather'", command=contar_roles_godfather)
button_contar_roles_godfather.pack(pady=5)

button_contar_roles_godfather_no_clasificados = tk.Button(window, text="Contar roles no clasificados en 'The Godfather'", command=contar_roles_godfather_no_clasificados)
button_contar_roles_godfather_no_clasificados.pack(pady=5)

result_text = tk.Text(window, height=10, width=80)
result_text.pack(pady=10)

window.mainloop()
