# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:16:34 2023

@author: myepez
"""

class Animales:
    #Atributos:
    def __init__(self,tipo, nombre, genero, expt_vida, habitat, activo):
        self.tipo = tipo
        self.nombre = nombre
        self.genero = genero
        self.expt_vida = expt_vida
        self.habitat = habitat
        self.activo = activo

#Métodos:    
    def alimentación(self):
        print("Este animal se alimenta en base a: ")
        
    def habitos(self):
        print("Se caracteriza por")
        
anim1= Animales("Perro","Zakura","hembra",15,"ciudad","diurna")
anim2= Animales("Gato","Lazy","hembra",15,"ciudad","nocturna")
anim3= Animales("Oso","Yogui","macho",25,"bosque","diurna")
anim4= Animales("Búho","Mocho","macho",20,"bosque","nocturna")
