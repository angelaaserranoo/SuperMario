#Importamos todas las clases
import pyxel
import time
from Jugador import *
from CONSTANTES import * #[[50, 138]] L[0]
from Enemigo import *
from Bloque import *
from Fondo import *
from Fondo import Fondo

class App():
#definimos cada atributo, siendo cada uno objetos de otras clases
    def __init__(self):
        self.__mario = Jugador()
        self.__suelo = self.CrearBloque(ListaSuelos)
        self.__nubes = self.CrearFondo(nubes, 40)
        self.__montañas = self.CrearFondo(n_montañas, 152)
        self.__bloques_rompibles = self.CrearBloque(ListaBloquesRompibles)
        self.__bloques_sorpresa = self.CrearBloque(ListaBloquesSorpresa)
        self.__bloques_duros = self.CrearBloque(ListaBloquesDuros)
        self.__tuberias_altas = self.CrearBloque(ListaTuberiasAltas)
        self.__tuberias_bajas = self.CrearBloque(ListaTuberiasBajas)
        #Definimos el tamaño y el nombre de la ventana
        pyxel.init(200, 200, caption = "Mario Bros")
        #Cargamos la imagen al banco
        pyxel.load(r'C:\Users\anaja\Documents\Super_maria\assets\mario_assets.pyxres')
        #se ejecuta el programa llamando continuamente a las funciones draw y update
        pyxel.run(self.update, self.draw)
    
#Funcion que crea una lista de objetos de tipo bloque y los posiciona a lo largo del mapa de manera equitativa
    def CrearBloque(self, Lista):
        ListaObjetosBloque = []
        for i in Lista:
             ListaObjetosBloque.append(Bloque(i[0], i[1], i[2], i[3]))
        return ListaObjetosBloque

    def ColisionVertical(self):
        for i in ListaTotal:
            if self.__mario.x()+16 > i[0] and self.__mario.x() < (i[0] + i[2]):
                if self.__mario.y()+16 > i[1] and self.__mario.y()+16 < (i[1]+i[3]):
                    self.__mario.setisJumping(False)
                    self.__mario.sety(i[1]-16)
                elif self.__mario.y() > i[1] and self.__mario.y() < (i[1]+i[3]):
                    self.__mario.sety(i[1]+i[3])    
                    self.__mario.setvy(2)

    def ColisionHorizontal(self):
        for i in ListaTotal:
            if self.__mario.y()+16 < i[1] and self.__mario.y() > (i[1]+i[3]):
                if self.__mario.x()+16 > i[0] and self.__mario.x()+16 < (i[0]+i[3]):
                    self.__mario.setx(i[0]-16)
                    self.__mario.sety(i[1])
                elif self.__mario.x() < (i[0]+i[3]) and self.__mario.x() > i[0]:
                    self.__mario.setx(i[0]+i[3])
                    self.__mario.sety(i[1])
                   


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
        self.ColisionVertical()
        self.ColisionHorizontal()

#Función que se encarga de dibujar cada uno de los elementos        
    def draw(self):
        #Dibuja fondo color azul
        pyxel.cls(5)
        #Montañas
        for j in self.__montañas:
            pyxel.blt(j.x(), j.y(), 0, 0, 193, 74,33, 12)
        #Nubes cercanas
        for j in self.__nubes:
            pyxel.blt(j.x(), j.y(), 0, 106, 138, 49, 21, 12)
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
            
        #PENDIENTE:Imprime un texto que indica el Mundo y el nivel actual
        pyxel.text(0, 100, str(self.__mario.x()), 7)
        pyxel.text(0, 140, str(self.__mario.y()), 7)
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
        pyxel.text(90, 10, str(self.__mario.score()), 7 )
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
                #Dibuja el Mario en reposo
                pyxel.blt(self.__mario.x(), self.__mario.y(), 0, 0, 97, 16, 16, 12)

App()