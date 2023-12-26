import pygame as py
from collections import deque
from coord import Coord
from cube import Cube
import copy

class Puzzle:

    def __init__(self, nRows, nCols, wid, hgt):
        self.rows = nRows
        self.cols = nCols
        self.wid = wid
        self.hgt = hgt

        self.grid = []
        self.backtrace = []
        self.visGrid = []
        self.queue = deque()

        self.endCoord = Coord(0, 0)
        self.end = False
        self.gameOver = False

        self.wallStr = '#'
        self.openStr = 'O'
        self.exitStr = 'X'
        self.pigStr = 'P'

        self.pCoord = Coord(round(nRows / 2), round(nCols / 2))

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
        self.backtrace = copy.deepcopy(self.grid)
        self.end = False
        self.queue = deque()

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
            self.backtrace[coord.getRow()][coord.getCol()] = char

        elif crtMap == self.exitStr:
            self.backtrace[coord.getRow()][coord.getCol()] = char
            self.end = True
            self.endCoord = coord


    def getNextMove(self):

        prevCoord = self.endCoord
        pchar = self.backtrace[prevCoord.getRow()][prevCoord.getCol()]

        nextCoord = prevCoord.getNext(pchar)
        char = self.backtrace[nextCoord.getRow()][nextCoord.getCol()]

        while char != '*':
            prevCoord = nextCoord
            nextCoord = nextCoord.getNext(char)

            char = self.backtrace[nextCoord.getRow()][nextCoord.getCol()]

        return prevCoord
    
    def isGameOver(self):
        return self.gameOver
    
    
    def pigNextMove(self, win):
        win.fill( (255, 255, 255) )


        self.fillBacktrace()
        next = self.getNextMove()
        self.move(next)
        self.fillVis()
        self.drawVis(win)
        
        py.display.update()

    def move(self, c):
        nextChar = self.grid[c.getRow()][c.getCol()]

        self.grid[c.getRow()][c.getCol()] = self.pigStr
        self.grid[self.pCoord.getRow()][self.pCoord.getCol()] = self.openStr
        self.pCoord = c

        if (nextChar == self.exitStr):
            self.gameOver = True


    def fillVis(self):
        size = 40
        sep = 15
        self.visGrid = []

        yPos = (self.hgt / 2) - (((self.rows / 2) + 1) * size) - ((((self.rows - 1) / 2) + 1) * sep)

        for r in range(self.rows):
            xPos = (self.wid / 2) - (((self.cols / 2) + 1) * size) - ((((self.cols - 1) / 2) + 1) * sep)
            #print("start = " + str(xPos))
            yPos += size + sep
            self.visGrid.append([])

            for c in range(self.cols):
                char = self.grid[r][c]
                xPos += size + sep

                if char == self.pigStr:
                    cube = Cube(round(xPos), round(yPos), size, "pig")
                elif char == self.openStr:
                    cube = Cube(round(xPos), round(yPos), size, "open")
                elif char == self.wallStr:
                    cube = Cube(round(xPos), round(yPos), size, "wall")
                else:
                    cube = Cube(round(xPos), round(yPos), size, "exit")

                self.visGrid[r].append(cube)


    def clickCheck(self, xCor, yCor):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.visGrid[r][c].isPressed(xCor, yCor):
                    self.grid[r][c] = self.wallStr
                    print(str(r) + ", " + str(c))
                    return True
        return False

    
    def drawVis(self, win):
        for r in self.visGrid:
            for c in r:
                c.draw(win)