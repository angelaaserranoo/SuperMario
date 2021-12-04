import random
import pyxel
#el juego crea y se carga al jugador
class Player:
    def __init__(self):

        self.__reset()

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def vy(self):
        return self.__vy

    def _reset(self):

        self.score = 0
        self.player_x = 72
        self.player_y = -16
        self.player_vy = 0 #es un atributo del jugador, no del juego (piensa en el caso de que haya dos jugadores)
        self.player_is_alive = True

    def update(self, player: Player):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.player_x = max(self.player_x - 2, 0)

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)

        self.player_y += self.player_vy
        self.player_vy = min(self.player_vy + 1, 8)

        if self.player_y > pyxel.height:
            if self.player_is_alive:
                self.player_is_alive = False
                pyxel.play(3, 5)

            if self.player_y > 600:
                self.score = 0
                self.player_x = 72
                self.player_y = -16
                self.player_vy = 0
                self.player_is_alive = True

class Fruit:
    def __init__(self, x, y , kind):
        self.__x = x
        self.__y = y
        self.__kind = kind
        self.__is_alive = True

    def update(self, player : PLayer):
        if self.__is_alive and abs(self.player__x - player.x) < 12 and abs(self.player_y - player.y) < 12:
            is_active = False
            self.score += (kind + 1) * 100
            self.player_vy = min(self.player_vy, -8)
            pyxel.play(3, 4)

        x -= 2

        if x < -40:
            x += 240
            y = randint(0, 104)
            kind = randint(0, 2)
            is_active = True

class Floor: #posee una tupla con sus coorfenadas y un booleano por si es pisable
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__is_alive = True #no lo ponemos en el __init__ pq siempre que creamos un suelo aparece siendo pisable

    def touchFloor(self):

        self.score += 10
        self.player_vy = -12
        pyxel.play(3, 3)

    def update(self):
        if self.__is_active:
            if (
                    player.x + 16 >= self.__x
                    and player.x <= self.__x + 40
                    and player.y + 16 >= self.__y
                    and player.y <= self.__y + 8
                    and player.vy > 0
            ):
                self.__is_active = False
                player.touchFloor()
        else:
            self.__y += 6

        self.__x -= 4

        if self.__x < -40:
            self.__x+= 240
            self.__y = randint(8, 104)
            self.__is_active = True
class Mountain:
    pass
class Cloud:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
class Forest:
    pass
#una clase superior llamada atrezzo que se componga por todo el fondo
class Atrezzo:
    pass

class Juego:
    def __init__ (self):

        pyxel.init(160, 120, caption = "Pyxel Jump")
        pyxel.load("assets")

        self.player = Player() #een el ejemplo aqui hay muchos slfs que son atributos del jugador que los hemos metido en una clase
        self.__floors = self.__createFloors(4)
        self.__fruits = self.__createFruits(4)
        self.__far_clouds = [Cloud(-10, 75), Cloud(40, 65), Cloud(90, 60)]
        self.__near_clouds = [Cloud(10, 25), Cloud(70, 35), Cloud(120, 15)]

        pyxel.playm(0, loop = True) #este loop esta para reprodcir la musica del juego
        pyxel.run
    def __crearFloors(self, numeros_items):
        items = []

        for i in range (items):
            item = Floor(i * 60, randint(8, 104))
            #crea el numero de suelos flotantes que indiquemos en item; el randint es para que vayan cambiando la altura de salida
            items.append(item)

        return floors
    def __crearFruits(self,numeros_items):
        items = []

        for i in range(items):
            item = Fruit(i * 60, randint(8, 104),randint(0,2))
            items.append(item)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.__player.update()

        for i, v in enumerate(self.floor):
            self.floor[i] = self.update_floor(*v)

        for i, v in enumerate(self.fruit):
            self.fruit[i] = self.update_fruit(*v)

