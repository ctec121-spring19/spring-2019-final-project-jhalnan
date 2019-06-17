# Model.py
#
# For TicTacToe

# Joel Halnan

# This imports the View class from the View file.
from View import View

class Model:

    # Main part of the class.
    def __init__(self, view):
        
        self.v = view

        # These two lists are the lists for each player's moves. These lists are appended from the Controller class.
        self.playX = []
        self.playO = []

    # Tells view to draw the X's based on the user's click
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

    # Tells view to draw the O's based on the user's click
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

    # This method checks to see if a game has been won by either player or is a tie. 
    def gameWin(self):

        # This first part of the if else if statement checks the playX list to see if any winning combination is in the list. If so, it returns "X" to the Controller.
        if (0 in self.playX and 1 in self.playX and 2 in self.playX) or (3 in self.playX and 4 in self.playX and 5 in self.playX) or (6 in self.playX and 7 in self.playX and 8 in self.playX) or (0 in self.playX and 3 in self.playX and 6 in self.playX) or (1 in self.playX and 4 in self.playX and 7 in self.playX) or (2 in self.playX and 5 in self.playX and 8 in self.playX) or (2 in self.playX and 4 in self.playX and 6 in self.playX) or (0 in self.playX and 4 in self.playX and 8 in self.playX):
            return "X"
        # This part of the statement checks the playO list to see if any winning combination is in the list. If so, it returns "O" to the Controller.
        elif (0 in self.playO and 1 in self.playO and 2 in self.playO) or (3 in self.playO and 4 in self.playO and 5 in self.playO) or (6 in self.playO and 7 in self.playO and 8 in self.playO) or (0 in self.playO and 3 in self.playO and 6 in self.playO) or (1 in self.playO and 4 in self.playO and 7 in self.playO) or (2 in self.playO and 5 in self.playO and 8 in self.playO) or (2 in self.playO and 4 in self.playO and 6 in self.playO) or (0 in self.playO and 4 in self.playO and 8 in self.playO):
            return "O"
        # This part of the statement checks to see if both players have played a combined total of nine times. If so, it returns "tie" to the Controller to signify that the game is a draw.
        elif len(self.playX) + len(self.playO) == 9:
            return "tie"
        # If none of the above are true, this method returns "continue" to the Controller so that play can continue to the next player.
        else:
            return "continue"

    # This method clears the play lists when the game is reset.
    def reset(self):
        self.playX.clear()
        self.playO.clear()

def ModelTest():
    
    pass

if __name__ == "__main__":
    ModelTest()
