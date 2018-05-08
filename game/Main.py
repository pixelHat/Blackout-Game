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
        self.status = "game"

    def start(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.levels = []
        for i in blocksList:
            for j in blocksList:
                self.levels.append(Level(i, j))
        self.level = self.levels[0]
        self.numLevel = 1
        self.maxLevel = len(self.levels)
        self.update()

    def update(self):
        while self.play:
            if self.status == GAME:
                self.level.draw(self.screen)
                self.status = self.level.update()
            elif self.status == PAUSE:
                self.status = self.level.pause(self.screen)
            elif self.status == WIN and self.numLevel < self.maxLevel:
                self.level = self.levels[self.numLevel]
                self.numLevel += 1
                self.status = GAME
            elif self.status == GAMEOVER:
                self.numLevel = 0
                self.level.reset()
                self.status = GAME
            elif self.status == QUIT:
                self.play = False

            #RENDER
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
