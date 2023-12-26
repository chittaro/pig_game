import pygame as py
from puzzle import Puzzle
from coord import Coord


nRows, nCols = 7, 7

puzz = Puzzle(nRows, nCols)

puzz.fillBacktrace()
puzz.printGrid()

nextCoord = puzz.getNextMove()
print(nextCoord.getRow())
print(nextCoord.getCol())