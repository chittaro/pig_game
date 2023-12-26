import pygame as py

def text(win, words, x, y, size, color):
    font = py.font.SysFont('simsunextb', round(size), True, False)
    initTxt = font.render(words, 1, color)

    tWid, tHgt = font.size(words)
    finalX, finalY = x - (tWid / 2), y - (tHgt / 2)
    win.blit(initTxt, (round(finalX), round(finalY)) )
