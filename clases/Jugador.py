from CONSTANTES import *
import pyxel
import time

class Jugador():
    def __init__(self):
        self.__x = x0
        self.__y = y0
        self.__vy = vy0
        self.__score = score0
        self.__n_vidas= n_vidas
        self.__monedas = monedas0
        """Jugador tiene 4 estados (muerto,
        mario, super mario, mario de fuego)
        el kind será un numero entre 0 y 3 que 
        definira su estado"""
        self.__kind = kind
        self.__isMoving = []
        self.__isJumping = False
        self.__tiempo = int(time.time())
    
    #@property
    def x(self):
        return self.__x

    def sety(self,value):
        self.__y = value
    
    
    #@property
    def y(self):
        return self.__y
    
    #@property
    def vy(self):
        return self.__vy

    def setvy(self, value):
        self.__vy = value

    def isJumping(self):
        return self.__isJumping

    def setisJumping(self, value):
        self.__isJumping = value

    #@property
    def score(self):
        return self.__score

    def monedas(self):
        return self.__monedas

    def tiempo(self):
        return self.__tiempo

    def isMoving(self):
        return self.__isMoving

    def Reset(self):
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
        self.__isJumping = False
        self.__startJumpHeight = 0
    
    def update(self, jumped = False):
        #MOVER IZQUIERDA
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            if len(self.__isMoving) <= 8:
                self.__x = max(self.__x-3, 0)
                self.__isMoving.append(True)
            else:
                self.__x = max(self.__x-3, 0)
                self.__isMoving.clear()

        #MOVER DERECHA
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            if len(self.__isMoving) <= 8:
                self.__x = min(self.__x+3, (200/2)-1)
                self.__isMoving.append(True)
            else:
                self.__x = min(self.__x+3, (200/2)-1)
                self.__isMoving.clear()
        else:
            self.__isMoving.clear()

        #SALTO
        if self.__isJumping == False:
            if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD_1_UP):
                self.__vy -= 9
                self.__y += self.__vy
                self.__isJumping = True
        else:
            self.__y += self.__vy