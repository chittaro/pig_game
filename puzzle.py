import pygame as py
from collections import deque
from coord import Coord

class Puzzle:

    def __init__(self, nRows, nCols):
        self.grid = []
        self.backtrace = []
        self.queue = deque()

        self.endCoord = Coord(0, 0)
        self.end = False

        self.wallStr = '#'
        self.openStr = 'O'
        self.exitStr = 'X'
        self.pigStr = 'P'

        self.pCoord = Coord(round(nRows / 2) - 1, round(nCols / 2) - 1)

        for r in range(nRows):
            self.grid.append([])

            for c in range(nCols):
                if (r == 0) or (r == nRows - 1) or (c == 0) or (c == nCols - 1):
                    self.grid[r].append(self.exitStr)
                else:
                    self.grid[r].append(self.openStr)
        
        self.grid[self.pCoord.getRow()][self.pCoord.getCol()] = self.pigStr


    def printGrid(self):
        for r in self.grid:
            for c in r:
                print(c, end = " ")
            print()

    def fillBacktrace(self):
        self.backtrace = self.grid
        self.end = False

        self.discover(self.pCoord, '*')

        while len(self.queue) > 0 and self.end != True:
            
            coor = self.queue[0]
            self.queue.popleft()

            self.discover(coor.uCoord(), 'U')
            self.discover(coor.dCoord(), 'D')
            self.discover(coor.lCoord(), 'L')
            self.discover(coor.rCoord(), 'R')


    def discover(self, coord, char):
        crtMap = self.grid[coord.getRow()][coord.getCol()]
        crtBt = self.backtrace[coord.getRow()][coord.getCol()]

        if (crtMap == self.openStr and crtBt == self.openStr) or crtBt == self.pigStr:
            self.queue.append(coord)
            crtBt = self.backtrace[coord.getRow()][coord.getCol()] = char

        elif crtMap == self.exitStr:
            crtBt = self.backtrace[coord.getRow()][coord.getCol()] = char
            self.end = True
            self.endCoord = coord