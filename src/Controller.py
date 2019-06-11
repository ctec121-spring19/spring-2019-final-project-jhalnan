# Controller.py
#
# For TicTacToe

# Has the game loops. Outer loop does the game and another game. Inner loop gets the cell number and validates it. If empty, tells View to draw the symbol and tells Model to update cell data. Then asks Model if there is a winner. If not, switch players, if so, or if it's a draw, tells View to put up the right message and exit to the outer loop. Outer loop tells View to display correct message.

import View
import Model

v = View()
m = Model()

class Controller:

    def __init__(self):
        
        player = "X"
        playAgain = True

        while playAgain is True:
            if Model.cell0 is "":
                Model.cell0 = player
            elif Model.cell1 is "":
                Model.cell1 = player
            elif Model.cell2 is "":
                Model.cell2 = player
            elif Model.cell3 is "":
                Model.cell3 = player
            elif Model.cell4 is "":
                Model.cell4 = player
            elif Model.cell5 is "":
                Model.cell5 = player
            elif Model.cell6 is "":
                Model.cell6 = player
            elif Model.cell7 is "":
                Model.cell7 = player
            elif Model.cell8 is "":
                Model.cell8 = player
            else:
                v.message.setText("Please choose an empty space.")



def ControllerTest():
    
    pass

if __name__ == "__main__":
    ControllerTest()
