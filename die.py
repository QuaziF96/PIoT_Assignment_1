from random import randint
from time import sleep
from abc import ABC, ABCMeta

class Die(ABC):

    g = (57,255,20) #neon green
    b = (0,0,0) #black

    one = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,g,g,b,b,b,
    b,b,b,g,g,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b]

    two = [
    b,b,b,b,b,b,b,b,
    b,g,g,b,b,b,b,b,
    b,g,g,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,g,g,b,b,
    b,b,b,b,g,g,b,b,
    b,b,b,b,b,b,b,b]

    three = [
    g,g,b,b,b,b,b,b,
    g,g,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,g,g,b,b,b,
    b,b,b,g,g,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,g,g,
    b,b,b,b,b,b,g,g]

    four = [
    b,b,b,b,b,b,b,b,
    b,g,g,b,b,g,g,b,
    b,g,g,b,b,g,g,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,g,g,b,b,g,g,b,
    b,g,g,b,b,g,g,b,
    b,b,b,b,b,b,b,b]

    five = [
    g,g,b,b,b,b,g,g,
    g,g,b,b,b,b,g,g,
    b,b,b,b,b,b,b,b,
    b,b,b,g,g,b,b,b,
    b,b,b,g,g,b,b,b,
    b,b,b,b,b,b,b,b,
    g,g,b,b,b,b,g,g,
    g,g,b,b,b,b,g,g]

    six = [
    g,g,b,b,b,b,g,g,
    g,g,b,b,b,b,g,g,
    b,b,b,b,b,b,b,b,
    g,g,b,b,b,b,g,g,
    g,g,b,b,b,b,g,g,
    b,b,b,b,b,b,b,b,
    g,g,b,b,b,b,g,g,
    g,g,b,b,b,b,g,g]

    def __init__(self):
        super().__init__()

    def roll(self,sense):
        n = randint(1,6)
        if n == 1:
            sense.set_pixels(self.one)
        elif n == 2:
            sense.set_pixels(self.two)
        elif n == 3:
            sense.set_pixels(self.three)
        elif n == 4:
            sense.set_pixels(self.four)
        elif n == 5:
            sense.set_pixels(self.five)
        elif n == 6:
            sense.set_pixels(self.six)
        sleep(1)
            




