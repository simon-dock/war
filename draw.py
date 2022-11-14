import pygame
import infor

#movable_positionとboardをもとに盤面と選択されている駒、可動範囲を描画する
def board(system, color):

    for i in range(8):
        for j in range(8):
            x_ren = 100*(j+1)+10*j
            y_ren = 100*(i+1)+10*i
            
            pygame.draw.rect(system.win, color.gray, (x_ren, y_ren, 100, 100))

    start_pos = [[80,80],[990,80],[990,990],[80,990]]
    pygame.draw.lines(system.win, color.white, True, start_pos, 2)