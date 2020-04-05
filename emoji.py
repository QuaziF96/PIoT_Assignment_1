from sense_hat import SenseHat
from time import sleep
from abc import ABC, ABCMeta

class Emoji(ABC):
    r = (255,0,0)
    g = (0,255,0)
    b = (0,0,255)

    x = (0,0,0) #Will vary
    y = (0,0,0) #Black
    matrix = [y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y]

    def __init__(self,emoji):
        super().__init__() 
        self.__emoji = emoji 

    def setMatrix(self):
        x = self.x
        y = self.y
        if (self.__emoji == "smiley"):
            self.matrix = [y,y,y,y,y,y,y,y,
                      y,y,y,y,y,y,y,y,
                      y,x,x,y,y,x,x,y,
                      y,x,x,y,y,x,x,y,
                      y,y,y,y,y,y,y,y,
                      y,x,x,y,y,x,x,y,
                      y,y,x,x,x,x,y,y,
                      y,y,y,x,x,y,y,y] 
                      

        elif (self.__emoji == "frowny"):
            self.matrix = [y,y,y,y,y,y,y,y,
                      y,y,y,y,y,y,y,y,
                      y,x,x,y,y,x,x,y,
                      y,x,x,y,y,x,x,y,
                      y,y,y,y,y,y,y,y,
                      y,y,y,x,x,y,y,y,
                      y,y,x,x,x,x,y,y,
                      y,x,x,y,y,x,x,y]

        elif (self.__emoji == "angry"):
            self.matrix = [y,y,y,y,y,y,y,y,
                      y,y,y,y,y,y,y,y,
                      y,y,y,y,y,y,y,y,
                      y,x,x,y,y,x,x,y,
                      y,y,y,y,y,y,y,y,
                      y,y,y,y,y,y,y,y,
                      y,y,x,x,x,x,y,y,
                      y,y,y,y,y,y,y,y]

    def displayRed(self,sensehat):
        self.x = self.r
        self.setMatrix()
        sensehat.set_pixels(self.matrix)
        sleep(3)

    def displayGreen(self,sensehat):
        self.x = self.g
        self.setMatrix()
        sensehat.set_pixels(self.matrix)
        sleep(3)

    def displayBlue(self,sensehat):
        self.x = self.b
        self.setMatrix()
        sensehat.set_pixels(self.matrix)
        sleep(3)

