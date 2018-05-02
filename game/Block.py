import pygame

class Block():
    def __init__(self, posX, posY, width, height, color):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(posX, posY, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        pass
