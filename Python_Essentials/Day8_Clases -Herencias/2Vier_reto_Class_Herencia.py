# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:14:38 2023

@author: Juan Carlos
"""

# Clase Dispositivo
class Dispositivo:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        
    def encender(self):
        print("El dispositivo", self.nombre, "se ha encendido")
        
    def apagar(self):
        print("El dispositivo", self.nombre, "se ha apagado")
        
# Clase LED
class LED(Dispositivo):
    def cambiar_color(self, color):
        print("El LED", self.nombre, "ha cambiado a", color)
        
    def parpadear(self):
        print("El LED", self.nombre, "está parpadeando")
        
# Clase Sensor
class Sensor(Dispositivo):
    def leer_valor(self):
        print("El sensor", self.nombre, "ha leído un valor")
        
    def detectar_movimiento(self):
        print("El sensor", self.nombre, "ha detectado movimiento")

# Uso de las clases para controlar
# Creación de dispositivos virtuales
mi_led = LED("mi LED", "sala")
mi_sensor = Sensor("mi sensor", "puerta")

# Control de dispositivos virtuales
mi_led.encender()
mi_led.cambiar_color("verde")
mi_sensor.leer_valor()
mi_sensor.detectar_movimiento()
mi_led.apagar()
