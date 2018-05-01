import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../game'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from Player import Player
import unittest
import constants as b

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.posY = 100
        self.vel = 10
        self.width = 50
        self.height = 25

    def testMoveLeftValid(self):
        posX = b.SCREEN_TAM[0] - self.width
        player = Player(posX, self.posY, self.vel, self.width, self.height, b.WHITE)
        player.move(-1)
        self.assertEqual((posX - self.vel, self.posY), player.getPos())

    def testMoveLeftInvalid(self):
        player = Player(0, self.posY, self.vel, self.width, self.height, b.WHITE)
        player.move(-1)
        self.assertEqual((0, self.posY), player.getPos())

    def testMoveRightValid(self):
        posX = b.SCREEN_TAM[0] - 2 * self.width
        player = Player(posX, self.posY, self.vel, self.width, self.height, b.WHITE)
        player.move(1)
        self.assertEqual((posX + self.vel, self.posY), player.getPos())

    def testMoveRightInvalid(self):
        posX = b.SCREEN_TAM[0] - self.width
        player = Player(posX, self.posY, self.vel, self.width, self.height, b.WHITE)
        player.move(1)
        self.assertEqual((posX, self.posY), player.getPos())
