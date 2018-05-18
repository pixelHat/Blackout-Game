from pygame import key, mouse
from pygame.locals import *
from Block import Block
from Player import Player
from Ball import Ball
from Text import Text
from Button import Button
from constants import *

class Level():
    def __init__(self, blocks1, blocks2=None):
        self.player = Player(SCREEN_TAM[0] // 8, SCREEN_TAM[1] - 50, 10, 100, 25, WHITE)
        self.ball = Ball(SCREEN_TAM[0] // 6, SCREEN_TAM[1] - 60, 4, -4, 10, WHITE)
        self.objects = [self.player, self.ball]
        self.numBlocks = 0
        self.play = True

        #TEXT
        _text2 = Text("Pause", 30, (100, 100), WHITE)
        _text1 = Button("Continue", 30, (100, 100 + _text2.getSizeHeight()), WHITE, GAME)
        _text3 = Button("Sair", 30, (100, 100 + _text1.getSizeHeight() + _text2.getSizeHeight()), WHITE, QUIT)
        self.textPause = [_text2]
        self.ButtonPause = [_text1, _text3]

        self.blocksPattern1 = blocks1
        if blocks2 != None:
            self.blocksPattern2 = blocks2
        else:
            self.blocksPattern2 = blocks1
        self.createBlock()

    def createBlock(self):
        """
        create level's blocks
        """
        self.blocks = []

        width, height = 40, 40
        posX, posY = 100, 0
        row, col = len(self.blocksPattern1[0]), len(self.blocksPattern1)
        for idxCol in range(col):
            for idxRow in range(row):
                if self.blocksPattern1[idxCol][idxRow] == 1:
                    block = Block(posX + idxRow*width, posY + idxCol*height, width, height, WHITE)
                    self.blocks.append(block)

        posX, posY = 360, 0
        for idxCol in range(col):
            for idxRow in range(row):
                if self.blocksPattern2[idxCol][idxRow] == 1:
                    block = Block(posX + idxRow*width, posY + idxCol*height, width, height, WHITE)
                    self.blocks.append(block)

        self.blocks = set(self.blocks)
        self.numBlocks = len(self.blocks)

    def draw(self, screen):
        for obj in self.objects:
            obj.draw(screen)
        for block in self.blocks:
                block.draw(screen)

    def update(self):
        """
        move the objects and call the method collision
        """
        pressed = key.get_pressed()
        if pressed[K_p]:
            return PAUSE
        for obj in self.objects:
            obj.update()
        self.collision()
        if not self.ball.isLive():
            return GAMEOVER
        if self.won():
            return WIN
        return GAME

    def pause(self, screen):
        """
        screen the pause for the level
        """
        _mouse = mouse.get_pressed()
        if _mouse[0]:
            for text in self.ButtonPause:
                click = text.click(mouse.get_pos())
                if click:
                    return text.getAction()

        for text in self.textPause:
            text.draw(screen)
        for text in self.ButtonPause:
            text.draw(screen)

        return PAUSE

    def reset(self):
        self.__init__(self.blocksPattern1, self.blocksPattern2)

    def collision(self):
        """
        verify collission betwen the ball and player
        and the ball and the blocks
        """
        playercollision = self.ball.getRect().colliderect(self.player.getRect())
        if playercollision:
            self.ball.collide()

        _block = []
        for block in self.blocks:
            if self.ball.getRect().colliderect(block.getRect()):
                self.ball.collide()
                _block.append(block)
        for block in _block:
            self.blocks.remove(block)
            self.numBlocks -= 1

    def won(self):
        if self.numBlocks == 0:
            return True

    def loser(self):
        return self.play
