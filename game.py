from die import Die
from sense_hat import SenseHat
from time import sleep
from player import Player
import datetime
import csv

sense = SenseHat()
sense.clear()

class Main:
    @staticmethod
    def main():
        sense.show_message("Welcome to the game! This is a two player"+ 
        "game. Player 1 goes first. Take turns shaking the device to"+ 
        "roll die. First one to 30 points wins!")
        i = 1
        die = Die()
        players = [Player(1),Player(2)]
        while (i < 61):
            if (i % 2 != 0):
                sense.show_message("Player 1's turn!")
                sleep(3)
                while True:
                    if die.checkShake(sense):
                        break
                die.roll(sense)
                players[0].updatePoints(die.getValue())

            else:
                sense.show_message("Player 2's turn!")
                sleep(3)
                while True:
                    if die.checkShake(sense):
                        break
                die.roll(sense)
                players[1].updatePoints(die.getValue())
            
            if checkWinStatus(players,sense):
                break 
            i += 1
        sense.clear()
        recordWinner(players)


def checkWinStatus(players,sense):
    if players[0].checkWinner():
        sense.show_message("Player 1 wins! Thanks for playing!")
        return True
    elif players[1].checkWinner():
        sense.show_message("Player 2 wins! Thanks for playing!")
        return True
    return False

def recordWinner(players):
    timeNow = str(datetime.datetime.now().time())
    row = ""
    if players[0].checkWinner():
        row = "Player 1,{score},{time}".format(score=str(players[0].count),time = timeNow)
    elif players[0].checkWinner():
        row = "Player 2,{score},{time}".format(score=str(players[1].count),time = timeNow)

    with open("winner.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow(row)
    

Main.main()        