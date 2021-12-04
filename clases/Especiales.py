class Especial():
    #defino todos los objetos especiales a partir de su
    #posicion, velocidad y si vienen o no de un ladrillo
    def __init__(self, x,y , vy, es_ladrillo):
        self.__x=x
        self.__y=y
        self.__vy=vy
        self.__es_ladrillo=es_ladrillo

