import pygame
from constants import SCREEN_TAM

class Ball:
    def __init__(self, posX, posY, velX, velY, radius, color):
        self.posX = posX
        self.posY = posY
        self.velX = velX
        self.velY = velY
        self.radius = radius
        self.color = color
        self.Live = True
        self.rect = pygame.Rect(self.posX - self.radius, self.posY - self.radius, 2 * self.radius, 2 * self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.posX, self.posY), self.radius)

    def update(self):
        self.move()

    def move(self):
        if self.velX < 0 and self.posX > self.radius:
            self.posX += self.velX
            self.rect.move_ip(self.velX, 0)
        elif self.velX > 0 and self.posX < SCREEN_TAM[0] - self.radius:
            self.posX += self.velX
            self.rect.move_ip(self.velX, 0)
        else:
            self.velX = -self.velX

        if self.velY < 0 and self.posY > self.radius:
            self.posY += self.velY
            self.rect.move_ip(0, self.velY)
        elif self.velY > 0 and self.posY < SCREEN_TAM[1] - self.radius:
            self.posY += self.velY
            self.rect.move_ip(0, self.velY)
        else:
            self.velY = -self.velY

        if self.posY + self.radius >= SCREEN_TAM[1]:
            self.Live = False

    def isLive(self):
        return self.Live

    def collide(self):
        self.velY = - self.velY

    def getRect(self):
        return self.rect

if __name__ == "__main__":
    b = Ball(10, 10, 5, 5, 10, (0, 0, 0))
    b.update()
