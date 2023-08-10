class Magnitud:
    def __init__(self,valor):
        self.valor = valor
        
class Temperatura(Magnitud):
    def kelvinCelsius(self):
        self.valor =  self.valor -273.1
        return self.valor
    def FarengeiCelsius(self):
        self.valor = self.valor-32*5/9
        return self.valor
    def kelvinFarengei(self):
        self.valor = self.valor-273*1.8+32
        return  self.valor

class Longitud(Magnitud):
    def centimetrosPulgada(self):
        self.valor =  self.valor / 2.54
        return self.valor

class Masa(Magnitud):
    def libraTonelada(self):
        self.valor =  self.valor / 2205
        return self.valor
