import pygame, sys
from constants import *
from Nivel import Nivel

pygame.init()
screen = pygame.display.set_mode(SCREEN_TAM)
pygame.display.set_caption("Blackout")
clock = pygame.time.Clock()

fase = Nivel()

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    #DRAW
    fase.draw(screen)

    #UPDATE
    fase.update()

    #RENDER
    pygame.display.flip()
    screen.fill(BLACK)

    clock.tick(FPS)
pygame.quit()
