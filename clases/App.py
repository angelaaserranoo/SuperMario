#Importamos todas las clases
import pyxel
from Jugador import *
from CONSTANTES import *
from Enemigo import *
from Bloque import *
from Fondo import *
from Fondo import Fondo
from Enemigo import *

class App():
#Definimos cada atributo, siendo cada uno objetos de otras clases
    def __init__(self):
        self.__mario = Jugador()
        self.__suelo = self.CrearBloque(ListaSuelos)
        self.__nubes = self.CrearFondo(ListaNubes)
        self.__montañas = self.CrearFondo(ListaMontañas)
        self.__arbustos = self.CrearFondo (ListaArbustos)
        self.__bloques_rompibles = self.CrearBloque(ListaBloquesRompibles)
        self.__bloques_sorpresa = self.CrearBloque(ListaBloquesSorpresa)
        self.__bloques_duros = self.CrearBloque(ListaBloquesDuros)
        self.__tuberias_altas = self.CrearBloque(ListaTuberiasAltas)
        self.__tuberias_bajas = self.CrearBloque(ListaTuberiasBajas)
        self.__enemigos = self.CrearEnemigo()
        #Definimos el tamaño y el nombre de la ventana
        pyxel.init(200, 200, caption = "Mario Bros")
        #Cargamos la imagen al banco
        pyxel.load(r'C:\Users\anaja\Documents\Super_maria\assets\mario_assets.pyxres')
        #se ejecuta el programa llamando continuamente a las funciones draw y update
        pyxel.run(self.update, self.draw)
    
#Funcion que genera los elementos del fondo y les atribuye una posicion a cada uno
    def CrearFondo(self, Lista):
        ListaObjetosFondo = []
        for i in Lista:
            ListaObjetosFondo.append(Fondo(i[0], i[1]))
        return ListaObjetosFondo

#Funcion que actualiza el fondo
    def updateFondo(self):
        if self.__mario.x >=100 and (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT)):
            for i in ListaTotalFondo:
                i[0]-=2

#Funcion que crea una lista de objetos de tipo bloque y los posiciona a lo largo del mapa de manera equitativa
    def CrearBloque(self, Lista):
        ListaObjetosBloque = []
        for i in Lista:
             ListaObjetosBloque.append(Bloque(i[0], i[1], i[2], i[3]))
        return ListaObjetosBloque

    def updateBloque(self):
        if self.__mario.x >=100 and (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT)):
            for i in ListaTotalBloques:
                i[0]-=2

    def CrearEnemigo(self):
        listaEnemigos = []
        for i in posx_enemigos:
            posibilidad = random.randint(0,3)
            if posibilidad == 0:
                listaEnemigos.append(Enemigo(i, 60, True))
            else:
                listaEnemigos.append(Enemigo(i, 60))
        return listaEnemigos

    def updateEnemigo(self):
        for i in self.__enemigos:
            if self.__mario.x >=100 and (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT)):
                i.setx(i.x-2)
            if i.x<-40:
                i.setx(i.x+300)
            i.setx(i.x+i.vx)

    def ColisionVertical (self, objeto: object):
        try:
            i=0
            Touch = False
            while i < len(ListaTotalBloques) and Touch ==False:
                if objeto.x+16 > ListaTotalBloques[i][0] and  (objeto.x < ListaTotalBloques[i][0] + ListaTotalBloques[i][2]):
                    if objeto.y+16 >= ListaTotalBloques[i][1] and objeto.y < ListaTotalBloques[i][1]:
                        objeto.setisFalling(False)
                        objeto.sety(ListaTotalBloques[i][1]-16)
                        objeto.setvy(0)
                        Touch =True
                    
                    elif objeto.y < (ListaTotalBloques[i][1]+ ListaTotalBloques[i][3]) and objeto.y + 16> (ListaTotalBloques[i][1]+ListaTotalBloques[i][3]):
                        objeto.sety(ListaTotalBloques[i][1]+ListaTotalBloques[i][3])
                        objeto.setisFalling(True)
                        Touch = True
                i += 1
        except:
            raise ValueError("Esperaba un objeto")

    def ColisionHorizontal(self, objeto: object):
        try:
            i=0
            Touch =False
            while i < len(ListaTotalBloques) and Touch ==False:
                if (objeto.y+16 > ListaTotalBloques[i][1] and objeto.y + 16 < ListaTotalBloques[i][1]+ ListaTotalBloques[i][3]) or (objeto.y > ListaTotalBloques[i][1] and objeto.y< ListaTotalBloques[i][1]+ListaTotalBloques[i][3]):
                    if objeto.x+16 > ListaTotalBloques[i][0] and objeto.x < (ListaTotalBloques[i][0]):
                        objeto.setx(ListaTotalBloques[i][0]-16)
                    elif objeto.x < (ListaTotalBloques[i][0]+ListaTotalBloques[i][2]) and objeto.x + 16 > (ListaTotalBloques[i][0]+ ListaTotalBloques[i][2]):
                        objeto.setx(ListaTotalBloques[i][0]+ListaTotalBloques[i][2])
                        Touch = True
                    else:
                        i+=1
                else:
                    i+=1
        except:
            raise ValueError("Esperaba un parametro de tipo objeto")


#Funcion que actualiza el juego, llamando a la actualizacion de cada uno de los objetos
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.__mario.update()
        self.ColisionVertical(self.__mario)
        self.ColisionHorizontal(self.__mario)
        for i in range(len(self.__enemigos)):
            self.__enemigos[i].updateEnemigo2()
            self.ColisionVertical(self.__enemigos[i])
            self.ColisionHorizontal(self.__enemigos[i])
        self.updateBloque()
        self.updateFondo()
        self.updateEnemigo()
        #self.ColisionVerticalEnemigo()

#Función que se encarga de dibujar cada uno de los elementos        
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
        pyxel.text(180, 20, str(tiempo_total - int(pyxel.frame_count/30) ), 7)
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

App()