import pyxel 
from Jugador import *
from CONSTANTES import *
from Enemigo import *
from Bloque import *
from Fondo import *

class App():

    def __init__(self):
        self.__mario = Jugador()
        self.__suelo = self.CrearSuelo(n_suelos)
        self.__nubes = self.CrearNubes(n_nubes)
        self.__tuberias = self.CrearTuberias(n_tuberias)
        pyxel.init(160, 160, caption = "Mario Bros")
        pyxel.load(r'C:\Users\anaja\Documents\Super_maria\assets\mario_assets.pyxres')
        pyxel.run(self.update, self.draw)

    def CrearSuelo(self, n_suelos):
        lista = []
        for i in range(n_suelos):
            x = Bloque(i * 200)
            lista.append(x)
        return lista

    def CrearNubes(self, n_nubes):
        lista = []
        for i in range(n_nubes):
            lista.append(Fondo ((i*640)/n_nubes, 30))
        return lista

    def CrearTuberias(self, n_tuberias):
        lista = []
        for j in range(n_tuberias):
            x = Bloque((j*640)/n_tuberias)
            lista.append(x)
        return lista
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.__mario.update()
        
    def draw(self):
        pyxel.cls(5)
        for i in self.__suelo:
            pyxel.blt(i.x(), 134, 0, 0, 115, 177, 15, 12)
        for j in self.__nubes:
            pyxel.blt(j.x(), j.y(), 0, 139, 47, 61,14, 12 )
        for j in self.__tuberias:
            """
            if j == self.__tuberias[0]:
                pass
            else:
                """
            pyxel.blt(j.x(), 103, 0, 38, 132, 32, 31, 8)    
        pyxel.blt(self.__mario.x(), self.__mario.y(), 0, 0, 96, 16, 16, 12)    
        
App()  