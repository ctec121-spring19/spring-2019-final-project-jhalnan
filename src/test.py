
from graphics import *

def main():

    win = GraphWin("TicTacToe", 500, 500)
    win.setCoords(0,0,3,4)

    win.setBackground("black")

    playArea = Rectangle(Point(0.05, 0.05), Point(2.95, 2.95))
    playArea.setFill("white")

    messageArea = Rectangle(Point(0.05, 3.05), Point(2.95, 3.95))
    messageArea.setFill("white")

    textForMessage = "It's Player X's turn."

    message = Text(Point(1.5, 3.5), textForMessage)
    message.setSize(18)
    message.setTextColor("blue")

    gridLine1 = Line(Point(1, 0), Point(1, 3))
    gridLine1.setWidth(3)
    gridLine3 = Line(Point(0, 1), Point(3, 1))
    gridLine3.setWidth(3)

    gridLine2 = gridLine1.clone()
    gridLine2.move(1,0)
    gridLine4 = gridLine3.clone()
    gridLine4.move(0,1)

    drawList = [playArea, messageArea, message, gridLine1, gridLine2, gridLine3, gridLine4]

    for item in drawList:
        item.draw(win)

    cordx = 1.5
    cordy = 1.5

    fillX = Text(Point(cordx, cordy), "X")
    fillX.setFace("helvetica")
    fillX.setSize(36)
    fillX.setStyle("bold")
    fillX.setTextColor("purple")
    
    fillO = fillX.clone()
    fillO.setText("O")

    input()

main()