from pygame import mouse
from Text import Text
from Button import Button
from constants import WHITE, GAME, QUIT

class Pause:
    def __init__(self, texts, buttons, actions):
        self.textPause = list()
        self.ButtonPause = list()

        posX, posY= 100, 100
        sizeFont = 30
        for text in texts:
            _text = Text(text, sizeFont, (posX, posY), WHITE)
            self.textPause.append(_text)
            posY += _text.getSizeHeight()

        for index in range(len(buttons)):
            _button = Button(buttons[index], sizeFont, (posX, posY), WHITE, actions[index])
            self.ButtonPause.append(_button)
            posY += _button.getSizeHeight()

    def buttonAction(self):
        for text in self.ButtonPause:
            click = text.click(mouse.get_pos())
            if click:
                return text.getAction()
        return False

    def draw(self, screen):
        for text in self.textPause:
            text.draw(screen)
        for text in self.ButtonPause:
            text.draw(screen)
