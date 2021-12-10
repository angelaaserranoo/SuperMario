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
#Ancho del nivel en px
ancho_nivel = 1000

n_enemigos_activos = 4
posx_enemigos = []
for i in range (n_enemigos_activos):
    a = random.randint (200, 400)
    posx_enemigos.append(a)

ListaNubes =[[0, 40], [100, 40], [150, 40], [300, 40], [460, 40], [560, 40], [760, 40], [940, 40]]
ListaMontañas = [[15, 155], [200, 160], [250, 150], [560, 160],[760, 155], [940, 150]]
ListaArbustos = [[95, 169], [330, 169], [650, 169],[840, 169]]
ListaTotalFondo= []
for i in ListaNubes:
    ListaTotalFondo.append(i)
for i in ListaMontañas:
    ListaTotalFondo.append(i)
for i in ListaArbustos:
    ListaTotalFondo.append(i)


#Lista con coordenadas de tuberías y sus dimensiones
ListaTuberiasAltas = [[350,138,32,48], [450,138,32,48], [620,138,32,48]]
#Cambiar primer suelo a i[3] = 120 cuando termine colisiones
ListaSuelos = [[0,184,147,16], [147,184,35,16], [200,184,200,16], [420,184,230,16], [675,184,210,16], [900,184,200,16], [1150, 184, 240, 16]]
ListaTuberiasBajas = [[280,154,32,32], [700, 154, 32, 32], [900, 154, 32, 32]]
ListaBloquesRompibles = [[200, 110, 16, 16], [550, 110, 16, 16], [ 760, 110, 16, 16], [850, 110, 16, 16]]
ListaBloquesSorpresa = [[216, 110, 16, 16], [566, 110, 16, 16], [ 776, 110, 16, 16], [866, 110, 16, 16]]
ListaBloquesDuros = [[232, 110, 16, 16], [582, 110, 16, 16], [ 792, 110, 16, 16], [882, 110, 16, 16]]

ListaTotalBloques = []
for i in ListaSuelos:
    ListaTotalBloques.append(i)
for i in ListaTuberiasAltas:
    ListaTotalBloques.append(i)
for i in ListaTuberiasBajas:
    ListaTotalBloques.append(i)
for i in ListaBloquesRompibles:
    ListaTotalBloques.append(i)
for i in ListaBloquesSorpresa:
    ListaTotalBloques.append(i)
for i in ListaBloquesDuros:
    ListaTotalBloques.append(i)


world = (str(mundo)+ "-" +str(nivel))
tiempo_total = 400