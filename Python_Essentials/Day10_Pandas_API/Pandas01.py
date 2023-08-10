# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 19:00:10 2023

@author: myepez
"""

import pandas as pd
titulos = pd.read_csv('data/titles.csv')
print(titulos.head(10))
print('\n'*2)
elenco = pd.read_csv('data/cast.csv')
print(elenco.head(10))
print("\n"*2)
elenco = pd.read_csv('data/cast.csv')
print(elenco.head(10))
#Cuantas películas están listadas en títulos dataframe
print(len(titulos))
#Cuántos elementos están listadas en títulos elenco
print(len(elenco))
#Listar todas las películas que contengan la palabra "Spider"
consulta1=titulos[titulos.title.str.contains("The Lord of the Rings")].sort_values("year",ascending=True)
print(consulta1)