# -*- coding: utf-8 -*-

# challenge 157 easy


input = """
O
O--
OOX
---
"""

def build_board(input):
    """
    makes board with input
    """

    raw = input.strip().split("\n")

    # next move
    next_move = raw.pop(0)

    print next_move, raw
    
    # list comprehension to make board from raw
    board = [[i for i in row] for row in raw]
    return board, next_move 

def find_move(board, next_move):
    for i in range(len(board)):
        if board[i].count(next_move) == 2 and board[i].count('-') == 1:
            print "found"
            board[i] = [next_move, next_move, next_move]
            return board, True 
    return board, False

def check_diag(board, next_move):
    diag1 = [board[i][i] for i in range(3)]
    if diag1[i]count(next_move) == 2 and board[i].count('-') == 1:
        print "found"
        board
    max = len(board)
    diag2 = [board[i][max-i-1] for i in range(3)]
    

def main():
    
    board, next_move = build_board(input) 
    check_diag(board, next_move)
    board_final, found = find_move(board, next_move)
    if not found:
        print "inside vertical"
        rotate = [[board[i][j] for i in range(3)] for j in range(3)] 
        board, found = find_move(rotate, next_move)
        board_final = [[board[i][j] for i in range(3)] for j in range(3)]
    print board_final 

if __name__ == "__main__":
    main()


    



