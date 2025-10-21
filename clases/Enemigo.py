from CONSTANTES import *
from random import randint
import pyxel

class Enemigo(): #Enemigo define tanto a Koopa Troopa como a Goomba a partir de su posicion, dimensiones, velocidad, y otros atributos que los diferenciaran
    def __init__(self, x_enemigo, y_enemigo, ancho, alto, is_walking=None):
        self.__x = x_enemigo
        self.__y = y_enemigo
        self.__ancho = ancho
        self.__alto = alto
        self.__vy = vy0
        self.__vx = -1
        #Define si esta vivo el enemigo
        self.__is_alive = True
        #Define si esta cayendo o esta quieto
        self.__isFalling = True
        # Podra ser none (Goomba), True (Koopa abierto) o False (koopa cerrado)
        self.__is_walking = is_walking
        #Atributo necesario para la parte grafica 
        self.__tiempo_muerte = 0
            

    @property
    def is_alive(self):
        return self.__is_alive

    @property
    def is_walking(self):
        return self.__is_walking

    @property
    def x(self):
        return self.__x

    @property
    def vx(self):
        return self.__vx

    @property
    def y(self):
        return self.__y

    @property
    def ancho(self):
        return self.__ancho

    @property
    def alto(self):
        return self.__alto

    @property
    def vy(self):
        return self.__vy

    @property
    def tiempo_muerte(self):
        return self.__tiempo_muerte

    def setx(self, value):
        self.__x = value

    def setvx(self, value):
        self.__vx = value

    def sety(self, value):
        self.__y = value
    
    def setvy(self, value):
        self.__vy = value

    def setalto(self, value):
        self.__alto = value

    def setancho(self, value):
        self.__ancho = value

    def setisFalling(self, value):
        self.__isFalling = value

    def setisAlive(self, value):
        self.__is_alive = value

    def setisWalking(self, value):
        self.__is_walking = value

    def setisFalling(self, value):
        self.__isFalling = value
    
    def settiempoMuerte(self, value):
        self.__tiempo_muerte = value

    def updateEnemigo2(self):
        #Actualizo posicion de enemigo en las caidas
        self.__vy += 1
        self.__vy = min(self.__vy+1, 9)
        self.__y += self.__vy
