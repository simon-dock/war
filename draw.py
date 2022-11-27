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

    if win[infor.win_name.board.value].close == True:
        return

    for i in range(9):
        for j in range(9):
            x_ren = 100*j+10*j + win[infor.win_name.board.value].x+system.space
            y_ren = 100*i+10*i + win[infor.win_name.board.value].y+system.bar+system.space
            pygame.draw.rect(system.win, color.gray, (x_ren, y_ren, 100, 100))


def flame(system, win, color, name):

    if win[name.value].close == True:
        return

    start_x = win[name.value].x
    start_y = win[name.value].y
    
    pygame.draw.rect(system.win, color.black_s, (start_x, start_y, win[name.value].width, win[name.value].height))
    pygame.draw.rect(system.win, color.white_s, (start_x, start_y, win[name.value].width, system.bar))
    pygame.draw.rect(system.win, color.red, (start_x+5, start_y+5, system.icon, system.icon))
    pos = [[start_x,start_y],[start_x,start_y+win[name.value].height],[start_x+win[name.value].width,start_y+win[name.value].height],[start_x+win[name.value].width,start_y]]
    pygame.draw.lines(system.win, color.white_s, True, pos, 2)

#カーソルを描画
def cursole(system, color):
    if system.dragging == True:
        pygame.draw.rect(system.win, color.orange, (system.cursole_x, system.cursole_y, 10, 10))
    else:
        pygame.draw.rect(system.win, color.blue, (system.cursole_x, system.cursole_y, 10, 10))