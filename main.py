import pygame as py
from puzzle import Puzzle
from coord import Coord
import time
from tools import text
from button import Button


nRows, nCols = 9, 9
wwid, whgt = 500, 500
py.init()
win = py.display.set_mode((wwid, whgt))
py.display.set_caption('PIG')


run = True
pressing = False
mode = "menu"

playButton = Button(wwid/2, whgt/2, 300, 100, "PLAY", (150, 200, 150))

while run:

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()
    mosX, mosY = py.mouse.get_pos()
    pressed = py.mouse.get_pressed()

    win.fill( (255, 255, 255) )

    if mode == "menu":
        playButton.draw(win)
        if playButton.isOn(mosX, mosY) and pressed[0]:
            mode = "play"

            puzz = Puzzle(nRows, nCols, wwid, whgt)
            clicks = 1
            puzz.setPressing()


    elif mode == "play":


        puzz.clickCheck(win, mosX, mosY, pressed)
        puzz.drawVis(win)

        if puzz.isGameOver():
            text(win, "GAME OVER", wwid/2, 35, 50, (200, 0, 0))
            py.display.update()
            time.sleep(2)
            run = False

        elif puzz.blocked():
            text(win, "PIG IS BLOCKED", wwid/2, 35, 50, (100, 200, 100))
            py.display.update()
            time.sleep(2)
            run = False

    py.display.update()



py.quit()