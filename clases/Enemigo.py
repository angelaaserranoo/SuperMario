from CONSTANTES import *
from random import randint
import pyxel

class Enemigo():
    def __init__(self, x_enemigo, y_enemigo, is_walking=None):
        self.__x = x_enemigo
        self.__y = y_enemigo
        self.__vy = vy0
        self.__vx = -1
        self.__is_alive = False
        self.__isFalling = True
        self.__is_walking = is_walking
    
    def setisFalling(self, value):
        self.__isFalling = value

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
    def vy(self):
        return self.__vy

    def setx(self, value):
        self.__x = value

    def sety(self, value):
        self.__y = value
    
    def setvy(self, value):
        self.__vy = value

    def activar(self):
        if self.__x < 200:
            self.__vx = 2
            self.__x+= self.__vx
    
    def updateEnemigo2(self):
        if self.__isFalling == False:
            if self.__vy > -7:
                self.__vy -= 1
                self.__y += self.__vy
            else:
                self.__isFalling = True
        
        else:
            self.__vy = min(self.__vy+1, 9)

    

    def morir (self):
        pass