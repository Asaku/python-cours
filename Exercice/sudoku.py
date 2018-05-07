#!/usr/bin/env python
# coding: utf-8

import tkinter, random

grid = []

def generateEmptyGrid():
    while len(grid) != 9:
        grid.append([0,0,0,0,0,0,0,0,0])
    return grid

def checkNumber(number, position):
    for l in grid:
        if l[position] == number:
            return False
    return True

def generateGrid():
    grid = generateEmptyGrid()
    for line in grid:
        for idx, p in enumerate(line):
            print("idx etape 1 ", idx)
            number = random.randint(1, 9)
            # check if number is in columns
            print("idx etape 2 ", idx)
            if checkNumber(number, idx):
                line.append(number)
    return grid


grid = generateGrid()


# for l in grid:
#     print(l)
