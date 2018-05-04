import pygame, sys
from constants import *
from Nivel import Nivel

class Main:
    def __init__(self, width, height, name, fps):
        self.width = width
        self.height = height
        self.name = name
        self.fps = fps
        self.play = True

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        self.clock = pygame.time.Clock()
        self.nivel = Nivel()
        self.update()

    def update(self):
        while self.play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

            if self.nivel.won():
                self.play  = False

            #DRAW
            self.nivel.draw(self.screen)

            #UPDATE
            self.nivel.update()

            #RENDER
            pygame.display.flip()
            self.screen.fill(BLACK)

            self.clock.tick(self.fps)
        self.finalise()

    def finalise(self):
        pygame.quit()

if __name__ == "__main__":
    main = Main(800, 600, "Blackout", 60)
    main.start()
