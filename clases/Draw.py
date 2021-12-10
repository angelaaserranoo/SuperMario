from CONSTANTES import *
import pyxel
import App
import time


class Draw():
    def draw(self):
        #Dibuja fondo color azul
        pyxel.cls(5)
        #Montañas
        for j in ListaMontañas:
            pyxel.blt(j[0], j[1], 0, 0, 193, 74,34, 12)
        #Nubes 
        for j in ListaNubes:
            pyxel.blt(j[0], j[1], 0, 107, 138, 48 ,21, 12)
        #Arbustos
        for j in ListaArbustos:
            pyxel.blt(j[0], j[1], 0, 139, 46, 61,15, 12)
        #Suelo
        for j in ListaSuelos:
            pyxel.blt(j[0], j[1], 0, 12, 227, j[2], j[3], 12)
        #Tuberias altas
        for j in ListaTuberiasAltas:
            pyxel.blt(j[0], j[1], 0, 79, 178, j[2], j[3], 12)
        #Tuberias bajas
        for j in ListaTuberiasBajas:
            pyxel.blt(j[0], j[1], 0, 38, 132, j[2], j[3], 12)
        for j in ListaBloquesRompibles:
            pyxel.blt(j[0], j[1], 0, 89, 160, j[2], j[3], 12)
        for j in ListaBloquesDuros:
            pyxel.blt(j[0], j[1], 0, 89, 160, j[2], j[3], 12)
        for j in ListaBloquesSorpresa:
            pyxel.blt(j[0], j[1], 0, 177, 27, j[2], j[3], 12)

        #ENEMIGOS
        for j in self.__enemigos:
            #Goomba
            if j.is_walking == None:
                pyxel.blt(j.x, j.y, 1, 0, 0, 16, 16, 12)
            #Koopa
            elif j.is_walking == True:
                pyxel.blt(j.x, j.y, 1, 32, 0, 16, 23, 12)
            else:
                pyxel.blt(j.x, j.y, 1, 16, 0, 16, 16, 12)
            
        #PENDIENTE:Imprime un texto que indica el Mundo y el nivel actual
        pyxel.text(0, 100, str(self.__mario.x), 7)
        pyxel.text(0, 140, str(self.__mario.y), 7)
        pyxel.text(120, 10, "WORLD ", 7)
        pyxel.text(120, 20, world, 7)
        #Imprime la puntuacion de Mario
        pyxel.text(20, 10, "MARIO", 7)
        pyxel.text(20, 20, str(self.__mario.score), 7)
        #Imprime monedas conseguidas
        pyxel.text(85, 10, str(self.__mario.monedas), 7)
        #Imprime simbolo moneda
        pyxel.blt(65, 5, 0, 2, 29, 9, 13, 12)
        #Imprime valor moneda
        pyxel.text (80, 10, "X", 7)
        pyxel.text(90, 10, str(self.__mario.score), 7 )
        #Imprime tiempo restante (encabezado)
        pyxel.text(160, 10, "TIME", 7)
        #Imprimer tiempo restante (Fatlta hacer que sea entero y no float)
        pyxel.text(180, 20, str(tiempo_total - int(time.time()) + self.__mario.tiempo), 7)
        #Dibuja Mario
        if self.__mario.isFalling:
             #Dibuja el Mario que salta
            pyxel.blt(self.__mario.x, self.__mario.y, 0, 0, 79, 16, 16, 12)
        else:
            if len(self.__mario.isMoving) <= 5:
                if len(self.__mario.isMoving) == 0:
                    #Diuja el Mario en reposo
                    pyxel.blt(self.__mario.x, self.__mario.y, 0, 0, 97, 16, 16, 12)
                else:
                    #Dibuja el Mario que anda hacia la derecha
                    pyxel.blt(self.__mario.x, self.__mario.y, 0, 18, 98, 16, 16, 12)
            else:
                #Dibuja el Mario en reposo
                pyxel.blt(self.__mario.x, self.__mario.y, 0, 0, 97, 16, 16, 12)
