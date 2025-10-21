class Especial():
    #Defino todos los objetos especiales a partir de su posición
    def __init__(self, x, y, ancho, alto, kind):
        self.__x = x
        self.__y = y
        self.__vx = 0
        self.__ancho = ancho
        self.__alto = alto
        self.__kind = kind

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def vx(self):
        return self.__vx

    @property
    def ancho(self):
        return self.__ancho

    @property
    def alto(self):
        return self.__alto

    @property
    def kind(self):
        return self.__kind

    def setx(self, value):
        self.__x = value

    def sety(self, value):
        self.__y = value

    def setvx(self, value):
        self._vx= value