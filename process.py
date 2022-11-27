import pygame
import infor

#アクティブウィンドウの管理、ドラック、座標移動など
def window(system, win):

    if system.clicked == True:
        for name in infor.win_name:
            base_x = win[name.value].x
            base_y = win[name.value].y
            #windowをクリックしたか判定し、アクティブ候補に追加
            if base_x < system.cursole_x and system.cursole_x < base_x+win[name.value].width:
                if base_y < system.cursole_y and system.cursole_y < base_y+win[name.value].height:
                    system.active_candidacy.append(name)

    #アクティブ候補のそれぞれがactive_logの何番目にあるか調べる
    active_list = []
    for i in range(len(system.active_candidacy)):
        for j in range(len(system.active_log)):
            if system.active_candidacy[i] == system.active_log[j]:
                active_list.append(j)
        
    #アクティブ候補がある場合アクティブを変更
    if len(active_list) != 0:
        min_index = 0
        for i in range(len(active_list)):
            if active_list[min_index] > active_list[i]:
                min_index = i
                
        system.active_log_update(system.active_candidacy[min_index])

        start_x = win[system.active_log[0].value].x
        start_y = win[system.active_log[0].value].y
            
        #閉じるアイコンをクリックしたか判定
        if start_x < system.cursole_x and system.cursole_x < start_x+system.icon:
            if start_y < system.cursole_y and system.cursole_y < start_y+system.icon:
                if system.clicked == True:
                    win[system.active_log[0].value].close_on()

        #バーの中をクリックしたか判定
        if start_x < system.cursole_x and system.cursole_x < start_x+win[system.active_log[0].value].width:
            if start_y < system.cursole_y and system.cursole_y < start_y+system.bar:
                if system.clicked == True:
                    system.distance_update(system.cursole_x-start_x,system.cursole_y-start_y)
                    win[system.active_log[0].value].drag_on()

    #ドラックしているか判定し、移動の処理、ドラック後の処理
    if win[system.active_log[0].value].drag == True:
        if system.dragging == True:
            win[system.active_log[0].value].update(system.cursole_x-system.distance_x, system.cursole_y-system.distance_y)
        else:
            win[system.active_log[0].value].drag_off()
            system.distance_update(0,0)

    system.active_candidacy_init()


#優先度によって描画する
def order(system, win, color):

    for i in reversed(range(0,len(win))):
        win[system.active_log[i].value].draw_flame(system, win, color)
        win[system.active_log[i].value].draw_content(system, win, color) 

    