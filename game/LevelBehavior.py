from constants import *
from Level import Level

class LevelBehavior:
    def __init__(self):
        self.levels = []
        for i in blocksList:
            for j in blocksList:
                self.levels.append(Level(i, j))
        self.levelCurrent = self.levels[0]
        self.indexLevel = 1
        self.maxLevel = len(self.levels)
        self.status = GAME

    def nextLevel(self):
        self.levelCurrent = self.levels[indexLevel]
        self.indexLevel += 1
        self.status = GAME

    def gameOver(self):
        self.numLevel = 0
        self.levelCurrent.reset()
        self.status = GAME

    def play(self, screen):
        self.levelCurrent.draw(screen)
        self.status = self.levelCurrent.update()

    def update(self, screen):
        """
        return True if the player will play,
        otherwise return false.
        """
        if self.status == GAME:
            self.play(screen)
        elif self.status == PAUSE:
            self.status = self.levelCurrent.pause(screen)
        elif self.status == WIN and self.indexLevel < self.maxLevel:
            self.nextLevel()
        elif self.status == GAMEOVER:
            self.gameOver()
        elif self.status == QUIT:
            return False
        return True
