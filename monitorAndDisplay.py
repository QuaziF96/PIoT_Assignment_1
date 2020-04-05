from sense_hat import SenseHat
from time import sleep
import json

with open('config.jsson') as json_file:
    parsed_json = json.loads(json_file)


coldMax = parsed_json['cold_max']
comfortableMin = parsed_json['comfortable_min']
comfortableMax = parsed_json['comfortable_max']
hotMin = parsed_json['hot_min']

red = (255,0,0)
blue = (0,255,0)
green = (0,0,255)

def senseTempAndDisplay():
    while True:
        sense =  SenseHat()
        temp = round(sense.get_temperature)

        if(temp < coldMax):
            #display number with blue
            sense.show_letter(str(temp), text_colour = blue)
        elif (temp <= 25 or temp >= 10):
            #display number with green
            sense.show_letter(str(temp), text_colour = green)
        else:
            #display number with red    
            sense.show_letter(str(temp), text_colour = red)
        sleep(10)    


senseTempAndDisplay()
