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
def win_board(system, color):

    start_x = system.win_board_x-10
    start_y = system.win_board_y-40 
    end_x = system.win_board_x+990
    end_y = system.win_board_y+990

    if start_x < system.cursole_x and system.cursole_x < end_x:
        if start_y < system.cursole_y and system.cursole_y < start_y+40:
            if system.clicked == True:
                system.update_distance(system.cursole_x-system.win_board_x,system.cursole_y-system.win_board_y)
                system.on_board_drag()

    if system.board_drag == True:
        if system.dragging == True:
            system.update_win_board(system.cursole_x-system.distance_x, system.cursole_y-system.distance_y)
        else:
            system.off_board_drag()

    for i in range(9):
        for j in range(9):
            x_ren = 100*j+10*j+system.win_board_x
            y_ren = 100*i+10*i+system.win_board_y
            pygame.draw.rect(system.win, color.gray, (x_ren, y_ren, 100, 100))

    start_pos = [[start_x,start_y],[start_x,end_y],[end_x,end_y],[end_x,start_y]]
    pygame.draw.lines(system.win, color.white, True, start_pos, 2)

#カーソルを描画
def cursole(system, color):
    if system.dragging == True:
        pygame.draw.rect(system.win, color.orange, (system.cursole_x, system.cursole_y, 10, 10))
    else:
        pygame.draw.rect(system.win, color.blue, (system.cursole_x, system.cursole_y, 10, 10))

