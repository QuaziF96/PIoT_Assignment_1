from sense_hat import SenseHat
from emoji import Emoji

sense = SenseHat()

class Main:
    @staticmethod
    def main():
        emojis = [Emoji("smiley"),
                  Emoji("frowny"),
                  Emoji("angry")]
                  
        for emoji in emojis:
            emoji.displayRed(sense)
            emoji.displayGreen(sense)
            emoji.displayBlue(sense)
Main.main()    
