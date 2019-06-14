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

        # winConditions = [[0 and 1 and 2], [3 and 4 and 5], [6 and 7 and 8], [0 and 3 and 6], [1 and 4 and 7], [2 and 5 and 8], [2 and 4 and 6], [0 and 4 and 8]]

        if (0 in self.playX and 1 in self.playX and 2 in self.playX) or (3 in self.playX and 4 in self.playX and 5 in self.playX) or (6 in self.playX and 7 in self.playX and 8 in self.playX) or (0 in self.playX and 3 in self.playX and 6 in self.playX) or (1 in self.playX and 4 in self.playX and 7 in self.playX) or (2 in self.playX and 5 in self.playX and 8 in self.playX) or (2 in self.playX and 4 in self.playX and 6 in self.playX) or (0 in self.playX and 4 in self.playX and 8 in self.playX):
            return "X"
        if (0 in self.playO and 1 in self.playO and 2 in self.playO) or (3 in self.playO and 4 in self.playO and 5 in self.playO) or (6 in self.playO and 7 in self.playO and 8 in self.playO) or (0 in self.playO and 3 in self.playO and 6 in self.playO) or (1 in self.playO and 4 in self.playO and 7 in self.playO) or (2 in self.playO and 5 in self.playO and 8 in self.playO) or (2 in self.playO and 4 in self.playO and 6 in self.playO) or (0 in self.playO and 4 in self.playO and 8 in self.playO):
            return "O"
        elif len(self.playX) + len(self.playO) == 9:
            return "tie"
        else:
            return "continue"

    def reset(self):
        self.playX.clear()
        self.playO.clear()

def ModelTest():
    
    pass

if __name__ == "__main__":
    ModelTest()
