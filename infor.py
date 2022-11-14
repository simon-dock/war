import pygame
from enum import Enum

WIN_WIDTH = 1100
WIN_HEIGHT = 1200

#状態を列挙
class status(Enum):
    title = 0

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
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("strategy")
        self.board = [[[-1 for k in range(2)] for j in range(8)]for i in range(8)]