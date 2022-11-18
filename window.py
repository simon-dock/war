import pygame
import infor

def process(system, win):

    #windowによって変更

    if system.clicked == True:

        for name in infor.win_name:
            base_x = win[name.value].x
            base_y = win[name.value].y

            #windowをクリックしたか判定
            if base_x < system.cursole_x and system.cursole_x < base_x+win[name.value].width:
                if base_y < system.cursole_y and system.cursole_y < base_y+win[name.value].height:
                    system.active_candidacy.append(name)

    active_list = []
    for i in range(len(system.active_candidacy)):
        for j in range(len(system.active_log)):
            if system.active_candidacy[i] == system.active_log[j]:
                active_list.append(j)
        
    if len(active_list) != 0:
        min_index = 0
        for i in range(len(active_list)):
            if active_list[min_index] > active_list[i]:
                min_index = i
                
        system.active_win_update(system.active_candidacy[min_index])

        start_x = win[system.active_win.value].x
        start_y = win[system.active_win.value].y
            
        #閉じるアイコンをクリックしたか判定
        if start_x < system.cursole_x and system.cursole_x < start_x+system.icon:
            if start_y < system.cursole_y and system.cursole_y < start_y+system.icon:
                if system.clicked == True:
                    win[system.active_win.value].close_on()#windowによって変更

        #バーの中をクリックしたか判定
        if start_x < system.cursole_x and system.cursole_x < start_x+win[system.active_win.value].width:
            if start_y < system.cursole_y and system.cursole_y < start_y+system.bar:
                if system.clicked == True:
                    system.distance_update(system.cursole_x-start_x,system.cursole_y-start_y)
                    win[system.active_win.value].drag_on()#windowによって変更

    #ドラックしているか判定し、移動の処理、ドラック後の処理
    if win[system.active_win.value].drag == True:#windowによって変更
        if system.dragging == True:
            #windowによって変更
            win[system.active_win.value].update(system.cursole_x-system.distance_x, system.cursole_y-system.distance_y)
        else:
            win[system.active_win.value].drag_off()#windowによって変更
            system.distance_update(0,0)

    system.active_candidacy_init()


def board(system, win, color):

    if win[infor.win_name.board.value].close == True:
        return

    start_x = win[infor.win_name.board.value].x
    start_y = win[infor.win_name.board.value].y
    #windowによって変更
    pygame.draw.rect(system.win, color.black_s, (start_x, start_y, win[infor.win_name.board.value].width, win[infor.win_name.board.value].height))
    pygame.draw.rect(system.win, color.white_s, (start_x, start_y, win[infor.win_name.board.value].width, system.bar))
    pygame.draw.rect(system.win, color.red, (start_x+5, start_y+5, system.icon, system.icon))

def menu(system, win, color):

    if win[infor.win_name.menu.value].close == True:
        return

    #windowによって変更
    start_x = win[infor.win_name.menu.value].x
    start_y = win[infor.win_name.menu.value].y

    #windowによって変更
    pygame.draw.rect(system.win, color.black_s, (start_x, start_y, win[infor.win_name.menu.value].width, win[infor.win_name.menu.value].height))
    pygame.draw.rect(system.win, color.white_s, (start_x, start_y, win[infor.win_name.menu.value].width, system.bar))
    pygame.draw.rect(system.win, color.red, (start_x+5, start_y+5, system.icon, system.icon))
