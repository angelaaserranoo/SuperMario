#Importamos todas las clases
import pyxel
import time
from Jugador import *
from CONSTANTES import *
from Enemigo import *
from Bloque import *
from Fondo import *
from Fondo import Fondo

class App():
#definimos cada atributo, siendo cada uno objetos de otras clases
    def __init__(self):
        self.__mario = Jugador()
        self.__suelo = self.CrearBloque(n_suelos, 184)
        self.__nubes = self.CrearFondo(nubes,40)
        self.__montañas = self.CrearFondo(n_montañas, 152)
        self.__bloques_rompibles = self.CrearBloque(n_bloques_rompibles, 120)
        self.__bloques_sorpresa = self.CrearBloque(n_bloques_sorpresa, 120)
        self.__tuberias_bajas = self.CrearBloque(n_tuberias_bajas, 153)
        self.__tuberias_altas = self.CrearBloque(n_tuberias_altas, 136)
        #Definimos el tamaño y el nombre de la ventana
        pyxel.init(200, 200, caption = "Mario Bros")
        #Cargamos la imagen al banco
        pyxel.load(r'C:\Users\anaja\Documents\Super_maria\assets\mario_assets.pyxres')
        #se ejecuta el programa llamando continuamente a las funciones draw y update
        pyxel.run(self.update, self.draw)

    def TocarSuelo(self):    
        for i in self.__suelo:
            if self.__mario.x() < i.x()+ 96 and self.__mario.x() >= i.x() and (self.__mario.y()-16 == i.y()):
                #self.__mario.setisJumping(False)
                self.__mario.setvy(0)
                self.__mario.sety(i.y()-15)
            else:
                #self.__mario.setisJumping(True)
                self.__mario.setvy(1)

#Funcion que crea una lista de objetos de tipo bloque y los posiciona a lo largo del mapa de manera equitativa
    def CrearBloque(self, n_suelos, y):
        lista = []
        repeticiones = int(ancho_nivel/n_suelos)
        for i in range(n_suelos):
            x = Bloque((i * repeticiones), y)
            lista.append(x)
        return lista
#Funcion que genera los elementos del fondo y les atribuye una posicion a cada uno
    def CrearFondo(self, n_elementos, y):
        lista = []
        repeticiones= ancho_nivel/n_elementos
        for i in range(n_elementos):
            lista.append(Fondo ((i*repeticiones), y))
        return lista
#Funcion que actualiza el juego, llamando a la actualizacion de cada uno de los objetos
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.__mario.update()
        self.TocarSuelo()

#Funcion que se encarga de dibujar cada uno de los elementos        
    def draw(self):
        #Dibuja fondo color azul
        pyxel.cls(5)
        #Montañas
        for j in self.__montañas:
            pyxel.blt(j.x(), j.y(), 0, 0, 193, 74,33, 12 )
        #Nubes cercanas
        for j in self.__nubes:
            pyxel.blt(j.x(), j.y(), 0, 106, 138, 49,21, 12 )
        #Suelo
        for j in self.__suelo:
            pyxel.blt(j.x(), j.y(), 0, 0, 227, 96, 15, 12)
        #Tuberias bajas
        for j in self.__tuberias_bajas:
            pyxel.blt(j.x(), j.y(), 0, 38, 132, 32, 31, 12)
        #Tuberias altas: La primera no se dibuja para que no se superponga con la baja    
        for j in self.__tuberias_altas:
            if j == self.__tuberias_altas[0]:
                pass
            else:
                pyxel.blt(j.x(), j.y(), 0, 79, 178, 32, 48, 12)
        #Bloques rompibles
        for j in self.__bloques_rompibles:
            if j == self.__bloques_rompibles[0]:
                pass
            else:
                pyxel.blt(j.x(), j.y(), 0, 0, 62, 16, 16, 12)
        #Bloques sorpresa
        for j in self.__bloques_sorpresa:
            if j == self.__bloques_sorpresa[0]:
                pass
            else:
                pyxel.blt(j.x(), j.y(), 0, 177, 27, 16,16, 12)
        #PENDIENTE:Imprime un texto que indica el Mundo y el nivel actual
        pyxel.text(120, 10, "WORLD ", 7)
        pyxel.text(120, 20, world, 7)
        #Imprime la puntuacion de Mario
        pyxel.text(20, 10, "MARIO", 7)
        pyxel.text(20, 20, str(self.__mario.score()), 7)
        #Imprime monedas conseguidas
        pyxel.text(85, 10, str(self.__mario.monedas()), 7)
        #Imprime simbolo moneda
        pyxel.blt(65, 5, 0, 2, 29, 9, 13, 12)
        #Imprime valor moneda
        pyxel.text (80, 10, "X", 7)
        #Imprime tiempo restante (encabezado)
        pyxel.text(160, 10, "TIME", 7)
        #Imprimer tiempo restante (Fatlta hacer que sea entero y no float)
        pyxel.text(180, 20, str(tiempo_total - int(time.time()) + self.__mario.tiempo()), 7)
        #Dibuja Mario
        if self.__mario.isJumping():
             #Dibuja el Mario que salta
            pyxel.blt(self.__mario.x(), self.__mario.y(), 0, 0, 79, 16, 16, 12)
        else:
            if len(self.__mario.isMoving()) <= 5:
                if len(self.__mario.isMoving()) == 0:
                    #Diuja el Mario en reposo
                    pyxel.blt(self.__mario.x(), self.__mario.y(), 0, 0, 97, 16, 16, 12)

                else:
                    #Dibuja el Mario que anda hacia la derecha
                    pyxel.blt(self.__mario.x(), self.__mario.y(), 0, 18, 98, 16, 16, 12)

            else:
                #Diuja el Mario en reposo
                pyxel.blt(self.__mario.x(), self.__mario.y(), 0, 0, 97, 16, 16, 12)

App()