import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../game'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from Ball import Ball
from constants import WHITE, SCREEN_TAM
import unittest

class TestBall(unittest.TestCase):
    def setUp(self):
        self.velX = 5
        self.velY = 5
        self.radius = 10
        self.color = WHITE

    def testMoveLeftUp(self):
        velX = - self.velX
        velY = - self.velY
        posX = 100
        posY = 100
        ball = Ball(posX, posY, velX, velY, self.radius, self.color)

        ball.move()

        self.assertEqual((posX + velX, posY + velY), (ball.posX, ball.posY))

    def testMoveLeftDown(self):
        velX = - self.velX
        posX = 100
        posY = 100
        ball = Ball(posX, posY, velX, self.velY, self.radius, self.color)

        ball.move()

        self.assertEqual((posX + velX, posY + self.velY), (ball.posX, ball.posY))

    def testMoveRightUp(self):
        velY = - self.velY
        posX = 100
        posY = 100
        ball = Ball(posX, posY, self.velX, velY, self.radius, self.color)

        ball.move()

        self.assertEqual((posX + self.velX, posY + velY), (ball.posX, ball.posY))

    def testMoveRightDown(self):
        posX = 100
        posY = 100
        ball = Ball(posX, posY, self.velX, self.velY, self.radius, self.color)

        ball.move()

        self.assertEqual((posX + self.velX, posY + self.velY), (ball.posX, ball.posY))

    def testMoveLeftInvalid(self):
        velX = - self.velX
        posX = self.radius
        posY = 100
        ball = Ball(posX, posY, velX, self.velY, self.radius, self.color)

        ball.move()

        self.assertEqual((posX, posY + self.velY), (ball.posX, ball.posY))

    def testMoveRightInvalid(self):
        posX = SCREEN_TAM[0] - self.radius
        posY = 100
        ball = Ball(posX, posY, self.velX, self.velY, self.radius, self.color)

        ball.move()

        self.assertEqual((posX, posY + self.velY), (ball.posX, ball.posY))

    def testMoveUpInvalid(self):
        velY = - self.velY
        posX = 100
        posY = self.radius
        ball = Ball(posX, posY, self.velX, velY, self.radius, self.color)

        ball.move()

        self.assertEqual((posX + self.velX, posY), (ball.posX, ball.posY))

    def testMoveDownInvalid(self):
        posX = 100
        posY = SCREEN_TAM[1] - self.radius
        ball = Ball(posX, posY, self.velX, self.velY, self.radius, self.color)

        ball.move()

        self.assertEqual((posX + self.velX, posY), (ball.posX, ball.posY))
