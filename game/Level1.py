import pygame
from Block import Block
from Player import Player
from Ball import Ball
from constants import WHITE, SCREEN_TAM
from Level import Level

class Level1(Level):
    def __init__(self):
        super().__init__()

    def createBlock(self):
        """
        create level's blocks
        """
        self.blocks = []
        blocks = [[0, 1, 1, 1, 1, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0],
                  [1, 1, 1, 0, 1, 1, 1],
                  [0, 1, 1, 0, 1, 1, 0],
                  [0, 1, 0, 0, 0, 1, 0]]

        width, height = 40, 40
        posX, posY = 100, 120
        row, col = len(blocks[0]), len(blocks)
        for idxCol in range(col):
            for idxRow in range(row):
                if blocks[idxCol][idxRow] == 1:
                    block = Block(posX + idxRow*width, posY + idxCol*height, width, height, WHITE)
                    self.blocks.append(block)

        posX, posY = 360, 120
        for idxCol in range(col):
            for idxRow in range(row):
                if blocks[idxCol][idxRow] == 1:
                    block = Block(posX + idxRow*width, posY + idxCol*height, width, height, WHITE)
                    self.blocks.append(block)

        self.blocks = set(self.blocks)
        self.numBlocks = len(self.blocks)
