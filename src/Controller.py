# Controller.py
#
# For TicTacToe

# Has the game loops. Outer loop does the game and another game. Inner loop gets the cell number and validates it. If empty, tells View to draw the symbol and tells Model to update cell data. Then asks Model if there is a winner. If not, switch players, if so, or if it's a draw, tells View to put up the right message and exit to the outer loop. Outer loop tells View to display correct message.

from View import View
from Model import Model
import time

class Controller:

    def __init__(self):

        self.v = View()
        self.m = Model(self.v)
        self.player = "X"


    # Starts the overall game.
    def playGame(self):
        done = False
        while not done:
            # Starts the first turn. The method will run until there is a winner, or the game is a tie.
            self.turn()

            # Asks if the users want to play another game. If so, 
            self.runAgain()

    # Goes through a turn and all available outcomes.
    def turn(self):

        self.player = "X"
        self.v.message.setText("It's Player X's turn.")
        
        while True:

            # Gets a click from the player.
            cellNum = self.v.getClick()
            
            # Validates the click. The while loop will continue to run if the user clicks in the message area or in an occupied cell. Once the user clicks in an empty cell, the outer loop will continue

            while cellNum:
                if cellNum == 9 or cellNum == 10 or cellNum == 11:
                    self.v.message.setText("Please click in the grid below.")
                    cellNum = self.v.getClick()
                    continue
                elif cellNum in self.m.playX:
                    self.v.message.setText("Please choose an empty space.")
                    cellNum = self.v.getClick()
                    continue
                elif cellNum in self.m.playO:
                    self.v.message.setText("Please choose an empty space.")
                    cellNum = self.v.getClick()
                    continue
                else:
                    break
            # Checks to see which player is playing. If X, the Model is called to draw an X in the cell and then to append that play to the "spaces played" list. If O, does the same thing, but for Player O.

            if self.player is "X":
                self.m.playerX(cellNum)
                self.m.playX.append(cellNum)
                self.m.playX.sort()
                print("X: " , self.m.playX)
            elif self.player is "O":
                self.m.playerO(cellNum)
                self.m.playO.append(cellNum)
                self.m.playO.sort()
                print("O: " , self.m.playO)

            # Defines a result variable based on Model's gameWin method. The returning result is then checked to see if the current player won, the game was a tie, or neither. If a player won, the game will display a win message for that player and then break out of the loop (and method) and return to playGame(). If the game is a tie, the game will display a tie message and return to playGame(). If neither, the game continues.

            result = self.m.gameWin()
            if result in ("X", "O"):
                self.v.message.setText("Player {} wins!".format(self.player))
                time.sleep(10)
                break
            elif result == "tie":
                self.v.message.setText("It's a tie!")
                time.sleep(10)
                break
            elif result == "continue":
                pass

            # Checks to see which player is active. The player is switched and the game displays a message for the next player. Loop then loops back to getting a click from the next player.

            if self.player is "X":
                self.player = "O"
                self.v.message.setText("It's Player O's turn.")
            elif self.player is "O":
                self.player = "X"
                self.v.message.setText("It's Player X's turn.")

    def runAgain(self):
        self.v.message.setText("Play again? (y/n)")

        answer = self.v.win.getKey()

        for key in answer:
            if answer == "y":
                self.v.reset()
                self.m.reset()
                break
            elif answer == "n":
                self.v.message.setText("Thanks for playing!")
                time.sleep(10)
                self.v.win.close()
            else:
                self.v.message.setText("Please type 'y' or 'n' to continue.")
                continue


def ControllerTest():
    
    c = Controller()

    c.playGame()
    

if __name__ == "__main__":
    ControllerTest()
