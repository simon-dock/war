import pygame
import infor
import draw
from pygame.locals import *

def init():
    system = infor.system()
    color = infor.color()

    return system, color

def main():

    pygame.init()

    system, color = init()

    run = True
    while run:
        system.win.fill(color.black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                first = False
                x_raw, y_raw = event.pos
        
        draw.board(system, color)
        pygame.time.delay(30)
        pygame.display.update()


if __name__ == '__main__':
    main()