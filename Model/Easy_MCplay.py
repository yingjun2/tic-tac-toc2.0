import copy
import os
import random
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Controller.Dialog import Dialog
from View.Board_GUI import BoardWindow


class Easy_Test(BoardWindow,QMainWindow):
    def __init__(self, parent=None,n=1):
        super().__init__(parent)
        self.setupUi(self)

        # Shows only the close button
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        xIconPath = os.path.join("../icon", "X.png")
        oIconPath = os.path.join("../icon", "O.png")

        self.xIcon = QIcon(xIconPath)
        self.oIcon = QIcon(oIconPath)

        # To make the icons appear in full color while disabled
        self.xIcon.addPixmap(QPixmap(xIconPath), QIcon.Disabled)
        self.oIcon.addPixmap(QPixmap(oIconPath), QIcon.Disabled)

        self.allButtons = self.frame.findChildren(QToolButton)
        self.availabeButtons = self.allButtons[:]
        """"
        board
        """
        self.board = list('---------')

        # connections
        for button in self.allButtons:
            button.clicked.connect(self.button_clicked)

        self.actionNew_Game.triggered.connect(self.new_game)
        self.action_Exit.triggered.connect(self.close)

        self.setFocus()  # sets the focus to the main window
        self.new_game()  # starts a new game

    def new_game(self):
        self.reset()

    def reset(self):
        self.frame.setEnabled(True)
        self.availabeButtons = self.allButtons[:]
        self.board = list('---------')
        self.statusbar.showMessage("You are X. You play first")

        for button in self.availabeButtons:
            button.setText("")
            button.setIcon(QIcon())
            button.setEnabled(True)

    def end_game(self, state):
        """Ends the game"""

        if state == 1:
            # the computer win the game
            Dialog(self, state).show()

            for button in self.availabeButtons:
                button.setEnabled(False)
            self.availabeButtons.clear()
            return True

        elif state == 2:
            # the computer lose the game
            Dialog(self, state).show()

            for button in self.availabeButtons:
                button.setEnabled(False)
            self.availabeButtons.clear()
            return True

        elif state == 3:
            # it's a draw
            Dialog(self, state).show()

            for button in self.allButtons:
                button.setEnabled(False)
            return True
        return False

    def button_clicked(self):
        button = self.sender()

        buttonName = str(button.objectName())
        buttonIndex = int(buttonName[-1]) - 1

        """
        transfer index into board list position
        """
        self.board[buttonIndex] = 'X'

        # self.sounds["cross"].play()
        button.setText("1")
        button.setIcon(self.xIcon)
        button.setEnabled(False)
        self.availabeButtons.remove(button)

        winTest = self.check_win('X')
        if winTest != 2:
            if winTest == 1:
                self.end_game(2)
                return
            if winTest == -1:
                self.end_game(1)
                return

            self.end_game(3)
            return

        self.frame.setEnabled(False)
        # computer trail
        self.MC_round()

    def MC_trail(self,board,pc,n=1,w2=[0]*9,l2=[0]*9,d2=[0]*9):
        # choice = self.chooseRandomMoveFromList()
        """

        player positions
        """
        # x=0
        # while x<=n:
        #     x+=1
            # choice=random.choice(pc)
            # board1=copy.copy(board)
            # if self.isWin(self.selection(board1, choice)) is True:
                # w2[choice] += 1
            # elif self.isXLost(self.selection(board1,choice)) is True:
            #     l2[choice] += 1
            # elif self.isDraw(self.selection(board1,choice)) is True:
            #     d2[choice] += 1
            # elif self.notFinished(self.selection(board1,choice)) is True:
            #     choice1 = self.chooseRandomMoveFromList(board1)
            #     board2 = copy.copy(board1)
            #     (w3, l3, d3) = self.MC_trail(board2,choice1, 1, w2, l2, d2)
            #     if sum(w3) - sum(w2) != 0:
            #         l2[choice] += 1
            #     # if sum(l3) - sum(l2) != 0:
            #     #     l2[choice] += 1
            #     if sum(d3) - sum(d2) != 0:
            #         d2[choice] += 1

        return w2, l2, d2

    def selection(self, board,n):
        """
        This is a manually selection.

        For the
        """
        if board[n] == '-':
            m = board.count('-')
            if m % 2 == 0:
                board[n] = '0'
            else:
                board[n] = 'X'
                #     else:
                #         print("The position has already been occupied")
        return board

    def auto_selection(self,w2=[0]*9,l2=[0]*9,d2=[0]*9) -> int:

            # this is a 2nd method for auto-selection.
            # The problem is that that max wining occurrence is not enough to win.
            # the example is in the next cell
            """
            This program simply select the best move by count the most win occurrence.
            """
            # for i in range(9):
            #     if l2[i] != 0:
            #         w2[i] = 0

            # if w2.index(max(w2))>0:
            #     move = w2.index(max(w2))
            # else:
            #     move = random.choice([0,1,2,3,4,5,6,7,8])
            move = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

            return move

    def MC_round(self,number=100):

        pc = self.chooseRandomMoveFromList(self.board)
        # (w2, l2, d2) = self.MC_trail(self.board, pc,number, [0] * 9, [0] * 9, [0] * 9)
        move = self.auto_selection()
        while move not in pc:
            move = self.auto_selection()

        buttonIndex = move
        """

            player positions
        """
        self.board[buttonIndex] = '0'

        for buttonAvail in self.availabeButtons:
            buttonName = str(buttonAvail.objectName())
            buttonIndexNew = int(buttonName[-1]) - 1
            if buttonIndexNew == buttonIndex:
                button = buttonAvail
                # self.sounds["circle"].play()
                button.setText("2")
                button.setIcon(self.oIcon)
                button.setEnabled(False)
                self.availabeButtons.remove(button)
                break

        winTest = self.check_win('0')
        if winTest != 2:
            if winTest == 1:
                self.end_game(2)
                return
            if winTest == -1:
                self.end_game(1)
                return

            self.end_game(3)
            return

        self.frame.setEnabled(True)

    def chooseRandomMoveFromList(self,board):
        pc = [i for i, j in enumerate(board) if j == '-']
        #     print(pc)
        return pc

    def isWin(self, board):
        """
        GIven a board checks if it is in a winning state.
        Arguments:
              board: a list containing X,O or -.
        Return Value:
               True if board in winning state. Else False
        """
        #  check if any of the rows has winning combination
        for i in range(3):
            if (
                            len(set(board[i * 3:i * 3 + 3])) is 1 and
                            board[i * 3] is not '-'
            ):
                return True

        # check if any of the Columns has winning combination
        for i in range(3):
            if (
                            (board[i] is board[i + 3]) and
                            (board[i] is board[i + 6]) and
                            board[i] is not '-'
            ):
                return True

        # 2,4,6 and 0,4,8 cases
        # diagonal
        if (
                            board[0] is board[4] and
                            board[4] is board[8] and
                        board[4] is not '-'
        ):
            return True

        if (
                            board[2] is board[4] and
                            board[4] is board[6] and
                        board[4] is not '-'
        ):
            return True

        return False

    def isWinner(self,board):
        """
            This is to define the status of "isWin" (for X).

            >>> bb=['X', 'X', 'X', '-', 'X', 'O', '-', 'O', 'O']
            >>> print(isWin(bb))
            True
            """
        if (
                        self.isWin(board) is True and
                        board.count('-') % 2 == 0
        ):
            return True

        return False

    def isDraw(self,board):
        """
        This is to define the status of "isDraw".

        >>> bb=['X', 'X', 'O', 'O', 'X', 'X', 'X','O', 'O']
        >>> print(isDraw(bb))
        True
        """
        if (
                        self.isWin(board) is False and
                        board.count('-') == 0
        ):
            return True

        return False

    def isLost(self,board):
        if (
                    self.isWin(board) is True and
                    board.count('-') % 2 == 1
        ):
            return True

        return False

    def notFinished(self,board):
        """
            This is to define the status of "notFinish".

            >>> b=['X', 'X', 'O', 'X', '-', '-', '-', '-', 'O']
            >>> print(notFinish(b))
            False
        """
        if (
                        self.isWin(board) is False and
                        board.count('-') != 0
        ):
            return True

        return False

    def check_win(self, player):
        if self.isWin(self.board):
            if player is 'X':
                return -1
            else:
                return 1

        c = self.board.count('-')
        if c is 0:
            return 0
        return 2


def main():
    app = QApplication(sys.argv)
    game = Easy_Test()
    game.show()
    app.exec_()

if __name__ == '__main__':
    main()
