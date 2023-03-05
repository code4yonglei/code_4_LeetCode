#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n----- 36. Valid Sudoku =====.')

def isValidSudoku(board:list):  # 向函数传递list，遇到过向函数传递 xxx:dict
    row, col, blk = set(), set(), set()
    for ix in range(9):
        for iy in range(9):
            if board[ix][iy] != '.':
                value = board[ix][iy]
                row_key = (ix, value)
                col_key = (iy, value)
                blk_key = (ix//3, iy//3, value)
                if (row_key in row) or (col_key in col) or (blk_key in blk):
                    return False
                row.add(row_key)
                col.add(col_key)
                blk.add(blk_key)
    return True

if __name__ == '__main__':
    board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print('Is board1 being a valid Sudoku?=====', isValidSudoku(board1))

    board2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print('Is board2 being a valid Sudoku?=====', isValidSudoku(board2))

