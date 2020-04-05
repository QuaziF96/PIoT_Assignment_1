class Player:
    
    count = 0

    def __init__(self, player):
        self.player = player
        self.count = self.count
        super().__init__()

    def updatePoints(self,value):
        self.count += value

    def checkWinner(self):
        if( self.count >= 30):
            return True    
        return False