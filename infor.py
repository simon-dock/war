import pygame
from enum import Enum

#ウィンドウサイズの設定
Win_width = 1920
Win_height = 1080

#状態を列挙
class status(Enum):
    title = 0
    playing = 1

#windowを列挙
class active(Enum):
    board = 0
    menu = 1

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
        self.active_win = active.board
        self.active_log = [active.board, active.menu]
        self.run = True
        self.clicked = False
        self.dragging = False

        self.key = None

        self.cursole_x = 0
        self.cursole_y = 0

        self.distance_x = 0
        self.distance_y = 0

        self.space = 10

        self.win = pygame.display.set_mode((Win_width, Win_height))
        pygame.display.set_caption("strategy")

    def active_win_update(self, result):
        self.active_win = result

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
class win():

    def __init__(self):
        self.icon = 30
        self.bar = 40

        self.board_x = 10
        self.board_y = 10
        self.board_width = 1000
        self.board_height = 1040
        self.board_drag = False
        self.board_close = False

        self.menu_x = 1500
        self.menu_y = 10
        self.menu_width = 200
        self.menu_height = 1040
        self.menu_drag = False
        self.menu_close = False

    def board_update(self, x, y):
        self.board_x = x
        self.board_y = y

    def board_drag_on(self):
        self.board_drag = True
    
    def board_drag_off(self):
        self.board_drag = False

    def board_close_on(self):
        self.board_close = True

    def board_close_off(self):
        self.board_close = False


    def menu_update(self, x, y):
        self.menu_x = x
        self.menu_y = y

    def menu_drag_on(self):
        self.menu_drag = True
    
    def menu_drag_off(self):
        self.menu_drag = False

    def menu_close_on(self):
        self.menu_close = True

    def menu_close_off(self):
        self.menu_close = False


#ゲーム情報を保持するクラス
class game():

    def __init__(self):
        self.board = [[[-1 for k in range(2)] for j in range(8)]for i in range(8)]