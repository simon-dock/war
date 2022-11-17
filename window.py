import pygame
import infor

def judge_active(system, win):

    #windowによって変更
    start_x = win.board_x
    start_y = win.board_y 

    #windowをクリックしたか判定
    if start_x < system.cursole_x and system.cursole_x < start_x+win.board_width:
        if start_y < system.cursole_y and system.cursole_y < start_y+win.board_height:
            if system.clicked == True:
                system.active_win_update(infor.active.board)#windowによって変更
    
    #閉じるアイコンをクリックしたか判定
    if start_x < system.cursole_x and system.cursole_x < start_x+win.icon:
        if start_y < system.cursole_y and system.cursole_y < start_y+win.icon:
            if system.clicked == True:
                win.board_close_on()#windowによって変更

    #バーの中をクリックしたか判定
    if start_x < system.cursole_x and system.cursole_x < start_x+win.board_width:
        if start_y < system.cursole_y and system.cursole_y < start_y+win.bar:
            if system.clicked == True:
                system.distance_update(system.cursole_x-start_x,system.cursole_y-start_y)
                win.board_drag_on()#windowによって変更

    #ドラックしているか判定し、移動の処理、ドラック後の処理
    if win.board_drag == True:#windowによって変更
        if system.dragging == True:

            #windowによって変更
            win.board_update(system.cursole_x-system.distance_x, system.cursole_y-system.distance_y)
        else:
            win.board_drag_off()#windowによって変更
            system.distance_update(0,0)


def board(system, win, color):

    if win.board_close == True:
        return

    #windowによって変更
    start_x = win.board_x
    start_y = win.board_y 

    #windowをクリックしたか判定
    if start_x < system.cursole_x and system.cursole_x < start_x+win.board_width:
        if start_y < system.cursole_y and system.cursole_y < start_y+win.board_height:
            if system.clicked == True:
                system.active_win_update(infor.active.board)#windowによって変更
    
    #閉じるアイコンをクリックしたか判定
    if start_x < system.cursole_x and system.cursole_x < start_x+win.icon:
        if start_y < system.cursole_y and system.cursole_y < start_y+win.icon:
            if system.clicked == True:
                win.board_close_on()#windowによって変更

    #バーの中をクリックしたか判定
    if start_x < system.cursole_x and system.cursole_x < start_x+win.board_width:
        if start_y < system.cursole_y and system.cursole_y < start_y+win.bar:
            if system.clicked == True:
                system.distance_update(system.cursole_x-start_x,system.cursole_y-start_y)
                win.board_drag_on()#windowによって変更

    #ドラックしているか判定し、移動の処理、ドラック後の処理
    if win.board_drag == True:#windowによって変更
        if system.dragging == True:

            #windowによって変更
            win.board_update(system.cursole_x-system.distance_x, system.cursole_y-system.distance_y)
        else:
            win.board_drag_off()#windowによって変更
            system.distance_update(0,0)

    #windowによって変更
    pygame.draw.rect(system.win, color.black_s, (start_x, start_y, win.board_width, win.board_height))
    pygame.draw.rect(system.win, color.white_s, (start_x, start_y, win.board_width, win.bar))
    pygame.draw.rect(system.win, color.red, (start_x+5, start_y+5, win.icon, win.icon))

def menu(system, win, color):

    if win.menu_close == True:
        return

    #windowによって変更
    start_x = win.menu_x
    start_y = win.menu_y 


    #windowをクリックしたか判定
    if start_x < system.cursole_x and system.cursole_x < start_x+win.menu_width:
        if start_y < system.cursole_y and system.cursole_y < start_y+win.menu_height:
            if system.clicked == True:
                system.active_win_update(infor.active.menu)#windowによって変更
    
    #閉じるアイコンをクリックしたか判定
    if start_x < system.cursole_x and system.cursole_x < start_x+win.icon:
        if start_y < system.cursole_y and system.cursole_y < start_y+win.icon:
            if system.clicked == True:
                win.menu_close_on()#windowによって変更

    #バーの中をクリックしたか判定
    if start_x < system.cursole_x and system.cursole_x < start_x+win.menu_width:
        if start_y < system.cursole_y and system.cursole_y < start_y+win.bar:
            if system.clicked == True:
                system.distance_update(system.cursole_x-start_x,system.cursole_y-start_y)
                win.menu_drag_on()#windowによって変更

    #ドラックしているか判定し、移動の処理、ドラック後の処理
    if win.menu_drag == True:#windowによって変更
        if system.dragging == True:

            #windowによって変更
            win.menu_update(system.cursole_x-system.distance_x, system.cursole_y-system.distance_y)
        else:
            win.menu_drag_off()#windowによって変更
            system.distance_update(0,0)

    #windowによって変更
    pygame.draw.rect(system.win, color.black_s, (start_x, start_y, win.menu_width, win.menu_height))
    pygame.draw.rect(system.win, color.white_s, (start_x, start_y, win.menu_width, win.bar))
    pygame.draw.rect(system.win, color.red, (start_x+5, start_y+5, win.icon, win.icon))
