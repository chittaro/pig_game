import pygame as py
from tools import text

class Button:

    def __init__(self, x, y, wid, hgt, text, color):
        self.rect = py.Rect(round(x - wid/2), round(y - hgt/2), wid, hgt)
        self.text = text
        self.isLight = False
        self.dark = color
        self.light = (color[0] + 20, color[1] + 20, color[2] + 20)

    def draw(self, win):
        if self.isLight:
            color = self.light
        else:
            color = self.dark

        py.draw.rect(win, color, self.rect)
        tx = self.rect.x + (self.rect.width / 2)
        ty = self.rect.y + (self.rect.height / 2)
        text(win, self.text, tx, ty, self.rect.width / 3, (0, 0, 0))


    def isOn(self, x, y):
        r = py.Rect(x, y, 1, 1)
        if py.Rect.colliderect(self.rect, r):
            self.isLight = True
            return True
        
        self.isLight = False
        return False
