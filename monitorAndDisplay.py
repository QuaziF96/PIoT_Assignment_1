from sense_hat import SenseHat
from time import sleep
import json

with open('config.json') as json_file:
    parsed_json = json.load(json_file)


coldMax = int(parsed_json['cold_max'])
comfortableMin = int(parsed_json['comfortable_min'])
comfortableMax = int(parsed_json['comfortable_max'])
hotMin = int(parsed_json['hot_min'])

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

def senseTempAndDisplay():
    sense = SenseHat()
    while True:
        temp = int(round(float(sense.get_temperature())))
        
        if(temp < coldMax):
            #display number with blue
            sense.show_message(str(temp),text_colour=blue)
        elif (temp <= comfortableMax and temp >= comfortableMin):
            #display number with green
            sense.show_message(str(temp),text_colour=green)
        elif (temp > hotMin):
            print('hello')
            #display number with red    
            sense.show_message(str(temp),text_colour=red)
        sleep(10)    


senseTempAndDisplay()
