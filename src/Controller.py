# Controller.py
#
# For TicTacToe

# Joel Halnan

# This imports the View and Model classes from the View and Model files.
from View import View
from Model import Model

# This imports the time library, which is used when displaying some of the messages.
import time

class Controller:

    # Main part of the class.
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

        # A game always starts with Player X. These two lines set the player to X and display the appropriate message.
        self.player = "X"
        self.v.message.setTextColor("blue")
        self.v.message.setText("It's Player X's turn.")
        
        while True:

            # Gets a click from the player.
            cellNum = self.v.getClick()
            
            # Validates the click. While the click is in an unacceptable area, the loop will continue.
            while cellNum:
                # This checks to see if the click is in the message area. If so, it tells the player to click in the play grid.
                if cellNum == 9 or cellNum == 10 or cellNum == 11:
                    self.v.message.setTextColor("red")
                    self.v.message.setText("Please click in the grid below.")
                    cellNum = self.v.getClick()
                    continue
                # The next two parts of the if else if statement check to see if the cell is already occupied. If so, it tells the player to choose an empty space.
                elif cellNum in self.m.playX:
                    self.v.message.setTextColor("red")
                    self.v.message.setText("Please choose an empty space.")
                    cellNum = self.v.getClick()
                    continue
                elif cellNum in self.m.playO:
                    self.v.message.setTextColor("red")
                    self.v.message.setText("Please choose an empty space.")
                    cellNum = self.v.getClick()
                    continue
                # If the user clicks in an unoccupied space in the play grid, the while loop is broken and play will continue.
                else:
                    break

            # Checks to see which player is playing. 
            # If X, the Model is called to draw an X in the cell and then to append that play to the "spaces played" list and then sort the list.
            # If O, does the same thing, but for Player O.
            if self.player is "X":
                self.m.playerX(cellNum)
                self.m.playX.append(cellNum)
                self.m.playX.sort()
            elif self.player is "O":
                self.m.playerO(cellNum)
                self.m.playO.append(cellNum)
                self.m.playO.sort()

            # Defines a result variable based on Model's gameWin method. The returning result is then checked to see if the current player won, the game was a tie, or neither. If a player won, the game will display a win message for that player and then break out of the loop (and method) and return to playGame(). If the game is a tie, the game will display a tie message and return to playGame(). If neither, the game continues.
            result = self.m.gameWin()
            
            if result in ("X", "O"):
                self.v.message.setText("Player {} wins!".format(self.player))
                # This loop changes the color of the win message and cycles through a few different colors for five seconds.
                for i in range(10):
                    self.v.message.setTextColor("red")
                    time.sleep(.125)
                    self.v.message.setTextColor("yellow")
                    time.sleep(.125)
                    self.v.message.setTextColor("green")
                    time.sleep(.125)
                    self.v.message.setTextColor("blue")
                    time.sleep(.125)
                break
            elif result == "tie":
                self.v.message.setText("It's a tie!")
                # This loop changes the color of the tie message and cycles through a few different colors for five seconds.
                for i in range(10):
                    self.v.message.setTextColor("red")
                    time.sleep(.125)
                    self.v.message.setTextColor("yellow")
                    time.sleep(.125)
                    self.v.message.setTextColor("green")
                    time.sleep(.125)
                    self.v.message.setTextColor("blue")
                    time.sleep(.125)
                break
            elif result == "continue":
                pass

            # Checks to see which player is active. The player is switched and the game displays a message for the next player. Loop then loops back to getting a click from the next player.
            if self.player is "X":
                self.player = "O"
                self.v.message.setText("It's Player O's turn.")
                self.v.message.setTextColor("white")
                time.sleep(.25)
                self.v.message.setTextColor("blue")
            elif self.player is "O":
                self.player = "X"
                self.v.message.setText("It's Player X's turn.")
                self.v.message.setTextColor("white")
                time.sleep(.25)
                self.v.message.setTextColor("blue")

    # This method asks the players if they want to play another game.
    def runAgain(self):
        self.v.message.setText("Play again? (y/n)")
        self.v.message.setTextColor("white")
        time.sleep(.25)
        self.v.message.setTextColor("blue")

        answer = self.v.win.getKey()

        # This while loop will continue to run until the user types a "y" or an "n."
        while True:
            if answer == "y":
                self.v.reset()
                self.m.reset()
                break
            elif answer == "n":
                self.v.message.setText("Thanks for playing!")
                for i in range(10):
                    self.v.message.setTextColor("red")
                    time.sleep(.125)
                    self.v.message.setTextColor("yellow")
                    time.sleep(.125)
                    self.v.message.setTextColor("green")
                    time.sleep(.125)
                    self.v.message.setTextColor("blue")
                    time.sleep(.125)
                self.v.win.close()
            else:
                self.v.message.setTextColor("red")
                self.v.message.setText("Please type 'y' or 'n' to continue.")
                answer = self.v.win.getKey()
                continue


def ControllerTest():
    pass
    

if __name__ == "__main__":
    ControllerTest()
