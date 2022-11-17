import pygame

#どのボタンが押されたか判断する
def where(system, win, event):
    if pygame.key.name(event.key) == "b":
        system.key_update("b")
        if win.board_close == True:
            win.board_close_off()
        else:
            win.board_close_on()

    if pygame.key.name(event.key) == "m":
        system.key_update("m")
        if win.menu_close == True:
            win.menu_close_off()
        else:
            win.menu_close_on()