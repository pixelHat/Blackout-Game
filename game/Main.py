import pygame, sys
from constants import *
from LevelBehavior import LevelBehavior

class Main:
    def __init__(self, width, height, name, fps):
        self.width = width
        self.height = height
        self.name = name
        self.fps = fps
        self.play = True

    def start(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.level = LevelBehavior()
        self.update()

    def update(self):
        while self.play:
            self.play = self.level.update(self.screen)
            pygame.display.flip()
            self.screen.fill(BLACK)
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
        self.finalise()

    def finalise(self):
        pygame.quit()

if __name__ == "__main__":
    main = Main(SCREEN_TAM[0], SCREEN_TAM[1], "Blackout", 60)
    main.start()
