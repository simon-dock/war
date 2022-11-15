import pygame
import infor
import draw
from pygame.locals import *

def init():
    system = infor.system()
    color = infor.color()
    game = infor.game()

    return system, game, color

def main():

    pygame.init()

    system, game, color = init()

    while system.run:
        #表示の設定をリセット
        system.win.fill(color.black)

        #カーソルの位置を常に取得
        x_raw, y_raw = pygame.mouse.get_pos()
        system.update_cursole(x_raw, y_raw)

        for event in pygame.event.get():
            #右上のボタンを押すと終了
            if event.type == pygame.QUIT:
                system.off_run()
            
            #左クリックの有無
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                system.on_clicked()

            #左ドラッグの判定
            result = pygame.mouse.get_pressed()
            system.update_dragging(result[0])

        if system.status == infor.status.title:
            draw.title(system, color)
        if system.status == infor.status.playing:
            draw.win_board(system, color)
        
        draw.cursole(system, color)
        pygame.time.delay(5)
        pygame.display.update()
        system.off_clicked()

if __name__ == '__main__':
    main()