import pygame
import infor
import draw
import process
import key
from pygame.locals import *

def init():
    system = infor.system()
    color = infor.color()
    win = [infor.menu(), infor.board()]
    game = infor.game()

    return system, game, color, win

def main():

    pygame.init()

    system, game, color, win = init()

    while system.run:
        #表示の設定をリセット
        system.win.fill(color.black)

        #カーソルの位置を常に取得
        x_raw, y_raw = pygame.mouse.get_pos()
        system.cursole_update(x_raw, y_raw)

        for event in pygame.event.get():
            #右上のボタンを押すと終了
            if event.type == pygame.QUIT:
                system.run_off()
            
            #左クリックの有無
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                system.clicked_on()

            #左ドラッグの判定
            result = pygame.mouse.get_pressed()
            system.dragging_update(result[0])

            # キーを押したとき
            if event.type == KEYDOWN:  
                key.where(system, win, event)
                
        if system.status == infor.status.title:
            draw.title(system, color)

        if system.status == infor.status.playing:

            process.window(system, win)
            process.order(system, win, color)

        draw.cursole(system, color)
        pygame.time.delay(5)
        pygame.display.update()
        system.key_update(None)
        system.clicked_off()

if __name__ == '__main__':
    main()