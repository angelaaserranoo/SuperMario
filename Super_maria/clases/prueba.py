import pyxel

class App():
    def __init__(self):
        pyxel.init(160, 160, caption ="Mario Bros")
        pyxel.load(r'C:\Users\anaja\Documents\Super_maria\assets\mario_assets.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

    def draw(self):
        pyxel.cls(6)
        pyxel.blt(0, 0, 0, 0, 0, 160, 160)

App()
