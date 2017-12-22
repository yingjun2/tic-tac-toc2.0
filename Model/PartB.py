import copy
import random
from Model.Med_MCplay import Med_Test


class PartB:
    def __init__(self, lvla, lvlb, times):
        from View.Board_GUI import chalWindow
        self.chalWindow = chalWindow()
        self.lvla = lvla
        self.lvlb = lvlb
        self.times = times
        """
        board
        """
        self.board = list('---------')
        from Model.Hard_MCplay import Hard_Test
        self.Hard_Test = Hard_Test()

    @staticmethod
    def judge(board):
        """
        The method is for judging the current status of the board finish or not.
        :param board: a list of position status.
        :return: state of 'w', 'l' or 'd'

        """
        if PartB.isWinner(board) == 1:
            state = 'w';
        elif PartB.isDraw(board) == 1:
            state = 'd';
        elif PartB.isLost(board) == 1:
            state = 'l';
        else:
            state = None
        # print(state)
        return state

    def single_game(self, board):
        board = self.board[:]
        m = board.count('-')
        while m > 0:
            if m % 2 == 1:
                if self.lvla == 'easy':
                    self.easy(board)
                    # m = board.count('-')
                elif self.lvla == 'medium':
                    self.medium(board)
                    # m = board.count('-')
                elif self.lvla == 'hard':
                    self.hard(board)
                    # m = board.count('-')
            elif (m % 2 == 0) & (m != 0):
                # print(self.lvlb) ##
                if self.lvlb == 'easy':
                    self.easy(board)
                    # m = board.count('-')
                elif self.lvlb == 'medium':
                    self.medium(board)
                    # m = board.count('-')
                elif self.lvlb == 'hard':
                    self.hard(board)
                    # m = board.count('-')

            state = PartB.judge(board)
            if state in ['l', 'w', 'd']:
                # print(board)
                print(state)
                # return state
                break
                # return state
            else:
                m = board.count('-')

        # print(board)
        return state

    @staticmethod
    def selection(board, n):
        """
        This is the selection. turn the move selected into effect.
        """
        if board[n] == '-':
            m = board.count('-')
            if m % 2 == 0:
                board[n] = '0'
            else:
                board[n] = 'X'
        return board

    @staticmethod
    def easy(board):
        pc = [i for i, j in enumerate(board) if j == '-']
        move = random.choice(pc)
        PartB.selection(board, move)
        return board

    @staticmethod
    def MC_trail1(board, pc, n: object = 100, w2: object = [0] * 9, l2: object = [0] * 9,
                  d2: object = [0] * 9) -> object:
        # choice = self.chooseRandomMoveFromList()
        """

        player positions
        :param n:
        :param n:
        :type board: object
        """
        x = 0
        while x <= n:
            x += 1
            choice = random.choice(pc)
            board1 = copy.copy(board)
            if PartB.isWin(PartB.selection(board1, choice)) is True:
                w2[choice] += 1
            elif PartB.isDraw(PartB.selection(board1, choice)) is True:
                d2[choice] += 1
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

    def medium(self, board):
        pc = [i for i, j in enumerate(board) if j == '-']
        (w2, l2, d2) = self.MC_trail1(board, pc, self.times, [0] * 9, [0] * 9, [0] * 9)
        # print(w2,l2,d2)
        move = PartB.auto_selection(w2, l2)
        while move not in pc:
            move = PartB.auto_selection(w2, l2)
        # move = random.choice(pc)
        PartB.selection(board, move)
        #         board.pop(0)
        #         m = board.count('-')
        # print(board)##
        return board

    def MC_trail(self, board, pc, n=1, w2=[0] * 9, l2=[0] * 9, d2=[0] * 9):
        # choice = self.chooseRandomMoveFromList()
        """
        what does w2,l2,d2,board,pc mean?
        w2: win [0,0,0,0,0,0,0,0,0] initialize the winning score for every position
        l2: lose score for every pos
        d2: draw score for every pos
        board: the board?【3*3？yes】
        pc: all the possible vacant pos eq
        position ：available positions(vacant)
        player positions

        """
        # choice = self.chooseRandomMoveFromList()
        """
        player positions
        """
        x = 0
        while x <= n:
            x += 1
            choice = random.choice(pc)
            board1 = copy.copy(board)
            if self.isWin(self.selection(board1, choice)) is True:
                w2[choice] += 1
            # elif self.isXLost(self.selection(board1,choice)) is True:
            #     l2[choice] += 1
            elif self.isDraw(self.selection(board1, choice)) is True:
                d2[choice] += 1
            elif self.notFinished(self.selection(board1, choice)) is True:
                # choice1 = [i for i, j in enumerate(board1) if j == '-']
                choice1 = self.chooseRandomMoveFromList(board1)
                (w3, l3, d3) = self.MC_trail(board1, choice1, 1, w2, l2, d2)
                if sum(w3) - sum(w2) != 0:
                    l2[choice] += 1
                # if sum(l3) - sum(l2) != 0:
                #     l2[choice] += 1
                if sum(d3) - sum(d2) != 0:
                    d2[choice] += 1

        return w2, l2, d2

    # def selection(self, board, n):
    #     """
    #     This is a manually selection.
    #
    #     For the
    #     """
    #     if board[n] == '-':
    #         m = board.count('-')
    #         if m % 2 == 0:
    #             board[n] = '0'
    #         else:
    #             board[n] = 'X'
    #             #     else:
    #             #         print("The position has already been occupied")
    #     return board

    @staticmethod
    def auto_selection(w2, l2) -> int:

        # this is a 2nd method for auto-selection.
        # The problem is that that max wining occurrence is not enough to win.
        # the example is in the next cell
        """
        This program simply select the best move by count the most win occurrence.
        """
        for i in range(9):
            if l2[i] != 0:
                w2[i] = 0

        if w2.index(max(w2)) > 0:
            move = w2.index(max(w2))
        else:
            move = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

        return move

    def chooseRandomMoveFromList(self, board):
        pc = [i for i, j in enumerate(board) if j == '-']
        #     print(pc)
        return pc

    def hard(self, board):
        pc = self.chooseRandomMoveFromList(board)
        (w2, l2, d2) = self.MC_trail(board, pc, self.times, [0] * 9, [0] * 9, [0] * 9)
        move = self.auto_selection(w2, l2)
        while move not in pc:
            move = self.auto_selection(w2, l2)
        # move = random.choice(pc)
        self.selection(board, move)
        #         board.pop(0)
        #         m = board.count('-')
        # print(board)##
        print(board)

        return board

    @staticmethod
    def isWin(board):
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
                            board[4] is board[6] and board[4] is not '-'
        ):
            return True

        return False

    @staticmethod
    def isWinner(board):
        """
            This is to define the status of "isWin" (for X).

            >>> bb=['X', 'X', 'X', '-', 'X', 'O', '-', 'O', 'O']
            >>> print(isWin(bb))
            True
            """
        if (PartB.isWin(board) is True and
                board.count('-') % 2 == 0):
            return True

        return False

    @staticmethod
    def isDraw(board):
        """
        This is to define the status of "isDraw".

        >>> bb=['X', 'X', 'O', 'O', 'X', 'X', 'X','O', 'O']
        >>> print(isDraw(bb))
        True
        """
        if (PartB.isWin(board) is False and
                board.count('-') == 0):
            return True

        return False

    @staticmethod
    def isLost(board):
        if (
                        PartB.isWin(board) is True and
                board.count('-') % 2 == 1):
            return True

        return False

    @staticmethod
    def notFinished(board):
        """
            This is to define the status of "notFinish".

            >>> b=['X', 'X', 'O', 'X', '-', '-', '-', '-', 'O']
            >>> print(notFinish(b))
            False
            """
        if (PartB.isWin(board) is False and
                board.count('-') != 0):
            return True

        return False

    def MC_games(self):
        #         times=self.times
        st_list = []
        x = 0
        #         print(self.times)
        while x < self.times:
            s = self.single_game(self.board)
            # print(s)
            st_list.append(s)
            x += 1

        # print(st_list)
        #         print(st_list.count('w'),st_list.count('d'),st_list.count('l'))
        win = st_list.count('w') / self.times
        draw = st_list.count('d') / self.times
        lose = st_list.count('l') / self.times
        print(self.lvla, self.lvlb)
        print(win, draw, lose, self.times)
        return win, draw, lose


# def main():
#     test = partb('easy', 'easy', 100)
#     print(test.board)
#     state = partb.single_game(test)
#     print(state)
#
#
# if __name__ == '__main__':
#     main()

