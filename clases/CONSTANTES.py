import random
#Posicion inicial Mario
x0 = 75
#Altura a la que mario esta, es decir la del suelo
y0 = 168
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
#n_suelos = 5
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

ancho_nivel = 1000

#Lista con coordenadas de tuberías y sus dimensiones
ListaTuberiasAltas = [[150,136,32,48], [350,136,32,48], [600,136,32,48]]
ListaSuelos = [[0,184,138,16], [165,184,200,16]] #[180,184,200,16],[384,184,200,16],[0,184,200,16],[0,184,200,16]
ListaTuberiasBajas = [[250,152,32,32], [700, 152, 32, 32], [900, 152, 32, 32]]
ListaBloquesRompibles = [[0, 110, 16, 16], [560, 110, 16, 16], [ 760, 110, 16, 16], [850, 110, 16, 16]]
ListaBloquesSorpresa = [[16, 110, 16, 16], [576, 110, 16, 16], [ 776, 110, 16, 16], [866, 110, 16, 16]]
ListaBloquesDuros = [[32, 110, 16, 16], [592, 110, 16, 16], [ 792, 110, 16, 16], [882, 110, 16, 16]]

ListaTotal = []
for i in ListaTuberiasAltas:
    ListaTotal.append(i)
for i in ListaTuberiasBajas:
    ListaTotal.append(i)
for i in ListaSuelos:
    ListaTotal.append(i)
for i in ListaBloquesRompibles:
    ListaTotal.append(i)
for i in ListaBloquesSorpresa:
    ListaTotal.append(i)
for i in ListaBloquesDuros:
    ListaTotal.append(i)



world = (str(mundo)+ "-" +str(nivel))
tiempo_total = 400
#ancue = 146
vg=2