import pygame
import infor

#どのボタンが押されたか判断する
def where(system, win, event):
    if pygame.key.name(event.key) == "b":
        system.key_update("b")
        push(system, win, infor.win_name.board)

    if pygame.key.name(event.key) == "m":
        system.key_update("m")
        push(system, win, infor.win_name.menu)
        

def push(system, win, name):
    system.active_log_update(name)
    if win[name.value].close == True:
        win[name.value].close_off()
    else:
        win[name.value].close_on()