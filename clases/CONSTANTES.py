import random
#Posicion inicial Mario
x0 = 75
#Altura a la que mario esta, es decir la del suelo
y0 = 60
#velocidad inicial Mario en y
vy0 = 0
#Puntos iniciales
score0 = 0
#Valor inicial de monedas
monedas0 = 0
#Especificaciones del juego
mundo = 1
nivel = 1
#Estado de Mario al inicio del juego
kind = 1
#Vidas iniciales Mario
n_vidas = 3
#Dimensiones super mario
alto_SMario= 32
ancho_SMario = 16
#Dimensiones mario
alto_mario=16
ancho_mario = 16
#Dimensiones Enemigo
ancho_enemigo= 16
ancho_goomba=16
alto_goomba=16
ancho_koopa=16
alto_koopa=23
alto_concha =16
#Dimension elementos especiales
ancho_especial=16
alto_especial=16
#Puntuacion sumada por colision con enemigos
score= 100
#Numero de enemigos visibles a la vez
n_enemigos_activos = 4
#cadena de texto que imprime
world = (str(mundo)+ "-" +str(nivel))
#Tiempo total maximo para pasar nivel
tiempo_total = 400

#Elementos del fondo con sus posiciones
ListaNubes =[[0, 40], [100, 40], [150, 40], [300, 40], [460, 40], [560, 40], [760, 40], [940, 40]]
ListaMontañas = [[15, 155], [200, 160], [250, 150], [560, 160],[760, 155], [940, 150]]
ListaArbustos = [[95, 169], [330, 169], [650, 169],[840, 169]]


#Lista de bloques con sus posiciones, dimensiones y el atributo rompible
ListaTuberiasAltas = [[350,138,32,48, False], [450,138,32,48,False], [620,138,32,48,False]]
ListaSuelos = [[0,184,150,16,False], [150,184,100,16,False], [250,184,200,16,False], [450,184,230,16,False], [700,184,200,16,False], [900,184,200,16,False], [1150, 184, 240, 16,False]]
ListaTuberiasBajas = [[280,154,32,32,False], [700, 154, 32, 32,False], [930, 154, 32, 32,False]]
ListaBloquesRompibles = [[200, 110, 16, 16, True], [550, 110, 16, 16, True], [ 760, 110, 16, 16, True], [850, 110, 16, 16, True]]
ListaBloquesSorpresa = [[216, 110, 16, 16,True], [566, 110, 16, 16,True], [ 776, 110, 16, 16,True], [866, 110, 16, 16,True]]
ListaBloquesDuros = [[232, 110, 16, 16,True], [582, 110, 16, 16,True], [ 792, 110, 16, 16,True], [882, 110, 16, 16,True]]
ListaCastillo = [[1310, 116, 77, 69, False]]




