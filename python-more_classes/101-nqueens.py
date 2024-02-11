#!/usr/bin/python3
import sys


def solveNQueens(n: int):
    col = []
    posDiag = []
    negDiag = []

    res = []
    board = []

    def backtrack(r):
        if r == n:
            res.append(board[:])
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.append(c)
            posDiag.append(r + c)
            negDiag.append(r - c)
            board.append([r, c])

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board.pop()
    backtrack(0)
    return res


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    num = int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)
if num < 4:
    print("N must be at least 4")
    exit(1)
solutions = solveNQueens(num)
for i in solutions:
    print(i)
