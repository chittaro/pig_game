import pygame as py

class Cube:

    def __init__(self, x, y, size, type):
        self.rect = py.Rect(x, y, size, size)
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
        if self.type != "exit":
            py.draw.rect(win, self.color, self.rect)

    def isPressed(self, xCor, yCor):
        rect2 = py.Rect(xCor, yCor, 1, 1)

        if self.type == "open":
            if py.Rect.colliderect(self.rect, rect2):
                return True
        
        return False
                                                                      