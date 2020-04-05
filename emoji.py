from sense_hat import SenseHat
from time import sleep
from abc import ABC, ABCMeta

class Emoji(ABC):
    r = (255,0,0)
    g = (0,255,0)
    b = (0,0,255)

    x = (0,0,0) #VARIABLE
    y = (0,0,0) #BLACK
    matrix = [y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y,
              y,y,y,y,y,y,y,y]

    def __init__(self,emoji):
        x = self.x
        y = self.y
        if (emoji == "smiley"): 
            self.matrix = [y,y,y,y,y,y,y,y,
                      y,y,y,y,y,y,y,y,
                      y,x,x,y,y,x,x,y,
                      y,x,x,y,y,x,x,y,
                      y,y,y,y,y,y,y,y,
                      y,x,x,y,y,x,x,y,
                      y,y,x,x,x,x,y,y,
                      y,y,y,x,x,y,y,y] 
                      

        elif (emoji == "frowny"):
            self.matrix = [y,y,y,y,y,y,y,y,
                      y,y,y,y,y,y,y,y,
                      y,x,x,y,y,x,x,y,
                      y,x,x,y,y,x,x,y,
                      y,y,y,y,y,y,y,y,
                      y,y,y,x,x,y,y,y,
                      y,y,x,x,x,x,y,y,
                      y,x,x,y,y,x,x,y]

        elif (emoji == "angry"):
            self.matrix = [y,y,y,y,y,y,y,y,
                      y,y,y,y,y,y,y,y,
                      y,y,y,y,y,y,y,y,
                      y,x,x,y,y,x,x,y,
                      y,y,y,y,y,y,y,y,
                      y,y,y,y,y,y,y,y,
                      y,y,x,x,x,x,y,y,
                      y,y,y,y,y,y,y,y]

        super().__init__()


    def displayRed(self,sensehat):
        self.x = self.r
        sensehat.set_pixels(self.matrix)
        sleep(3)

    def displayGreen(self,sensehat):
        self.x = self.g
        sensehat.set_pixels(self.matrix)
        sleep(3)

    def displayBlue(self,sensehat):
        self.x = self.b
        sensehat.set_pixels(self.matrix)
        sleep(3)

