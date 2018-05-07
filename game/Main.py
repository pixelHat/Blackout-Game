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
        self.statu = "game"

    def start(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.level = Level(blocks4, blocks3)
        self.update()

    def update(self):
        while self.play:
            if self.statu == GAME:
                #DRAW
                self.level.draw(self.screen)

                #UPDATE
                self.statu = self.level.update()

            elif self.statu == PAUSE:
                self.statu = self.level.pause(self.screen)

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
