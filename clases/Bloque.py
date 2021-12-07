class  Bloque():
    #Se incluyen tuberias, suelo, y todos los tipos de bloques
    #Cada bloque tendra una posicion (tanto en x como en y), en principio será la del suelo pero podrá cambiarse
    def __init__(self, x, y, ancho, largo):
        self.__y = y
        self.__x = x
        self.__ancho =ancho
        self.__largo = largo

#funciones para obtener atributos privados
    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def ancho(self):
        return self.__ancho

    def largo(self):
        return self.__largo
    