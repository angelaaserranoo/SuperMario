
#En el fondo se incluyen las montañas, nubes, arbustos
#cada uno con una posicion
class Fondo():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y  

