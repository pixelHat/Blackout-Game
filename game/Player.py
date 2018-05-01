from constants import *
from Block import Block
import pygame

class Player(Block):
    def __init__(self, posX, posY, vel, width, height, color):
        super().__init__(posX, posY, width, height, color)
        self.vel = vel

    def update(self):
        input = self.getInput()
        move(input)

    def getInput(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            return -1
        elif pressed[K_RIGHT]:
            return 1
        return 0

    def move(self, input):
        if input == -1 and self.posX > 0:
            self.posX -= self.vel
            self.rect.move_ip(self.posX - self.vel, self.posY)
        elif input == 1 and self.posX < SCREEN_TAM[0] - self.width:
            self.posX += self.vel
            self.rect.move_ip(self.posX + self.vel, self.posY)

    def getPos(self):
        return (self.posX, self.posY)
