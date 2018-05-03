#!/usr/bin/env python
# coding: utf-8

import tkinter, random

grid = []

def checkNumber(number, position):
    for line in grid:
        try:
            if line[position] == number:
                return False
        except:
            pass
    return True

def generateGrid():
    while len(grid) != 9:
        grid.append([])
    for line in grid:
        while len(line) != 9:
            number = random.randint(0, 9)
            if not line.count(number):
                if checkNumber(number, len(line)):
                    line.append(number)

    for l in grid:
        print(l)

generateGrid()
