import pyxel 


class App():
    def __init__(self):
        pyxel.init(160,160)
        self.x = 0
        self.y=0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width        
        self.y = (self.y + 1) % pyxel.height

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 8, 8, 6)
App()