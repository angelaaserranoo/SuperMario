from CONSTANTES import *
import pyxel
import time

class Jugador():
    def __init__(self):
        self.__x = x0
        self.__y = y0
        self.__vy = vy0
        self.__score = score0
        self.__n_vidas = n_vidas
        self.__monedas = monedas0
        """Jugador tiene 4 estados (muerto,
        mario, super mario, mario de fuego)
        el kind será un numero entre 0 y 3 que 
        definira su estado"""
        self.__kind = kind
        self.__isMoving = []
        self.__isFalling = False
        self.__tiempo = int(time.time())
        self.__previous = [self.__x, self.__y]
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @property
    def vy(self):
        return self.__vy
    @property
    def isFalling(self):
        return self.__isFalling    

    @property
    def previous(self):
        return self.__previous

    @property
    def score(self):
        return self.__score

    @property
    def monedas(self):
        return self.__monedas

    @property
    def tiempo(self):
        return self.__tiempo

    @property
    def isMoving(self):
        return self.__isMoving


    def setx(self, value):
        self.__x = value

    def sety(self,value):
        self.__y = value
    
    def setvy(self, value):
        self.__vy = value

    def setisFalling(self, value):
        self.__isFalling = value


    def Reset(self):
        self.__x = x0
        self.__y = y0
        self.__vy = vy0
        self.__score = score0
        self.__n_vidas = n_vidas
        self.__monedas = monedas0
        #Jugador tiene 4 estados (muerto,mario, super mario, mario de fuego) el kind será un numero entre 0 y 3 que definira su estado
        self.__kind = kind
        self.__isFalling = False
        self.__startJumpHeight = 0
    
    def update(self, jumped = False):
        #self.__previous = [self.__x, self.__y]
        self.__y += self.__vy
        #MOVER IZQUIERDA
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            if len(self.__isMoving) <= 8:
                self.__isMoving.append(True)
                self.__x = max(self.__x-3, 0)
            else:
                self.__isMoving.clear()
                self.__x = max(self.__x-3, 0)

        #MOVER DERECHA
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            if len(self.__isMoving) <= 8:
                self.__x = min(self.__x+3, 100)
                self.__isMoving.append(True)
            else:
                self.__x = min(self.__x+3, 100)
                self.__isMoving.clear()
        else:
            self.__isMoving.clear()

        #SALTO
        if self.__isFalling == False:
            if pyxel.btn(pyxel.KEY_UP) == True or pyxel.btn(pyxel.GAMEPAD_1_UP) == True:
                if self.__vy > -7:
                    self.__vy -= 1
                    self.__y += self.__vy
                else:
                    self.__isFalling = True
            else:
                self.__isFalling = True
        else:
            self.__vy = min(self.__vy+1, 9)

        #Resetea el jugador (Borrar al final)
        if pyxel.btn(pyxel.KEY_R) :
            self.Reset()