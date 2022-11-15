import pygame
from enum import Enum

#ウィンドウサイズの設定
Win_width = 1920
Win_height = 1080

#状態を列挙
class status(Enum):
    title = 0
    playing = 1

#色
class color():

    def __init__(self):
        self.white = [255, 255, 255]
        self.black = [0, 0, 0]
        self.gray = [193, 162, 129]
        self.blue = [51, 255, 255]
        self.w_blue = [204,255,255]
        self.orange = [255,127,0]


#ゲームの設定のクラス　
class system():

    def __init__(self):
        self.status = status.title
        self.run = True
        self.clicked = False
        self.dragging = False

        self.distance_x = 0
        self.distance_y = 0

        self.cursole_x = 0
        self.cursole_y = 0

        self.win = pygame.display.set_mode((Win_width, Win_height))
        pygame.display.set_caption("strategy")

        self.win_board_x = 20
        self.win_board_y = 80
        self.board_drag = False

    def update_cursole(self, x, y):
        self.cursole_x = x
        self.cursole_y = y

    def update_dragging(self, result):
        self.dragging = result

    def update_distance(self, x, y):
        self.distance_x = x
        self.distance_y = y

    def update_win_board(self, x, y):
        self.win_board_x = x
        self.win_board_y = y

    def on_clicked(self):
        self.clicked = True
    
    def on_board_drag(self):
        self.board_drag = True
    
    def off_board_drag(self):
        self.board_drag = False

    def off_clicked(self):
        self.clicked = False

    def off_run(self):
        self.run = False

#ゲーム情報を保持するクラス
class game():

    def __init__(self):
        self.board = [[[-1 for k in range(2)] for j in range(8)]for i in range(8)]