class Coord:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col
    
    def uCoord(self):
        return Coord(self.row - 1, self.col)
    
    def dCoord(self):
        return Coord(self.row + 1, self.col)
    
    def rCoord(self):
        return Coord(self.row, self.col + 1)
    
    def lCoord(self):
        return Coord(self.row, self.col - 1)
    
    def getNext(self, char):
        if (char == 'U'):
            return Coord(self.row + 1, self.col)
        elif (char == 'D'):
            return Coord(self.row - 1, self.col)
        elif (char == 'L'):
            return Coord(self.row, self.col + 1)
        else:
            return Coord(self.row, self.col - 1)