#!/usr/bin/env python
# coding: utf-8

stick = 21

print("|||| Welcome to the Nim game ||||")

print(" | "*stick)

lastPlayer = None

while stick > 0:
    number = int(input("Player 1"))
    stick = stick - number
    print(" | " * stick)
    lastPlayer = "Player 1"

    number2 = int(input("Player 2"))
    stick = stick - number2
    print(" | " * stick)
    lastPlayer = "Player 2"

print("Lose "+lastPlayer)
