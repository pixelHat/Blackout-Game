from Text import Text

class Button(Text):
    def __init__(self, text, tam, pos, color, action=None):
        super().__init__(text, tam, pos, color)
        self.action = action

    def click(self, pos):
        return self.rect.collidepoint(pos)

    def getAction(self):
        return self.action
