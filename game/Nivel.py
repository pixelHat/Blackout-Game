import pygame
from Block import Block
from Player import Player
from Ball import Ball
from constants import WHITE, SCREEN_TAM

class Nivel():
    def __init__(self):
        block = Block(10, 10, 100, 25, WHITE)
        block2 = Block(115, 10, 100, 25, WHITE)
        block3 = Block(220, 10, 100, 25, WHITE)
        self.numBlocks = 3
        self.blocks = [[block, block2], [block3, ]]
        self.player = Player(SCREEN_TAM[0] // 2, SCREEN_TAM[1] - 50, 10, 100, 25, WHITE)
        self.ball = Ball(SCREEN_TAM[0] // 2, 100, 5, -5, 10, WHITE)
        self.objects = [self.player, self.ball]

    def draw(self, screen):
        for obj in self.objects:
            obj.draw(screen)
        for blockList in self.blocks:
            for block in blockList:
                block.draw(screen)

    def update(self):
        for obj in self.objects:
            obj.update()
        self.collision()

    def collision(self):
        """
        verify collission betwen the ball and player
        and the ball and the blocks
        """
        playercollision = self.ball.getRect().colliderect(self.player.getRect())
        if playercollision:
            self.ball.collide()

        for listBlock in self.blocks:
            for block in listBlock:
                if self.ball.getRect().colliderect(block.getRect()):
                    self.ball.collide()
                    listBlock.pop(listBlock.index(block))
                    self.numBlocks -= 1

    def won(self):
        if self.numBlocks == 0:
            return True
