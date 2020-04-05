class Temperature:

    red = [255,0,0]
    green = [0,255,0]
    blue = [0,0,255]

    def __init__(self, temp, cMax, hMin, comfMax, comfMin, sense):
        self.temp = temp
        self.cMax = cMax
        self.hMin = hMin
        self.comfMax = comfMax
        self.comfMin = comfMin
        self.sense = sense

    def checkAndDisplay(self):

        if(self.temp < self.cMax):
            #display number with blue
            self.sense.show_message(str(self.temp),text_colour= self.blue)

        elif (self.temp <= self.comfMax and self.temp >= self.comfMin):
            #display number with green
            self.sense.show_message(str(self.temp),text_colour=self.green)

        elif (self.temp > self.hMin):
            #display number with red    
            self.sense.show_message(str(self.temp),text_colour=self.red)    