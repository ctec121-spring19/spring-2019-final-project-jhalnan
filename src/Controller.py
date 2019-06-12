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
        click = v.getClick()

        # First part of inner loop checks to see if the space is available. Second statement sees if the user clicked in the non-play area. The Else statement appends the move to the lists in the Model and switches players.
        while playAgain is True:
            
            if click in m.playX or click in m.playO:
                v.message.setText("Please choose an empty space.")
            elif click in m.npa:
                v.message.setText("Please click in the grid below.")
            else:
                if player is "X":
                    m.playX.append(click)
                    player = "O"
                elif player is "O":
                    m.playO.append(click)
                    player = "X"



def ControllerTest():
    
    pass

if __name__ == "__main__":
    ControllerTest()
