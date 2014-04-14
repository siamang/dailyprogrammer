#!/usr/bin/python
# -*- coding: utf-8 -*-

# challenge 157 easy

input1 = """
O
O-X
-XX
O--
"""
input2 = """
X
XO-
OO-
---
"""
input3 = """
O
OXOX
OOXX
--O-
----
"""


def build_board(input):
    raw = input.strip().split('\n')
    next_move = raw.pop(0)
    board = [[i for i in row] for row in raw]
    return (board, next_move)

def find_move(board, next_move):
    for i in range(len(board)):
        if board[i].count(next_move) == len(board) - 1 \
            and board[i].count('-') == 1:
            for j in range(len(board)):
                board[i][j] = next_move
            return (board, True)
    return (board, False)

def check_diag(board, next_move):
    max = len(board)
    
    # top left to bottom right
    diag1 = [board[i][i] for i in range(max)]
    if diag1.count(next_move) == max - 1 and diag1.count('-') == 1:
        for i in range(max):
            for j in range(max):
                if i == j:
                    board[i][j] = next_move
        return (board, True)

    # top right to bottom left
    diag2 = [board[i][max - i - 1] for i in range(max)]
    if diag2.count(next_move) == max - 1 and diag2.count('-') == 1:
        for i in range(max):
            for j in range(max):
                if i == abs(j - max + 1):
                    board[i][j] = next_move
        return (board, True)
    return (board, False)


def main(input):
    (board, next_move) = build_board(input)
    (board_final, found) = check_diag(board, next_move)
    if not found:
        (board_final, found) = find_move(board, next_move)
        if not found:
            
            # rotate board to check vertical
            rotate = [[board[i][j] for i in range(len(board))] for j in
                      range(len(board))]
            (board_final, found) = find_move(rotate, next_move)
            
            # rotate back
            for i in range(3):
                board_final = [[board_final[i][j] for i in
                               range(len(board))] for j in
                               range(len(board))]
                
    # print result
    if not found:
        print 'No winning Move!'
    else:
        for i in range(len(board)):
            print ''.join(board_final[i])
    print ''

if __name__ == '__main__':
    main(input1)
    main(input2)
    main(input3)