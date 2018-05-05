import pygame
from Block import Block
from Player import Player
from Ball import Ball
from constants import WHITE, SCREEN_TAM

class Level():
    def __init__(self, blocks1, blocks2=None):
        self.player = Player(SCREEN_TAM[0] // 2, SCREEN_TAM[1] - 50, 10, 100, 25, WHITE)
        self.ball = Ball(SCREEN_TAM[0] // 2, SCREEN_TAM[1] - 60, 4, -4, 10, WHITE)
        self.objects = [self.player, self.ball]
        self.numBlocks = 0
        self.play = True
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
        posX, posY = 100, 120
        row, col = len(self.blocksPattern1[0]), len(self.blocksPattern1)
        for idxCol in range(col):
            for idxRow in range(row):
                if self.blocksPattern1[idxCol][idxRow] == 1:
                    block = Block(posX + idxRow*width, posY + idxCol*height, width, height, WHITE)
                    self.blocks.append(block)

        posX, posY = 360, 120
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
        for obj in self.objects:
            obj.update()
        self.collision()
        self.play = self.ball.isLive()

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
