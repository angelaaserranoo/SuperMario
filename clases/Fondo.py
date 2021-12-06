
#En el fondo se incluyen las montañas, nubes, arbustos
#cada uno con una posicion
class Fondo():
    def __init__(self, x, y= 184):
        self.__x = x
        self.__y = y
        
    def x(self):
        return self.__x

    def y(self):
        return self.__y  

#Funcion que hara que una vez que Mario alcance la mitad de la pantalla el fondo actualice su posicion
"""    def update(self):
        if App.mario.x()>= ancho_nivel/2:
            self.__x-=2
            """