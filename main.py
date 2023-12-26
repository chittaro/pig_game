import pygame as py
from puzzle import Puzzle
from coord import Coord
import time


nRows, nCols = 9, 9
wwid, whgt = 500, 500
py.init()
win = py.display.set_mode((wwid, whgt))
py.display.set_caption('PIG')


puzz = Puzzle(nRows, nCols, wwid, whgt)

win.fill( (255, 255, 255))
puzz.fillVis()
puzz.drawVis(win)
py.display.update()

run = True
pressing = False
while run:

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()
    mosX, mosY = py.mouse.get_pos()
    pressed = py.mouse.get_pressed()

    if (pressed[0] == 1 and pressing != True):
        if (puzz.clickCheck(mosX, mosY)):
            puzz.pigNextMove(win)
            pressing = True

    elif (pressed[0] == 0):
        pressing = False

    if (puzz.isGameOver()):

        run = False

print("game ove")



py.quit()