from sense_hat import SenseHat
from random import randint
from die import Die

sense = SenseHat()
sense.clear()



g = (57,255,20) #neon green
y = (0,0,0) #black

class Main:
    @staticmethod
    def main():
        sense.show_message("Shake to roll die!")
        die = Die()
        while True:
            if checkShake():
                die.roll(sense)


def checkShake():
        x, y, z = sense.get_accelerometer_raw().values()

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1.5 or y > 1.5 or z > 1.5:
            return True
        return False      

Main.main()        
 