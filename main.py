import random
import numpy as np
import tkinter as tk

BOARD_SIZE = 4
PERCENT_LOW = 0.9  # the percent that are 2 instead of 4 on randomization

board = np.zeros((BOARD_SIZE, BOARD_SIZE), int)


def compress_row(row):
    total_len = len(row)
    # print(f"comp row {row}")
    def compress_row_once(lst):
        dex = 0
        out = []

        while lst.count(0) != 0:
            lst.remove(0)

        if len(lst) == 0:
            return []
        while dex != len(lst):
            if dex == len(lst)-1:
                out.append(lst[dex])
            elif lst[dex] == lst[dex+1]:
                out.append(lst[dex]+1)
                dex += 1
            elif lst[dex] == 0:
                pass
            else:
                out.append(lst[dex])

            dex += 1
        # print(f"comp row once {lst}, {out}")
        return out

    row = compress_row_once(row)
    while row != compress_row_once(row):
        row = compress_row_once(row)
    while len(row) != total_len:
        row.append(0)
    return row

def shift_board(array:np.array, move):
    # according to the move shift the board so the numbers are the same
    move_shift = {'up':1, 'left':0, 'down':3, 'right':2}
    array = np.rot90(array, move_shift[move])
    out_array = []
    array = array.tolist()
    for row in array:
        out_array.append(compress_row(row))
    out = np.array(out_array)
    out = np.rot90(out, 4-move_shift[move])
    return out




def keep_playing(array:np.array):
    flat = list(array.flatten())
    if flat.count(0) != 0:
        return True
    for mve in ['up','down','right','left']:
        if not np.array_equal(array,shift_board(array, mve)):
            return True
    return False


GAME = True
ROUND = 0
board[random.randint(0,BOARD_SIZE-1), random.randint(0,BOARD_SIZE-1)] = 2 if random.uniform(0,1) > PERCENT_LOW else 1
while GAME:
    ROUND += 1
    print(ROUND)
    new_tuple = (random.randint(0,BOARD_SIZE-1),random.randint(0,BOARD_SIZE-1))
    while board[new_tuple] != 0:
        new_tuple = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
    board[new_tuple] = 2 if random.uniform(0,1) > PERCENT_LOW else 1
    print(board)

    GAME = keep_playing(board)
    if not GAME:
        break

    next_move = input("What move do you want to make? (up, down, left, right) > ")

    while next_move not in ['up', 'down', 'left', 'right']:
        next_move = input("Invalid move. Try again. > ")
    new_board = shift_board(board, next_move)
    while np.array_equal(board, new_board):
        next_move = input("What move do you want to make? (up, down, left, right) > ")
        print(board)
        while next_move not in ['up', 'down', 'left', 'right']:
            next_move = input("Invalid move. Try again. > ")


    # new_board = shift_board(board, 'down')
    # while np.array_equal(board, new_board):
    #     print("bad mve")
    #     new_board = shift_board(board, random.choice(['up', 'down', 'right', 'left']))
    board = new_board

print(f"{0:_>250}")

