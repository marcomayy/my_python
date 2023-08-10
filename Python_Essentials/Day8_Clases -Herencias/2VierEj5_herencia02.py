# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 08:34:02 2023

@author: Juan Carlos
"""

class Robot:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y soy un robot {self.color}.")

class RobotAsistente(Robot):
    def __init__(self, nombre, color, tareas):
        super().__init__(nombre, color)
        self.tareas = tareas

    def saludar(self):
        super().saludar()
        print("Soy un robot asistente y estoy aquí para ayudarte.")

    def realizar_tareas(self):
        print(f"Realizando tareas: {self.tareas}")


robot1 = Robot("Robot1", "rojo")
robot1.saludar()

robot2 = RobotAsistente("Robot2", "azul",
                        ["limpiar", 
                         "cocinar", "organizar"])
robot2.saludar()
robot2.realizar_tareas()
