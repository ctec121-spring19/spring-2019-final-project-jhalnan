# View.py
#
# For TicTacToe

# Does all the graphic things, gets the click and converts it to a cell number

from graphics import *

class View:

    def __init__(self):

        # list of objects to be undrawn when resetting window.

        self.objectList = []

        #initiates the window and sets the coordinates.

        self.win = GraphWin("Tic Tac Toe", 500, 500)
        self.win.setCoords(0,0,3,4)

        self.win.setBackground("black")

        #draws white area for the play area and the message area.

        playArea = Rectangle(Point(0.05, 0.05), Point(2.95, 2.95))
        playArea.setFill("white")
        playArea.draw(self.win)

        messageArea = Rectangle(Point(0.05, 3.05), Point(2.95, 3.95))
        messageArea.setFill("white")
        messageArea.draw(self.win)

        #sets the initial message and creates the message in the message area.

        self.message = Text(Point(1.5, 3.5), "")
        self.message.setSize(18)
        self.message.setTextColor("blue")
        self.message.draw(self.win)

        #creates the grid

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

    def drawX(self, click):
        
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
        
        fillX = Text(Point(cordx, cordy), "X")
        fillX.setFace("helvetica")
        fillX.setSize(36)
        fillX.setStyle("bold")
        fillX.setTextColor("purple")
        fillX.draw(self.win)
        self.objectList.append(fillX)

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

    def reset(self):
        for obj in self.objectList:
            obj.undraw()
        self.objectList.clear()

    def getClick(self, cellNum):
        point = self.win.getMouse()
        cellNum = int(point.getY())*3 + int(point.getX())
        return cellNum

def ViewTest():
    pass

if __name__ == "__main__":
    ViewTest()