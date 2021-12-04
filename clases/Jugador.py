from CONSTANTES import *
import pyxel

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
        self.__isJumping = False
        self.__startJumpHeight = 0

    #@property
    def score(self):
        return self.__score
    
    #@property
    def x(self):
        return self.__x
    
    #@property
    def y(self):
        return self.__y
    
    #@property
    def vy(self):
        return self.__vy

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

    def update(self, jumped=False):
        #MOVER IZQUIERDA
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.__x = max(self.__x-3, 0)
        #MOVER DERECHA
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.__x = min(self.__x+3, (160/2)-1)
        #SALTO
        if self.__isJumping == False:
            if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD_1_UP):
                self.__startJumpHeight = self.__y
                self.__vy -= 9
                self.__y += self.__vy
                self.__isJumping = True
        else:
            if not(self.__y + self.__vy >= self.__startJumpHeight):
                self.__y += self.__vy
                self.__vy += 2
            else:
                self.__vy = 0
                self.__y = self.__startJumpHeight
                self.__isJumping = False