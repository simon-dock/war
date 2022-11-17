import pygame
from pygame.locals import *
import infor

#タイトルの画面
def title(system, color):

    template = pygame.font.SysFont(None,100)

    if system.clicked == True:
        system.status = infor.status.playing
    text = template.render("War Strategy Game", True, color.white)
    system.win.blit(text, (600,400))


#movable_positionとboardをもとに盤面と選択されている駒、可動範囲を描画する
def board(system, win, color):

    if win.board_close == True:
        return

    for i in range(9):
        for j in range(9):
            x_ren = 100*j+10*j + win.board_x+system.space
            y_ren = 100*i+10*i + win.board_y+win.bar+system.space
            pygame.draw.rect(system.win, color.gray, (x_ren, y_ren, 100, 100))


#カーソルを描画
def cursole(system, color):
    if system.dragging == True:
        pygame.draw.rect(system.win, color.orange, (system.cursole_x, system.cursole_y, 10, 10))
    else:
        pygame.draw.rect(system.win, color.blue, (system.cursole_x, system.cursole_y, 10, 10))

