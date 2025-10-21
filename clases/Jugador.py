from CONSTANTES import *
import pyxel
import time

class Jugador():#Definira al objeto Mario con su posicion, velocidad, dimensiones, el marcador que se le atribuye (tiempo, monedas y vidas)
    def __init__(self):
        self.__x = x0
        self.__y = y0
        self.__ancho = ancho_mario
        self.__alto = alto_mario
        self.__vx = 0
        self.__vy = vy0
        self.__score = score0
        self.__n_vidas = n_vidas
        self.__monedas = monedas0
        #Jugador tiene 4 estados (muerto, mario, super mario, mario de fuego) el kind será un numero entre 0 y 3 que definira su estado
        self.__kind = kind
        #Utilizado para la parte grafica
        self.__isMoving = []
        #Define si se le esta aplicando o no gravedad al objeto 
        self.__isFalling = False
        #Utilizado para el marcador
        self.__tiempo = 0
    @property
    def x(self):
        return self.__x

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
    def vx(self):
        return self.__vx
    
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
    
    @property
    def n_vidas(self):
        return self.__n_vidas

    @property
    def kind(self):
        return self.__kind


    def setx(self, value):
        self.__x = value

    def setvx(self, value):
        self.__vx = value

    def sety(self,value):
        self.__y = value
    
    def setvy(self, value):
        self.__vy = value

    def setkind(self,value):
        #Si Mario cambia entre mario, SuperMario y Mario de fuego sus dimensiones tambien lo hacen y asi se define en este metodo
        self.__kind = value
        if value==1:
            #Cambio dimensiones Mario normal
            self.setalto(alto_mario)
            self.setancho(ancho_mario)
        elif value== 2:
            #Cambio dimensiones SuperMario
            self.setalto(alto_SMario)
            self.setancho(ancho_SMario)
        elif value== 3:
            #Cambio dimensiones que juston coinciden con las de SMario. Esto s epuede modificar desde el fichero constantes
            self.setalto(alto_SMario)
            self.setancho(ancho_SMario)


    def setancho(self, value):
        self.__ancho = value

    def setalto(self, value):
        self.__alto = value

    def setScore(self, value):
        self.__score = value

    def setisFalling(self, value):
        self.__isFalling = value

    def setMonedas(self, value):
        self.__monedas = value
    
    def set_n_vidas(self, value):
        self.__n_vidas = value

    def Reset(self):
        #Metodo utilizado para matar a reiniciar los valores de Mario a los definidos en el constructor
        self.__x = x0
        self.__y = y0
        self.__ancho = ancho_mario
        self.__alto = alto_mario
        self.__vx = 0
        self.__vy = vy0
        #Se omiten los valores del marcador para que sean constante a lo largo de la partida
        #Jugador tiene 4 estados (muerto, mario, super mario, mario de fuego), el kind será un numero entre 0 y 3 que definira su estado
        self.__kind = kind
        self.__isMoving = []
        self.__isFalling = False
        self.__tiempo = pyxel.frame_count
    
    def update(self):
        #Actualizo la posicion a partir de la velocidad
        self.__y += self.__vy
        #Si mario sale de la pantalla por abajo o se termina el tiempo...
        if self.__y > 250 or (pyxel.frame_count > 30*tiempo_total):
            #El kind de Mario se hace cero, es decir, muere
            self.setkind(0)
        #MOVER IZQUIERDA
        #Compruebo si se esta presionando la tecla indicada
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            #Modifico posicion y velocidad
            self.__x = max(self.__x-2, 0)
            self.__vx = -2
            """El atributo isMoving es una lista a la cual se le van agregando booleanos en caso de presionar la tecla derecha 
            o izquierda. En el momento que la lista alcanza los 9 elementos se limpia, esto tiene implicaciones futuras que veremos mas adelante """
            if len(self.__isMoving) <= 8:
                self.__isMoving.append(True)
            else:
                self.__isMoving.clear()

        #MOVER DERECHA
        #Misma funcion que el anterior pero moviendose hacia la derecha
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            #Corrijo posicion y velocidad
            self.__x = min(self.__x+2, 100)
            self.__vx = 2
            if len(self.__isMoving) <= 8:
                self.__isMoving.append(True)
            else:
                self.__isMoving.clear()

        else:
            self.__isMoving.clear()
            self.__vx = 0

        #SALTO
        #Define que ocurre con la gravedad. Tiene una gran relevancia en las colisiones 
        if self.__isFalling == False:
            #Si no esta cayendo y me dicen que salte
            if pyxel.btn(pyxel.KEY_UP) == True or pyxel.btn(pyxel.GAMEPAD_1_UP) == True:
                #Corrijo posiciones solo si no ha alcanzado el maximo salto
                if self.__vy > -7:
                    self.__vy -= 1
                    self.__y += self.__vy
                #Si ha saltado el maximo aunque siga presionando se definira que esta cayendo
                else:
                    self.__isFalling = True
            #Si no salta, esta cayendo        
            else:
                self.__isFalling = True
        #Si decimos que esta cayendo
        else:
            #Se le asocia una velocidad que actua en forma de gravedad
            self.__vy = min(self.__vy+1, 9)
        
        #Funcionalidad extra para facilitar observaciones puntuales en el juego
        if pyxel.btn(pyxel.KEY_R)== True:
            self.Reset()