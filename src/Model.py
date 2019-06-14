# Model.py
#
# For TicTacToe

# Keeps track of what's in each cell. Updates when told by the Controller. Provides logic and detirmines if there is a winner or a draw.

from View import View
import time


class Model:

    def __init__(self, view):
        
        self.v = view

        self.playX = []
        self.playO = []
        #Following list is for the message area at the top. Used by the Controller to tell the player to click in the grid. npa = Non-Play Area

    # Tells view to draw the X's based on click
    def playerX(self, click):
        if click == 0:
            self.v.drawX(0)
        elif click == 1:
            self.v.drawX(1)
        elif click == 2:
            self.v.drawX(2)
        elif click == 3:
            self.v.drawX(3)
        elif click == 4:
            self.v.drawX(4)
        elif click == 5:
            self.v.drawX(5)
        elif click == 6:
            self.v.drawX(6)
        elif click == 7:
            self.v.drawX(7)
        elif click == 8:
            self.v.drawX(8)

    # Tells view to draw the O's based on the click
    def playerO(self, click):
        if click == 0:
            self.v.drawO(0)
        elif click == 1:
            self.v.drawO(1)
        elif click == 2:
            self.v.drawO(2)
        elif click == 3:
            self.v.drawO(3)
        elif click == 4:
            self.v.drawO(4)
        elif click == 5:
            self.v.drawO(5)
        elif click == 6:
            self.v.drawO(6)
        elif click == 7:
            self.v.drawO(7)
        elif click == 8:
            self.v.drawO(8)

    def gameWin(self):

        # Defines the win conditions
        # DOES NOT WORK!!!!!!!!!!!!!!!!! AAAAAHHHHHHH
        winConditions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [2,4,6], [0,4,8]]

        print(winConditions[0])

        for condition in winConditions:
            if self.playX in winConditions[0]:
                return "X"
            else:
                return "continue"

        # for item in winConditions:
        #     if item in self.playX:
        #         return "X"
        #     elif item in self.playO:
        #         return "O"
        #     else:
        #         break
        # if len(self.playX) + len(self.playO) == 9:
        #     return "tie"
        # else:
        #     return "continue"

    def reset(self):
        pass

def ModelTest():
    
    pass

if __name__ == "__main__":
    ModelTest()
