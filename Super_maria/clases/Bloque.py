class  Bloque():
    #Se incluyen tuberias, suelo, y todos los tipos de bloques
    def __init__(self, x, y=130):
        self.__y = y
        self.__x = x

    def x(self):
        return self.__x

    def y(self):
        return self.__y