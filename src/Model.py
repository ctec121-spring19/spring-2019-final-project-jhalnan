# Model.py
#
# For TicTacToe

# Keeps track of what's in each cell. Updates when told by the Controller. Provides logic and detirmines if there is a winner or a draw.

import View
import time

v = View.View()

class Model:

    def __init__(self):

        playX = []
        playO = []
        #Following list is for the message area at the top. Used by the Controller to tell the player to click in the grid. npa = Non-Play Area
        npa = [9, 10, 11]

        click = v.getClick()

        # Tells view to draw the X's based on click
        def playerX():
            if click == 0:
                v.drawX(0)
            elif click == 1:
                v.drawX(1)
            elif click == 2:
                v.drawX(2)
            elif click == 3:
                v.drawX(3)
            elif click == 4:
                v.drawX(4)
            elif click == 5:
                v.drawX(5)
            elif click == 6:
                v.drawX(6)
            elif click == 7:
                v.drawX(7)
            elif click == 8:
                v.drawX(8)

        # Tells view to draw the O's based on the click
        def playerO():
            if click == 0:
                v.drawO(0)
            elif click == 1:
                v.drawO(1)
            elif click == 2:
                v.drawO(2)
            elif click == 3:
                v.drawO(3)
            elif click == 4:
                v.drawO(4)
            elif click == 5:
                v.drawO(5)
            elif click == 6:
                v.drawO(6)
            elif click == 7:
                v.drawO(7)
            elif click == 8:
                v.drawO(8)

    def gameWin(self):

        # Defines the win conditions
        winConditions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [2,4,6], [0,4,8]]

        # Compares palyers' clicks to the win conditions.
        if self.playX in winConditions:
            v.message.setText("Player X wins!")
            self.runAgain()
        elif self.playO in winConditions:
            v.message.setText("Player O wins!")
            self.runAgain()
        else:
            return
        
    def runAgain(self, again):
        v.message.setText("Play again? (y/n)")

        answer = v.win.checkKey()

        if answer == "y":
            v.reset()
        if answer == "n":
            v.message.setText("Thanks for playing")
            time.sleep(10)
            v.win.close()

def ModelTest():
    
    v

if __name__ == "__main__":
    ModelTest()
