from sense_hat import SenseHat
from random import randint
from die import Die

class Main:
    @staticmethod
    def main():
        sense = SenseHat()
        sense.clear()
        sense.show_message("Shake to roll die!")
        die = Die()
        while True:
            if die.checkShake(sense):
                die.roll(sense)

Main.main()        
 