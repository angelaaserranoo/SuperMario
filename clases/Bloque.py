import pyxel
from CONSTANTES import *
class  Bloque():
    #Se incluyen tuberias, suelo, y todos los tipos de bloques
    #Cada bloque tendra una posicion y dimension definida(tanto en x como en y), ademas del atributo que comprueba si el bloque se rompe y cuantas veces se ha golpeado
    def __init__(self, x, y, ancho, alto, rompible):
        self.__x = x
        self.__y = y
        self.__ancho = ancho
        self.__alto = alto
        self.__rompible = rompible
        self.__roto = False
        self.__n_colisiones = 0

#funciones para obtener atributos privados
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def rompible(self):
        return self.__rompible

    @property
    def ancho(self):
        return self.__ancho

    @property
    def alto(self):
        return self.__alto

    @property
    def roto(self):
        return self.__roto

    @property
    def n_colisiones(self):
        return self.__n_colisiones

    def setx(self, value):
        self.__x = value
    
    def sety(self, value):
        self.__y = value

    def setancho(self, value):
        self.__ancho = value
    
    def setalto(self, value):
        self.__alto = value

    def setrompible(self, value):
        self.__rompible = value

    def setroto(self, value):
        self.__roto = value

    def set_n_colisiones(self, value):
        self.__n_colisiones = value