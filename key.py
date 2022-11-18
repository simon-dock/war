import pygame
import infor

#どのボタンが押されたか判断する
def where(system, win, event):
    if pygame.key.name(event.key) == "b":
        system.key_update("b")
        system.active_win_update(infor.win_name.board)
        if win[infor.win_name.board.value].close == True:
            win[infor.win_name.board.value].close_off()
        else:
            win[infor.win_name.board.value].close_on()

    if pygame.key.name(event.key) == "m":
        system.key_update("m")
        system.active_win_update(infor.win_name.menu)

        if win[infor.win_name.menu.value].close == True:
            win[infor.win_name.menu.value].close_off()
        else:
            win[infor.win_name.menu.value].close_on()