from CONSTANTES import *
class Colisiones:
    def __init__(self, objeto):
        self.__objeto = objeto

    def ColisionVertical (self, objeto: object):
        try:
            i=0
            Touch = False
            while i < len(ListaTotalBloques) and Touch ==False:
                if objeto.x+16 > ListaTotalBloques[i][0] and  (objeto.x < ListaTotalBloques[i][0] + ListaTotalBloques[i][2]):
                    if objeto.y+16 >= ListaTotalBloques[i][1] and objeto.y < ListaTotalBloques[i][1]:
                        objeto.setisFalling(False)
                        objeto.sety(ListaTotalBloques[i][1]-16)
                        objeto.setvy(0)
                        Touch =True
                    
                    elif objeto.y < (ListaTotalBloques[i][1]+ ListaTotalBloques[i][3]) and objeto.y + 16> (ListaTotalBloques[i][1]+ListaTotalBloques[i][3]):
                        objeto.sety(ListaTotalBloques[i][1]+ListaTotalBloques[i][3])
                        objeto.setisFalling(True)
                        Touch = True
                i += 1
        except:
            raise ValueError("Esperaba un objeto")

    def ColisionHorizontal(self, objeto: object):
        try:
            i=0
            Touch =False
            while i < len(ListaTotalBloques) and Touch ==False:
                if (self.__mario.y+16 > ListaTotalBloques[i][1] and self.__mario.y + 16 < ListaTotalBloques[i][1]+ ListaTotalBloques[i][3]) or (self.__mario.y > ListaTotalBloques[i][1] and self.__mario.y< ListaTotalBloques[i][1]+ListaTotalBloques[i][3]):
                    if self.__mario.x+16 > ListaTotalBloques[i][0] and self.__mario.x < (ListaTotalBloques[i][0]):
                        self.__mario.setx(ListaTotalBloques[i][0]-16)
                    elif self.__mario.x < (ListaTotalBloques[i][0]+ListaTotalBloques[i][2]) and self.__mario.x + 16 > (ListaTotalBloques[i][0]+ ListaTotalBloques[i][2]):
                        self.__mario.setx(ListaTotalBloques[i][0]+ListaTotalBloques[i][2])
                        Touch = True
                    else:
                        i+=1
                else:
                    i+=1
        except:
            raise ValueError("Esperaba un parametro de tipo objeto")
