import pygame as py
from puzzle import Puzzle


nRows, nCols = 7, 7

puzz = Puzzle(nRows, nCols)

puzz.fillBacktrace()
puzz.printGrid()