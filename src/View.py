# View.py
#
# For TicTacToe

# Joel Halnan

# Imports all of hte graphics functions from the graphics library
from graphics import *

class View:

    # Main part of the class
    def __init__(self):

        # List of objects to be undrawn when resetting window. Starts as empty and will be filled as players play the game.

        self.objectList = []

        # Initiates the window and sets the coordinates.

        self.win = GraphWin("Tic Tac Toe", 500, 500)
        self.win.setCoords(0,0,3,4)

        # Sets the background of the window to black. This creates a set of "borders" when the next two areas are drawn.
        self.win.setBackground("black")

        # Draws white rectangles for the play area and the message area.

        playArea = Rectangle(Point(0.05, 0.05), Point(2.95, 2.95))
        playArea.setFill("white")
        playArea.draw(self.win)

        messageArea = Rectangle(Point(0.05, 3.05), Point(2.95, 3.95))
        messageArea.setFill("white")
        messageArea.draw(self.win)

        # Sets the initial message and creates the message in the message area.

        self.message = Text(Point(1.5, 3.5), "")
        self.message.setSize(18)
        self.message.setTextColor("blue")
        self.message.draw(self.win)

        # Creates the grid

        gridLine = Line(Point(1, 0), Point(1, 3))
        gridLine.setWidth(3)
        gridLine.draw(self.win)
        gridLine = Line(Point(0, 1), Point(3, 1))
        gridLine.setWidth(3)
        gridLine.draw(self.win)
        gridLine = Line(Point(2, 0), Point(2, 3))
        gridLine.setWidth(3)
        gridLine.draw(self.win)
        gridLine = Line(Point(0, 2), Point(3, 2))
        gridLine.setWidth(3)
        gridLine.draw(self.win)

    # This draws an X when Player X makes a move.
    def drawX(self, click):
        
        # This if else if statement sets the X coordinate for the symbol to be drawn. 
        if click == 0 or click == 3 or click == 6:
            cordx = 0.5
        elif click == 1 or click == 4 or click == 7:
            cordx = 1.5
        elif click == 2 or click == 5 or click == 8:
            cordx = 2.5
        elif click == 9 or click == 10 or click == 11:
            self.message.setText("Please click in the grid below.")
            cordx = 5

        # This if else if statment sets the Y coordinate for the symbol to be drawn.
        if click == 0 or click == 1 or click == 2:
            cordy = 0.5
        elif click == 3 or click == 4 or click == 5:
            cordy = 1.5
        elif click == 6 or click == 7 or click == 8:
            cordy = 2.5
        elif click == 9 or click == 10 or click == 11:
            self.message.setText("Please click in the grid below.")
            cordy = 5
        
        # Draws the X based on the two above statements. The last line appends the object to the list created at the beginning so that it can be undrawn when reseting the game.
        fillX = Text(Point(cordx, cordy), "X")
        fillX.setFace("helvetica")
        fillX.setSize(36)
        fillX.setStyle("bold")
        fillX.setTextColor("purple")
        fillX.draw(self.win)
        self.objectList.append(fillX)

    # This draws the O when Player O makes a move. Except for the symbol, it is exactly the same as the previous method.
    def drawO(self, click):

        if click == 0 or click == 3 or click == 6:
            cordx = 0.5
        elif click == 1 or click == 4 or click == 7:
            cordx = 1.5
        elif click == 2 or click == 5 or click == 8:
            cordx = 2.5
        elif click == 9 or click == 10 or click == 11:
            self.message.setText("Please click in the grid below.")
            cordx = 5

        if click == 0 or click == 1 or click == 2:
            cordy = 0.5
        elif click == 3 or click == 4 or click == 5:
            cordy = 1.5
        elif click == 6 or click == 7 or click == 8:
            cordy = 2.5
        elif click == 9 or click == 10 or click == 11:
            self.message.setText("Please click in the grid below.")
            cordy = 5
        
        fillO = Text(Point(cordx, cordy), "O")
        fillO.setFace("helvetica")
        fillO.setSize(36)
        fillO.setStyle("bold")
        fillO.setTextColor("purple")
        fillO.draw(self.win)
        self.objectList.append(fillO)

    # This resets the board for a new game. The for loop undraws all of the symbols in the list. The last line then clears the list.
    def reset(self):
        for obj in self.objectList:
            obj.undraw()
        self.objectList.clear()

    # This method gets a click from the user and translates it to a cell number.
    def getClick(self):
        point = self.win.getMouse()
        cellNum = int(point.getY())*3 + int(point.getX())
        return cellNum

def ViewTest():
    pass

if __name__ == "__main__":
    ViewTest()