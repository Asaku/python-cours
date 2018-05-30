#!/usr/bin/env python
# coding: utf-8

import random
import sys
sys.setrecursionlimit(8000)

grid = []

def generateNumber():
    return random.randint(1, 9)

def generateEmptyGrid():
    while len(grid) != 9:
        grid.append([0,0,0,0,0,0,0,0,0])
    return grid

# check if number is in column
def checkColumn(position, number):
    for l in grid:
        if l[position] == number:
            return False
    return True

# check if number is in line
def checkLine(line, number):
    if line.count(number) > 0:
        return False
    return True

def generateGrid():
    grid = generateEmptyGrid()
    for line in grid:
        for idx, p in enumerate(line):
            number = 0
            check = False
            while not check:
                number = generateNumber()
                if checkLine(line, number) and checkColumn(idx, number):
                    check = True

            line[idx] = number
    return grid

grid = generateGrid()

for l in grid:
    print(l)
