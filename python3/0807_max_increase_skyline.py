#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n----- | Leetcode 807. Max Increase to Keep City Skyline. | =====\n')

grid = [[3, 0, 8, 4],
        [2, 4, 5, 7],
        [9, 2, 6, 3],
        [0, 3, 1, 0]]

m = len(grid)  # no. of rows
n = len(grid[0])  # no. of columns
max_row = [max(x) for x in grid]
max_col = [max(x) for x in zip(*grid)]

rst = 0
for ix in range(m):
    for iy in range(n):
        rst += min(max_row[ix], max_col[iy]) - grid[ix][iy]

if rst == 35:
    print(f'Result = {rst}. ----- Wunderbar! You got correct result.')
