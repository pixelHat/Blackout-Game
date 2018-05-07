from pygame import font

class Text:
    def __init__(self, text, tam, pos, color):
        _font = font.SysFont('Comic Sans MS', 30)
        self.text = _font.render(text, False, color)
        self.pos = pos
        self.sizeWidth = _font.size(text)[0]
        self.sizeHeight = _font.size(text)[1]

    def draw(self, screen):
        screen.blit(self.text, self.pos)

    def getSizeWidth(self):
        return self.sizeWidth

    def getSizeHeight(self):
        return self.sizeHeight
