import pygame, sys
from constants import *
from Level import Level

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
        self.level = Level(blocks1, blocks3)
        self.update()

    def update(self):
        while self.play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

            if self.level.won():
                self.play  = False
            if not self.level.loser():
                self.play = False

            #DRAW
            self.level.draw(self.screen)

            #UPDATE
            self.level.update()

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
