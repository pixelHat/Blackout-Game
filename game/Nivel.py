import pygame
from Block import Block
from Player import Player
from Ball import Ball
from constants import WHITE, SCREEN_TAM

class Nivel():
    def __init__(self):
        self.player = Player(SCREEN_TAM[0] // 2, SCREEN_TAM[1] - 50, 10, 100, 25, WHITE)
        self.ball = Ball(SCREEN_TAM[0] // 2, 100, 5, -5, 10, WHITE)
        self.objects = [self.player, self.ball]
        self.createBlock()

    def createBlock(self):
        self.blocks = []
        #lado esquerdo
        block = Block(300, 280, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(300, 240, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(300, 200, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(300, 160, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(300, 120, 40, 40, WHITE)
        self.blocks.append(block)

        #lado direito
        block = Block(460, 280, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(460, 240, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(460, 200, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(460, 160, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(460, 120, 40, 40, WHITE)
        self.blocks.append(block)

        #topo
        block = Block(420, 120, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(380, 120, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(340, 120, 40, 40, WHITE)
        self.blocks.append(block)

        # topo meio
        block = Block(380, 160, 40, 40, WHITE)
        self.blocks.append(block)

        # esquerda interna
        block = Block(340, 200, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(340, 240, 40, 40, WHITE)
        self.blocks.append(block)

        #direita interna
        block = Block(420, 200, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(420, 240, 40, 40, WHITE)
        self.blocks.append(block)

        # braços
        block = Block(260, 200, 40, 40, WHITE)
        self.blocks.append(block)
        block = Block(500, 200, 40, 40, WHITE)
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
