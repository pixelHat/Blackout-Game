import pygame
from .Block import Block
from .Player import Player
from .Ball import Ball
from .constants import WHITE

class Nivel():
    def __init__(self):
        block = Block(10, 10, 100, 25, WHITE)
        player = Player(100, 100, 100, 25, WHITE)
        ball = Ball(50, 50, 5, 5, 10, WHITE)
        self.objects = [block, player, ball]

    def draw(self, screen):
        for obj in self.objects:
            obj.draw(screen)

    def update(self):
        for obj in self.objects:
            obj.update()
