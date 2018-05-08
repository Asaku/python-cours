#!/usr/bin/env python
# coding: utf-8

import tkinter, random
import sys
sys.setrecursionlimit(8000)

grid = []

def generateNumber():
    return random.randint(1, 9)

def generateEmptyGrid():
    while len(grid) != 9:
        grid.append([0,0,0,0,0,0,0,0,0])
    return grid

# check if number is in columns
def checkNumber(position, line):
    number = generateNumber()
    while line.count(number) > 0:
        number = generateNumber()
    for l in grid:
        if l[position] == number:
            checkNumber(position, line)

    return number

def generateGrid():
    grid = generateEmptyGrid()
    for line in grid:
        for idx, p in enumerate(line):
            number = checkNumber(idx, line)
            line[idx] = number
    return grid


grid = generateGrid()


for l in grid:
    print(l)
