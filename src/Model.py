# Model.py
#
# For TicTacToe

# Keeps track of what's in each cell. Updates when told by the Controller. Provides logic and detirmines if there is a winner or a draw.

import View

v = View()

class Model:

    def __init__(self):
        cell0, cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8 = ""

        if cell0 is "X":
            v.cordx = 0.5
            v.cordy = 0.5
            v.fillX.setText("X")
            v.fillX.draw(v.win)
            gameWin()
            player = "O"
            return
        elif cell1 is "X":
            v.cordx = 1.5
            v.cordy = 0.5
            v.fillX.setText("X")
            v.fillX.draw(v.win)
        elif cell2 is "X":
            v.cordx = 2.5
            v.cordy = 0.5
            v.fillX.setText("X")
            v.fillX.draw(v.win)
        elif cell3 is "X":
            v.cordx = 0.5
            v.cordy = 1.5
            v.fillX.setText("X")
            v.fillX.draw(v.win)
        elif cell4 is "X":
            v.cordx = 1.5
            v.cordy = 1.5
            v.fillX.setText("X")
            v.fillX.draw(v.win)
        elif cell5 is "X":
            v.cordx = 2.5
            v.cordy = 1.5
            v.fillX.setText("X")
            v.fillX.draw(v.win)
        elif cell6 is "X":
            v.cordx = 0.5
            v.cordy = 2.5
            v.fillX.setText("X")
            v.fillx.draw(v.win)
        elif cell7 is "X":
            v.cordx = 1.5
            v.cordy = 2.5
            v.fillX.setText("X")
            v.fillX.draw(v.win)
        elif cell8 is "X":
            v.cordx = 2.5
            v.cordy = 2.5
            v.fillX.setText("X")
            v.fillX.draw(v.win)
        elif cell0 is "O":
            v.cordx = 0.5
            v.cordy = 0.5
            v.fillO.setText("O")
            v.fillO.draw(v.win)
        elif cell1 is "O":
            v.cordx = 1.5
            v.cordy = 0.5
            v.fillO.setText("O")
            v.fillO.draw(v.win)
        elif cell2 is "O":
            v.cordx = 2.5
            v.cordy = 0.5
            v.fillO.setText("O")
            v.fillO.draw(v.win)
        elif cell3 is "O":
            v.cordx = 0.5
            v.cordy = 1.5
            v.fillO.setText("O")
            v.fillO.draw(v.win)
        elif cell4 is "O":
            v.cordx = 1.5
            v.cordy = 1.5
            v.fillO.setText("O")
            v.fillO.draw(v.win)
        elif cell5 is "O":
            v.cordx = 2.5
            v.cordy = 1.5
            v.fillO.setText("O")
            v.fillO.draw(v.win)
        elif cell6 is "O":
            v.cordx = 0.5
            v.cordy = 2.5
            v.fillO.setText("O")
            v.fillO.draw(v.win)
        elif cell7 is "O":
            v.cordx = 1.5
            v.cordy = 2.5
            v.fillO.setText("O")
            v.fillO.draw(v.win)
        elif cell8 is "O":
            v.cordx = 2.5
            v.cordy = 2.5
            v.fillO.setText("O")
            v.fillO.draw(v.win)
        else:
            v.message.setText("Please choose an empty space.")

    def gameWin(self):
        if self.cell0 is "X" and self.cell1 is "X" and self.cell2 is "X":
            v.message.setText("Player X wins!")
        else:
            return

def ModelTest():
    
    pass

if __name__ == "__main__":
    ModelTest()
