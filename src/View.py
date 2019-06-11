# View.py
#
# For TicTacToe

# Does all the graphic things, gets the click and converts it to a cell number

from graphics import *

class View:

    def __init__(self):

        #initiates the window and sets the coordinates.

        self.win = GraphWin("TicTacToe", 500, 500)
        self.win.setCoords(0,0,3,4)

        self.win.setBackground("black")

        #draws white area for the play area and the message area.

        playArea = Rectangle(Point(0.05, 0.05), Point(2.95, 2.95))
        playArea.setFill("white")

        messageArea = Rectangle(Point(0.05, 3.05), Point(2.95, 3.95))
        messageArea.setFill("white")

        #sets the initial message and creates the message in the message area.

        textForMessage = "It's Player X's turn."

        message = Text(Point(1.5, 3.5), textForMessage)
        message.setSize(18)
        message.setTextColor("blue")

        #creates the grid

        gridLine1 = Line(Point(1, 0), Point(1, 3))
        gridLine1.setWidth(3)
        gridLine3 = Line(Point(0, 1), Point(3, 1))
        gridLine3.setWidth(3)

        gridLine2 = gridLine1.clone()
        gridLine2.move(1,0)
        gridLine4 = gridLine3.clone()
        gridLine4.move(0,1)

        #draws all the things.

        gridDrawList = [playArea, messageArea, message, gridLine1, gridLine2, gridLine3, gridLine4]

        for item in gridDrawList:
            item.draw(self.win)

        cordx = 0.5
        cordy = 0.5

        fillX = Text(Point(cordx, cordy), "X")
        fillX.setFace("helvetica")
        fillX.setSize(36)
        fillX.setStyle("bold")
        fillX.setTextColor("purple")
    
        fillO = fillX.clone()

    def getClick(self):
        point = self.win.getMouse()
        cellNum = int(point.getY())*3 + int(point.getX())
        return cellNum

def ViewTest():
    
    v = View()
    while v.win:
        print(v.getClick())
    input()
    

if __name__ == "__main__":
    ViewTest()
