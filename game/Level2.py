import pygame
from Block import Block
from Player import Player
from Ball import Ball
from constants import WHITE, SCREEN_TAM, blocks2
from Level import Level

class Level2(Level):
    def __init__(self):
        super().__init__()
