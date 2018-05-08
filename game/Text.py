from pygame import font, Rect
from pygame import draw
class Text:
    def __init__(self, text, tam, pos, color):
        _font = font.SysFont('Comic Sans MS', 30)
        self.text = _font.render(text, False, color)
        self.pos = pos
        self.sizeWidth = _font.size(text)[0]
        self.sizeHeight = _font.size(text)[1]
        self.rect = Rect(pos[0], pos[1], self.sizeWidth, self.sizeHeight)

    def draw(self, screen):
        screen.blit(self.text, self.pos)

    def getSizeWidth(self):
        return self.sizeWidth

    def getSizeHeight(self):
        return self.sizeHeight

    def click(self, pos):
        return self.rect.collidepoint(pos)
