import pygame
import draw
from enum import Enum

#ウィンドウサイズの設定
Win_width = 1920
Win_height = 1080

#状態を列挙
class status(Enum):
    title = 0
    playing = 1

#windowを列挙
class win_name(Enum):
    menu = 0
    board = 1
    side = 2

#色
class color():

    def __init__(self):
        self.white = [255, 255, 255]
        self.white_s = [224, 224, 224]
        self.black = [0, 0, 0]
        self.black_s = [30, 30, 30]
        self.gray = [193, 162, 129]
        self.blue = [51, 255, 255]
        self.w_blue = [204,255,255]
        self.orange = [255,127,0]
        self.red = [255, 0, 0]


#ゲームの設定のクラス　
class system():

    def __init__(self):
        self.status = status.title
        self.active_candidacy = []
        self.active_log = [win_name.board, win_name.menu, win_name.side]
        self.run = True
        self.clicked = False
        self.dragging = False

        self.key = None

        self.cursole_x = 0
        self.cursole_y = 0

        self.distance_x = 0
        self.distance_y = 0

        self.icon = 30
        self.bar = 40
        self.space = 10

        self.win = pygame.display.set_mode((Win_width, Win_height))
        pygame.display.set_caption("strategy")

    def active_candidacy_init(self):
        self.active_candidacy = []

    def active_log_update(self, result):
        past_order = 0
        for i in range(len(self.active_log)):
            if result == self.active_log[i]:
                past_order = i
                break

        tmp_now = self.active_log[0]
        tmp_next = 0
        for i in range(past_order):
            tmp_next = self.active_log[i+1]
            self.active_log[i+1] = tmp_now
            tmp_now = tmp_next

        self.active_log[0] = result

    def run_off(self):
        self.run = False

    def clicked_on(self):
        self.clicked = True

    def clicked_off(self):
        self.clicked = False

    def dragging_update(self, result):
        self.dragging = result

    def key_update(self, result):
        self.key = result

    def cursole_update(self, x, y):
        self.cursole_x = x
        self.cursole_y = y

    def distance_update(self, x, y):
        self.distance_x = x
        self.distance_y = y


#windowの情報を保持するクラス
class menu():

    def __init__(self):
        self.name = win_name.menu
        self.x = 1500
        self.y = 10
        self.width = 400
        self.height = 600
        self.drag = False
        self.close = False

    def draw_flame(self, system, win, color):
        draw.flame(system, win, color, self.name)

    def draw_content(self, system, win, color):
        pass

    def update(self, x, y):
        self.x = x
        self.y = y

    def drag_on(self):
        self.drag = True
    
    def drag_off(self):
        self.drag = False

    def close_on(self):
        self.close = True

    def close_off(self):
        self.close = False


class board():

    def __init__(self):
        self.name = win_name.board
        self.x = 10
        self.y = 10
        self.width = 1000
        self.height = 1040
        self.drag = False
        self.close = False

    def draw_flame(self, system, win, color):
        draw.flame(system, win, color, self.name)

    def draw_content(self, system, win, color):
        draw.board(system, win, color)

    def update(self, x, y):
        self.x = x
        self.y = y

    def drag_on(self):
        self.drag = True
    
    def drag_off(self):
        self.drag = False

    def close_on(self):
        self.close = True

    def close_off(self):
        self.close = False

class side():

    def __init__(self):
        self.name = win_name.side
        self.x = 400
        self.y = 10
        self.width = 300
        self.height = 600
        self.drag = False
        self.close = False

    def draw_flame(self, system, win, color):
        draw.flame(system, win, color, self.name)

    def draw_content(self, system, win, color):
        pass

    def update(self, x, y):
        self.x = x
        self.y = y

    def drag_on(self):
        self.drag = True
    
    def drag_off(self):
        self.drag = False

    def close_on(self):
        self.close = True

    def close_off(self):
        self.close = False


#ゲーム情報を保持するクラス
class game():

    def __init__(self):
        self.board = [[[-1 for k in range(2)] for j in range(8)]for i in range(8)]