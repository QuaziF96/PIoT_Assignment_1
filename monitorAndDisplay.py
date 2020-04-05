from sense_hat import SenseHat
from time import sleep
import json
from Temperature import Temperature

with open('config.json') as json_file:
    parsed_json = json.load(json_file)


coldMax = int(parsed_json['cold_max'])
comfortableMin = int(parsed_json['comfortable_min'])
comfortableMax = int(parsed_json['comfortable_max'])
hotMin = int(parsed_json['hot_min'])

def senseTempAndDisplay():
    sense = SenseHat()
    while True:
        temp = int(round(float(sense.get_temperature())))

        temperature = Temperature(temp, coldMax, hotMin, comfortableMax, comfortableMin, sense)
        temperature.checkAndDisplay()
        
        sleep(10)    


senseTempAndDisplay()
