import pygame as py
from puzzle import Puzzle
from coord import Coord
import time


nRows, nCols = 7, 7

puzz = Puzzle(nRows, nCols)

while (puzz.isGameOver() != True):
    print("--------")
    time.sleep(2)
    puzz.pigNextMove()

print("game ove")