import sys
import random
import math


class vector (object):
    def __init__(self, x=0, y=0, randspeed=0):
        if randspeed:
            self.randomize(randspeed)
        else:
            self.x, self.y = x, y

    def __add__(self, a):
        rx, ry = self.x + a.x, self.y + a.y
        return vector(rx, ry)

    def __radd__(self, a):
        rx, ry = self.x + a.x, self.y + a.y
        return vector(rx, ry)

    def __sub__(self, a):
        rx, ry = self.x - a.x, self.y - a.y
        return vector(rx, ry)

    def __str__(self):
        return ('({} ; {})'.format(self.x, self.y))

    def getpos(self):
        return (self.x, self.y)

    def randomize(self, speed):
        g = 0
        while g == 0:
            g = random.randrange(-speed, speed + 1) 
        self.x = g
        self.y = round(math.sqrt(speed * speed - self.x * self.x))
        neg = random.randint (0, 1)
        if neg:
            self.y = -self.y


class point (vector):
    pass
