import random
#Posicion inicial Mario
x0 = 75
#Altura a la que mario esta, es decir la del suelo
y0 = 50
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
#Cantidad de saltos entre suelos que habra en el nivel
n_suelos = 5
#Cantidad de nubes a lo largo del nivel
nubes = 5
#Numero de tuberias 
n_tuberias_bajas = 2
n_tuberias_altas = 3
#Numero de cada tipo de bloque 
n_bloques_rompibles= 5
n_bloques_sorpresa=2
n_bloques_duros= 9

#Cantidad de montañas a lo largo del nivel
n_montañas= 3
#La longitud de todo el nivel que tendra que recorrer el jugador
ancho_nivel= 800
largo_nivel =200

world= (str(mundo)+ "-" +str(nivel))
tiempo_total= 400