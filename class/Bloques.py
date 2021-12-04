class  Bloque():
    #Se incluyen todos los tipos de bloques, la tuberia y el suelo
    #kind sera un boolean que determinara si la colision con mario tiene o no consecuencia
    def __init__(self, x, y, kind):
        self.__x=x
        self.__y=y
        self.__kind=kind
        