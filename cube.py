import pygame as py

class Cube:

    def __init__(self, x, y, size, type):
        self.x = x
        self.y = y
        self.size = size
        self.type = type
        
        if type == "pig":
            self.color = (255, 192, 203)
        elif type == "open":
            self.color = (200, 200, 200)
        elif type == "exit":
            self.color = (255, 255, 255)
        else: #wall
            self.color = (100, 100, 100)

    def draw(self, win):
        py.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

    def isPressed(self, xCor, yCor):

        if self.type == "open":
            if (self.x <= xCor and self.x + self.size >= xCor and
                self.y <= yCor and self.y + self.size >= yCor):
                return True
        
        return False
                                                                      