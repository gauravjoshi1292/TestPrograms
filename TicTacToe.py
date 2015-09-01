from graph import *


class TicTacToe:
    def __init__(self):
        self.graph = Graph()

    def legal_moves_x(self, board):
        retVal = []
        if self.has_x_won(board):
            return retVal
        if self.has_o_won(board):
            return retVal
        for i in range(len(board)):
            if board[i] == " ":
                tmp = board[0:i] + "X" + board[i+1:]
                if tmp.count("X") - tmp.count("O") == 0 or tmp.count("X") - tmp.count("O") == 1:
                    retVal.append(tmp)
        return retVal

    def legal_moves_o(self, board):
        retVal = []
        if self.has_x_won(board):
            return retVal
        if self.has_o_won(board):
            return retVal
        for i in range(len(board)):
            if board[i] == " ":
                tmp = board[0:i] + "O" + board[i+1:]
                if tmp.count("X") - tmp.count("O") == 0 or tmp.count("X") - tmp.count("O") == 1:
                    retVal.append(tmp)
        return retVal

    def has_x_won(self, board):
        win = False
        f = True
        for i in range(3):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(3, 6):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(6, 9):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(0, 9, 3):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(1, 9, 3):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(2, 9, 3):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(0, 9, 4):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(2, 7, 2):
            if board[i] != 'X':
                f = False
                break
        win = win or f
        if win is True:
            return win

    def has_o_won(self, board):
        win = False
        f = True
        for i in range(3):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(3, 6):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(6, 9):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(0, 9, 3):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(1, 9, 3):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(2, 9, 3):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(0, 9, 4):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

        f = True
        for i in range(2, 7, 2):
            if board[i] != 'O':
                f = False
                break
        win = win or f
        if win is True:
            return win

    def is_tied(self, board):
        if not self.has_x_won(board) and not self.has_o_won(board):
            return True
        else:
            return False

win_for_x = 0
win_for_o = 0
full_board_tie = 0
legal_boards = 0

game = TicTacToe()
start_pos = "         "
start_v = game.graph.addVertex(start_pos)
turn = "X"

from collections import deque

queue = deque()
queue.append(start_v)

tie_list = []

while queue:
    u = queue.popleft()

    legal_boards += 1
    if game.has_x_won(u.id):
        win_for_x += 1
    elif game.has_o_won(u.id):
        win_for_o += 1
    elif game.is_tied(u.id) and not " " in u.id:
        full_board_tie += 1
        tie_list.append(u.id)

    possible_moves = game.legal_moves_x(u.id)
    for move in possible_moves:
        if move not in game.graph:
            v = game.graph.addVertex(move)
            game.graph.addEdge(u, v, 1)
            queue.append(v)

    possible_moves = game.legal_moves_o(u.id)
    for move in possible_moves:
        if move not in game.graph:
            v = game.graph.addVertex(move)
            game.graph.addEdge(u, v, 1)
            queue.append(v)

print("Total vertices that result in win for X = " + str(win_for_x))
print("Total vertices that result in win for O = " + str(win_for_o))
print("Total vertices that result in a tie = " + str(full_board_tie))
print("Total number of legal boards = " + str(legal_boards))


if len(tie_list) != len(set(tie_list)):
    print("FUCK")