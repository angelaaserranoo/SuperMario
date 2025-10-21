#Importamos todas las clases
import pyxel
from Jugador import *
from CONSTANTES import *
from Enemigo import *
from Bloque import *
from Fondo import *
from Fondo import Fondo
from Enemigo import *
from Especial import *
from pathlib import Path

class App():
#Definimos cada atributo, siendo cada uno objetos de otras clases
    def __init__(self):
        self.__mario = Jugador()
        #Funcion que contiene el resto de atributos
        self.ResetApp()
        #Definimos el tamaño y el nombre de la ventana
        pyxel.init(200, 200, title = "Mario Bros")
        #Cargamos la imagen al banco        
        _ASSETS = Path(__file__).resolve().parent.parent / "assets" / "mario_assets.pyxres"
        pyxel.load(str(_ASSETS))
        #se ejecuta el programa llamando continuamente a las funciones draw y update
        pyxel.run(self.update, self.draw)
    
#Función que genera los elementos del fondo y les atribuye una posicion a cada uno
    def CrearFondo(self, Lista):
        try:
            ListaObjetosFondo = []
            #Recorro la lista introducida por parametro
            for i in Lista:
                #Genero un objeto de tipo fondo a partir de sus elementos y lo agrego a otra lista
                ListaObjetosFondo.append(Fondo(i[0], i[1]))
            #Devuelvo lista (lista de objetos)
            return ListaObjetosFondo
        except:
            raise ValueError("Esperaba una lista")

#Función que actualiza el fondo
    def updateFondo(self):
        #Si mario supera la mitad de la pantalla y sigue avanzando el fondo se mueve en sentido contrario
        if self.__mario.x >=100 and (pyxel.btn(pyxel.KEY_RIGHT)):
            for i in self.__ListaTotalFondo:
                i.setx(i.x-2)

#Función que crea una lista de objetos de tipo bloque y los posiciona a lo largo del mapa
    def CrearBloque(self, Lista):
        try:
            #Misma logica que en CrearFondo, en este caso el bloque requiere mas parametros
            ListaObjetosBloque = []
            for i in Lista:
                ListaObjetosBloque.append(Bloque(i[0], i[1], i[2], i[3], i[4]))
            return ListaObjetosBloque
        except:
            raise ValueError("Esperaba una lista")
    
#Si mario supera la mitad de la pantalla y sigue avanzando los bloques se mueven en sentido contrario
    def updateBloque(self):
        if self.__mario.x >=100 and (pyxel.btn(pyxel.KEY_RIGHT)):
            for i in self.__ListaTotalBloques:
                i.setx(i.x-2)
    
#Metodo parecido a CrearBloque o CrearFondo
    def CrearSorpresa(self, x, y):
        #El numero aleatorio indica el tipo de objeto que saldrá
        item_especial = Especial(x, y, ancho_especial, alto_especial, random.randint(0,1))
        self.__sorpresas.append(item_especial)
        
    def updateSorpresa(self):
        #Si mario supera la mitad de la pantalla y sigue avanzando las sorpresas se mueven en sentido contrario
        for i in self.__sorpresas:
            if self.__mario.x >=100 and (pyxel.btn(pyxel.KEY_RIGHT) ):
                i.setx(i.x-2)

        #Mario colisiona con el objeto
            if (self.__mario.x + self.__mario.ancho < i.x+i.ancho and self.__mario.x + self.__mario.ancho > i.x) or (self.__mario.x < i.x+i.ancho and self.__mario.x > i.x):
                if i.y + (i.alto/2) < self.__mario.y+self.__mario.alto and i.y + (i.alto/2)> self.__mario.y:
                    #El objeto es una moneda
                    if i.kind== 1:
                        #Genero la moneda
                        self.__mario.setScore(self.__mario.score + 100)
                        self.__mario.setMonedas(self.__mario.monedas + 1)
                        self.__sorpresas.pop(self.__sorpresas.index(i))
                    elif i.kind == 0:
                        #Si es el otro objeto y mario es normal
                        if self.__mario.kind ==1:
                            #Lo convierto a SuperMario
                            self.__mario.setalto(alto_SMario)
                            self.__mario.setancho(ancho_SMario)
                            self.__mario.setkind(2)
                            #Elimino la sorpresa
                            self.__sorpresas.pop(self.__sorpresas.index(i))
                        #Si es SuperMario y tengo la flor
                        elif self.__mario.kind ==2:
                            #Me hago mario de fuego
                            self.__mario.setkind(3)
                            self.__sorpresas.pop(self.__sorpresas.index(i))

    def CrearEnemigo(self):
        #Genero numero aleatorio para crear un GOOMBA o un KOOPA
        posibilidad = random.randint(0,3)
        #Genero posicion aleatoria
        x_random = random.randint(200, 300)
        contador = 0
        while contador != len(self.__enemigos):
            #Compruebo que en la posicion generada no haya otro enemigo ya existente
            if not(x_random > self.__enemigos[contador].x+self.__enemigos[contador].ancho or x_random+ ancho_enemigo < self.__enemigos[contador].x):
                x_random = random.randint(200, 300)
                contador = 0
            else:
                contador += 1
        #Si cumple la posibilidad 1/4 será un koopa
        if posibilidad == 0:
            self.__enemigos.append(Enemigo(x_random, 100, ancho_koopa, alto_koopa, True))
        #Sino un goomba
        else:
            self.__enemigos.append(Enemigo(x_random, 100, ancho_goomba, alto_goomba))

    def updateEnemigo(self):
        for i in self.__enemigos:
            if i.tiempo_muerte < 45:
                #Primero colisión enemigo con objetos sólidos
                self.ColisionVertical(i)
                self.ColisionHorizontal(i)
                #Colisión enemigo con Jugador
                #pos x de mario = pos x de enemigo
                if self.__mario.x+self.__mario.ancho > i.x and self.__mario.x < i.x + ancho_enemigo and self.__mario.x < i.x+i.ancho:
                    #Comprobamos si el enemigo es un Goomba o un Koopa
                    if i.is_walking == None and i.is_alive:
                        #Mario aplasta enemigo
                        if self.__mario.y+ self.__mario.alto > i.y and self.__mario.y+ self.__mario.alto < (i.y+ i.alto):
                            i.setisAlive(False)
                            self.__mario.setScore(self.__mario.score + score)
                            i.setvx(0)
                            i.setalto(6)
                            self.__mario.setvy(-3)
                            i.settiempoMuerte(pyxel.frame_count)
                        #Mario es colisionado por Goomba
                        elif self.__mario.y <= i.y and self.__mario.y+self.__mario.alto>= i.y:
                            self.__mario.setvy(self.__mario.vy  -2)
                            self.__mario.setkind(self.__mario.kind-1)
                    #KOOPA
                    elif i.is_walking == True:
                        #Mario aplasta al koopa
                        if self.__mario.y+self.__mario.alto > i.y and self.__mario.y+self.__mario.alto < (i.y+ i.alto):
                            self.__mario.setvy(self.__mario.vy -2)
                            i.setisWalking(False)
                            self.__mario.setScore(self.__mario.score+100)
                            i.setalto(alto_concha)
                            i.setvx(0)
                            if self.__mario.x + self.__mario.ancho > i.x and self.__mario.x + self.__mario.ancho < i.x + i.ancho:
                                self.__mario.setx(i.x -self.__mario.ancho)
                            else:
                                self.__mario.setx(i.x +i.ancho)
                        #Mario es colisionado por el koopa
                        elif (self.__mario.y < i.y and self.__mario.y+self.__mario.alto > i.y) or (self.__mario.y> i.y and self.__mario.y < i.y + i.alto):
                            self.__mario.setvy(self.__mario.vy  - 2)
                            self.__mario.setkind(self.__mario.kind - 1)
                    elif i.is_walking == False:
                        if self.__mario.y+self.__mario.alto == i.y+i.alto:
                            self.__mario.setScore(self.__mario.score + (4*score))
                            if i.vx ==0:
                                i.setx(self.__mario.x +self.__mario.ancho)
                                if self.__mario.vx > 0:
                                    i.setvx(3)
                                elif self.__mario.vx < 0:
                                    i.setvx(-3)
                            else:
                                self.__mario.setvy(self.__mario.vy  -2)
                                self.__mario.setkind(self.__mario.kind-1)

                #Colisión entre enemigos
                for j in self.__enemigos:
                    if i != j:
                        #Compruebo que los enemigos esten a la misma altura al colisionar
                        if ((i.x + i.ancho > j.x and i.x < j.x+j.ancho)or (j.x + j.ancho > i.x and j.x < i.x+i.ancho)) and  i.y + (i.alto/2) < j.y+j.alto and i.y + (i.alto/2)> j.y: 
                            #Si uno de ellos es una concha que se esta moviendo
                            if (j.is_walking == False and j.vx != 0) :
                                #Mato al otro enemigo sin importar que sea
                                i.setisAlive(False)
                                i.settiempoMuerte(pyxel.frame_count)
                                self.__mario.setScore(self.__mario.score +500)
                            elif i.is_walking == False and i.vx != 0:
                                j.setisAlive(False)
                            elif j.is_walking!=False:
                                i.setvx(-i.vx)
                                j.setvx(-j.vx)


            #Actualización posición enemigo respecto al jugador
            if self.__mario.x >=100 and (pyxel.btn(pyxel.KEY_RIGHT)):
                i.setx(i.x - 2)
            #Si desaparecen los enemigos
            if i.x<-i.ancho or i.y>230:
                #Se eliminan y se crea uno nuevo
                self.__enemigos.pop(self.__enemigos.index(i))
                self.CrearEnemigo()
            #Si han pasado mas de 50 frames desde la muerte de un enemigo lo eliminamos
            if not i.is_alive and i.tiempo_muerte+50< pyxel.frame_count:
                self.__enemigos.pop(self.__enemigos.index(i))
                self.CrearEnemigo()
            #Actualizo posicion x
            i.setx(i.x+i.vx)
            #Actualizo posicion y
            i.updateEnemigo2()

    def ColisionVertical(self, objeto: object):
        try:
            i=0
            Touch = False
            #bucle que recorre cada uno de los objetos colisionables estaticos
            while i < len(self.__ListaTotalBloques) and Touch == False:
                #Compuebo si el objeto introducido por parametro comparte posicion x con alguno de los bloques
                if objeto.x+objeto.ancho> self.__ListaTotalBloques[i].x and (objeto.x < self.__ListaTotalBloques[i].x + self.__ListaTotalBloques[i].ancho):
                    #Compruebo si el final del cuerpo de mario esta entrando en el bloque 
                    if objeto.y+ objeto.alto >= self.__ListaTotalBloques[i].y and objeto.y < self.__ListaTotalBloques[i].y:
                        #Desactivo la gravedad
                        objeto.setisFalling(False)
                        #Corrijo posicion del objeto para que aparente estar apoyado en el suelo
                        objeto.sety(self.__ListaTotalBloques[i].y-objeto.alto)
                        objeto.setvy(0)
                        #Dejo de ejecutar el bucle
                        Touch = True
                    #Compruebo si el objeto a colisionado con la cabeza
                    elif objeto.y < (self.__ListaTotalBloques[i].y+ self.__ListaTotalBloques[i].alto) and objeto.y + objeto.alto > (self.__ListaTotalBloques[i].y+self.__ListaTotalBloques[i].alto):
                        #Corrijo posicion
                        objeto.sety(self.__ListaTotalBloques[i].y+self.__ListaTotalBloques[i].alto)
                        #Le hago caer
                        objeto.setvy(3)
                        objeto.setisFalling(True)
                        Touch = True
                        #si el bloque colisionado es rompible
                        if self.__ListaTotalBloques[i].rompible == True:
                            #Si pertenece a los bloques sorpresa
                            if self.__ListaTotalBloques[i] in self.__bloques_sorpresa and not self.__ListaTotalBloques[i].roto:
                                #Cambio su apariencia en el draw
                                self.__ListaTotalBloques[i].setroto(True)
                                #Creo sorpresa en la posicion del bloque 
                                self.CrearSorpresa(self.__ListaTotalBloques[i].x, self.__ListaTotalBloques[i].y-alto_especial)
                            #Si pertenece a los bloques duros y no esta roto
                            elif self.__ListaTotalBloques[i] in self.__bloques_duros and not self.__ListaTotalBloques[i].roto:
                                #Sumo al marcador y agrego una colision
                                    self.__mario.setMonedas(self.__mario.monedas+1)
                                    self.__mario.setScore(self.__mario.score+ score)
                                    self.__ListaTotalBloques[i].set_n_colisiones(self.__ListaTotalBloques[i].n_colisiones+1)
                                    #En la quinta colision el bloque se rompe
                                    if self.__ListaTotalBloques[i].n_colisiones==5:
                                        self.__ListaTotalBloques[i].setroto(True)
                            #Si pertenece a los rompibles y soy SuperMario o Mario de fuego
                            elif self.__ListaTotalBloques[i] in self.__bloques_rompibles and (self.__mario.kind == 2 or self.__mario.kind == 3):
                                #Actualizo apariencia y elimino el objeto para que no colision mas
                                self.__ListaTotalBloques[i].setroto(True)
                                self.__ListaTotalBloques.pop(i)
                i += 1
        except:
            raise ValueError("Esperaba un objeto")

    def ColisionHorizontal(self, objeto: object):
        try:
            i=0
            Touch =False
            #Mismo procedimiento que en Colision Vertical intercambiando las x por las y
            while i < len(self.__ListaTotalBloques) and Touch ==False:
                if (objeto.y+objeto.alto > self.__ListaTotalBloques[i].y and objeto.y+objeto.alto < self.__ListaTotalBloques[i].y+ self.__ListaTotalBloques[i].alto) or (objeto.y > self.__ListaTotalBloques[i].y and objeto.y < self.__ListaTotalBloques[i].y+self.__ListaTotalBloques[i].alto):
                    if objeto.x+objeto.ancho > self.__ListaTotalBloques[i].x and objeto.x < (self.__ListaTotalBloques[i].x):
                        #Corrijo Posicion
                        objeto.setx(self.__ListaTotalBloques[i].x-objeto.ancho)
                        objeto.setvx(objeto.vx*-1)
                        if self.__ListaTotalBloques[i] in self.__castillo:
                            self.__mario.setkind(4)
                    elif objeto.x < (self.__ListaTotalBloques[i].x+self.__ListaTotalBloques[i].ancho) and objeto.x + objeto.ancho > (self.__ListaTotalBloques[i].x+ self.__ListaTotalBloques[i].ancho):
                        #Corrijo Posicion
                        objeto.setx(self.__ListaTotalBloques[i].x+self.__ListaTotalBloques[i].ancho)
                        objeto.setvx(objeto.vx*-1)
                        Touch = True
                    else:
                        i+=1
                else:
                    i+=1
        except:
            raise ValueError("Esperaba un parámetro de tipo objeto")

    def ResetApp(self):
        #Definicion de cada uno de los atributos de la clase App que deben reiniciarse en algun momento del juego
        self.__suelo = self.CrearBloque(ListaSuelos)
        self.__nubes = self.CrearFondo(ListaNubes)
        self.__montañas = self.CrearFondo(ListaMontañas)
        self.__castillo = self.CrearBloque(ListaCastillo)
        self.__arbustos = self.CrearFondo (ListaArbustos)
        self.__bloques_rompibles = self.CrearBloque(ListaBloquesRompibles)
        self.__bloques_sorpresa = self.CrearBloque(ListaBloquesSorpresa)
        self.__bloques_duros = self.CrearBloque(ListaBloquesDuros)
        self.__tuberias_altas = self.CrearBloque(ListaTuberiasAltas)
        self.__tuberias_bajas = self.CrearBloque(ListaTuberiasBajas)
        self.__sorpresas = []
        self.__ListaTotalFondo = []
        self.__ListaTotalBloques = []
        for i in self.__nubes:
            self.__ListaTotalFondo.append(i)
        for i in self.__montañas:
            self.__ListaTotalFondo.append(i)
        for i in self.__arbustos:
            self.__ListaTotalFondo.append(i)
        for i in self.__suelo:
           self.__ListaTotalBloques.append(i)
        for i in self.__tuberias_altas:
            self.__ListaTotalBloques.append(i)
        for i in self.__tuberias_bajas:
            self.__ListaTotalBloques.append(i)
        for i in self.__bloques_rompibles:
            self.__ListaTotalBloques.append(i)
        for i in self.__bloques_sorpresa:
            self.__ListaTotalBloques.append(i)
        for i in self.__bloques_duros:
            self.__ListaTotalBloques.append(i)
        for i in self.__castillo:
            self.__ListaTotalBloques.append(i)
        self.__enemigos = []
        for i in range(n_enemigos_activos):
            self.CrearEnemigo()

#Funcion que actualiza el juego, llamando a la actualizacion de cada uno de los objetos
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        #Si mario esta vivo Atualizo
        if self.__mario.kind >0 and self.__mario.kind<4:
            #Metodo de Jugador que actua en forma de gravedad
            self.__mario.update()
            #Comprobamos colision con mario y objetos estaticos
            self.ColisionVertical(self.__mario)
            self.ColisionHorizontal(self.__mario)
            #Actualizamos posiciones de los objetos si mario avanza
            self.updateBloque()
            self.updateFondo()
            #Colisiones de los enemigos
            self.updateEnemigo()
            self.updateSorpresa()
        #Si mario muere
        elif self.__mario.kind == 0:
            #le quitamos una vida y reseteamos el nivel
            self.__mario.set_n_vidas(self.__mario.n_vidas -1)
            self.__mario.Reset()
            self.ResetApp()


#Función que se encarga de dibujar cada uno de los elementos        
    def draw(self):
        if self.__mario.n_vidas ==0:
            pyxel.cls(pyxel.frame_count %16)
            pyxel.text(80, 20, "GAME OVER", 7)
            pyxel.blt(90, 100, 1, 0, 49, 16, 16, 12)
        elif self.__mario.kind==4:
            pyxel.cls(pyxel.frame_count %16)
            pyxel.text(80, 20, "NIVEL SUPERADO", 7)
            pyxel.blt(90, 100, 1, 0, 49, 16, 16, 12)
        elif self.__mario.n_vidas>0:
            #Dibuja fondo color azul
            pyxel.cls(5)
            #Montañas
            for j in self.__montañas:
                pyxel.blt(j.x, j.y, 0, 0, 193, 74,34, 12)
            #Nubes 
            for j in self.__nubes:
                pyxel.blt(j.x, j.y, 0, 107, 138, 48 ,21, 12)
            #Arbustos
            for j in self.__arbustos:
                pyxel.blt(j.x, j.y, 0, 139, 46, 61,15, 12)
            for j in self.__castillo:
                pyxel.blt(j.x, j.y, 0, 150, 158, 77,69, 12)
            #Suelo
            for j in self.__suelo:
                pyxel.blt(j.x, j.y, 0, 12, 227, j.ancho, j.alto, 12)
            #Tuberias altas
            for j in self.__tuberias_altas:
                pyxel.blt(j.x, j.y, 0, 79, 178, j.ancho, j.alto, 12)
            #Tuberias bajas
            for j in self.__tuberias_bajas:
                pyxel.blt(j.x, j.y, 0, 38, 132, j.ancho, j.alto, 12)
            #Bloques rompibles
            for j in self.__bloques_rompibles:
                if not j.roto:
                    pyxel.blt(j.x, j.y, 0, 89, 160, j.ancho, j.alto, 12)
            #Bloques duros
            for j in self.__bloques_duros:
                if j.roto:
                    pyxel.blt(j.x, j.y, 0, 145, 27, j.ancho, j.alto, 12)
                else:
                    pyxel.blt(j.x, j.y, 0, 89, 160, j.ancho, j.alto, 12)
            #Bloques Sorpresa
            for j in self.__bloques_sorpresa:
                #Apariencia si el glope no se ha golpeado
                if not j.roto:
                    pyxel.blt(j.x, j.y, 0, 177, 27, j.ancho, j.alto, 12)
                
                #Apariencia si el glope se ha golpeado
                else:
                    pyxel.blt(j.x, j.y, 0, 145, 27, j.ancho, j.alto, 12)
            #Pinto sorpresas
            for j in self.__sorpresas:
                if j.kind == 1 :
                    pyxel.blt(j.x, j.y, 0,0, 28, j.ancho,j.alto, 12 )
                elif j.kind ==0 and self.__mario.kind == 1:
                    pyxel.blt(j.x, j.y, 0, 0, 44, j.ancho, j.alto, 12)
                elif j.kind == 0 and self.__mario.kind ==2:
                    pyxel.blt(j.x, j.y, 0,56, 47, j.ancho,j.alto, 12 )


            #ENEMIGOS
            for j in self.__enemigos:
                #Goomba
                if j.is_walking == None:
                    if j.tiempo_muerte > 0:
                        pyxel.blt(j.x, j.y, 1, 0, 25, 12, 6, 12)
                    else:
                        pyxel.blt(j.x, j.y, 1, 0, 0, j.ancho, j.alto, 12)
                #Koopa
                elif j.is_walking == True:
                    if j.tiempo_muerte > 0:
                        pyxel.blt(j.x, j.y, 1, 16, 24, j.ancho, j.alto, 12)
                    else:
                        pyxel.blt(j.x, j.y, 1, 32, 0, j.ancho, j.alto, 12)
                elif j.is_walking == False and j.is_alive:
                    pyxel.blt(j.x, j.y, 1, 16, 0, j.ancho, j.alto, 12)

            #Imprime un texto que indica el Mundo y el nivel actual
            pyxel.text(120, 10, "WORLD ", 7)
            pyxel.text(120, 20, world, 7)
            #Imprime la puntuacion de Mario
            pyxel.text(20, 10, "MARIO", 7)
            pyxel.text(20, 20, str(self.__mario.score), 7)
            #Imprime simbolo moneda
            pyxel.blt(65, 5, 0, 2, 29, 9, 13, 12)
            #Imprime valor moneda
            pyxel.text (80, 10, "X", 7)
            pyxel.text(90, 10, str(self.__mario.monedas), 7 )
            #Imprime tiempo restante (encabezado)
            pyxel.text(160, 10, "TIME", 7)
            #Imprimer tiempo restante (Fatlta hacer que sea entero y no float)
            pyxel.text(180, 20, str(tiempo_total - int((pyxel.frame_count - self.__mario.tiempo)/30) ), 7)
            #Dibuja Mario
            if self.__mario.kind ==1:
                if self.__mario.vy < 0 or self.__mario.isFalling:
                    #Dibuja el Mario que salta
                    pyxel.blt(self.__mario.x, self.__mario.y, 0, 0, 79, self.__mario.ancho, self.__mario.alto, 12)
                else:
                    if len(self.__mario.isMoving) <= 5:
                        if len(self.__mario.isMoving) == 0:
                            #Diuja el Mario en reposo
                            pyxel.blt(self.__mario.x, self.__mario.y, 0, 0, 97, self.__mario.ancho, self.__mario.alto, 12)
                        else:
                            #Dibuja el Mario que anda hacia la derecha
                            pyxel.blt(self.__mario.x, self.__mario.y, 0, 18, 98, self.__mario.ancho, self.__mario.alto, 12)
                    else:
                        #Dibuja el Mario en reposo
                        pyxel.blt(self.__mario.x, self.__mario.y, 0, 0, 97, self.__mario.ancho, self.__mario.alto, 12)
            elif self.__mario.kind ==2:
                #pyxel.blt(self.__mario.x, self.__mario.y, 0, 56, 81, self.__mario.ancho, self.__mario.alto, 12)
                if self.__mario.vy < 0 or self.__mario.isFalling:
                    #Dibuja el Mario que salta
                    pyxel.blt(self.__mario.x, self.__mario.y, 0, 147, 79, self.__mario.ancho, self.__mario.alto, 12)
                else:
                    if len(self.__mario.isMoving) <= 5:
                        if len(self.__mario.isMoving) == 0:
                            #Diuja el Mario en reposo
                            pyxel.blt(self.__mario.x, self.__mario.y, 0, 54, 81, self.__mario.ancho, self.__mario.alto, 12)
                        else:
                            #Dibuja el Mario que anda hacia la derecha
                            pyxel.blt(self.__mario.x, self.__mario.y, 0, 87, 81, self.__mario.ancho, self.__mario.alto, 12)
                    else:
                        #Dibuja el Mario en reposo
                        pyxel.blt(self.__mario.x, self.__mario.y, 0, 54, 81, self.__mario.ancho, self.__mario.alto, 12)
            
            elif self.__mario.kind ==3:
                pyxel.blt(self.__mario.x, self.__mario.y, 0, 168, 81, self.__mario.ancho, self.__mario.alto, 12)

App()