import pygame
from pygame.locals import *
import sys

#ウィンドウの初期化
pygame.init()
WIN_WIDTH = 1100
WIN_HEIGHT = 1200
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


pygame.display.set_caption("Chess")


#駒情報を読み出し、記憶する配列
pieces = [['0' for j in range(6)]for i in range(2)]
for i in range(2):
    for j in range(6):
        pieces[i][j] = pygame.image.load(f"./image/{i}{j}.png")


#盤面、選ばれた座標、駒の可動範囲を記憶する配列
board = [[[-1 for k in range(2)] for j in range(8)]for i in range(8)]
select_position = [[-1 for j in range(8)]for i in range(8)]
movable_position = [[-1 for j in range(8)]for i in range(8)]


#色
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GRAY = [193, 162, 129]
BLUE = [51, 255, 255]
W_BLUE = [204,255,255]
ORANGE = [255,127,0]

#フラグ
B_KING_MOVED = False
B_QUEENSIDE_ROOK_MOVED = False
B_KINGSIDE_ROOK_MOVED = False

W_KING_MOVED = False
W_QUEENSIDE_ROOK_MOVED = False
W_KINGSIDE_ROOK_MOVED = False


#movable_positionとboardをもとに盤面と選択されている駒、可動範囲を描画する
def draw_board():

    WIN.fill(BLACK)

    for i in range(8):
        for j in range(8):
            x_ren = 100*(j+1)+10*j
            y_ren = 100*(i+1)+10*i
            if movable_position[i][j] == 1:
                pygame.draw.rect(WIN, BLUE, (x_ren, y_ren, 100, 100))
            elif movable_position[i][j] == 2:
                pygame.draw.rect(WIN, W_BLUE, (x_ren, y_ren, 100, 100))
            else:
                pygame.draw.rect(WIN, GRAY, (x_ren, y_ren, 100, 100))

            if board[i][j][0] == -1: continue
            WIN.blit(pieces[board[i][j][0]][board[i][j][1]],(x_ren+25,y_ren)) 

    start_pos = [[80,80],[990,80],[990,990],[80,990]]
    pygame.draw.lines(WIN, WHITE, True, start_pos, 2)








#ゲーム情報を盤面以外で補足するために表示
def draw_system_massege(player, first, promotion, castling, x, y):

    start_pos = [[80,1040],[80,1140],[990,1140],[990,1040]]
    pygame.draw.lines(WIN, WHITE, True, start_pos, 2)

    template = pygame.font.SysFont(None,50)

    if first == True:#起動後どこかをクリックするまで表示する
        template = pygame.font.SysFont(None,80)
        text = template.render("GAME START", True, WHITE)
        WIN.blit(text, (90,1065))

    elif promotion == True:#プロモーションが成立しているとき表示する

        draw_promotion_massege(x, y)

    elif castling != 0:#キャスリングが成立するとき表示する

        draw_castling_massege(castling)

    else:
        if player == 0:
            text = template.render("Black player's turn", True, WHITE)
            WIN.blit(text, (90,1050))
        if player == 1:
            text = template.render("White player's turn", True, WHITE)
            WIN.blit(text, (90,1050))


#ゲーム終了後の表示
def draw_ending_message(win):
    
    start_pos = [[80,1040],[80,1140],[990,1140],[990,1040]]
    pygame.draw.lines(WIN, WHITE, True, start_pos, 2)

    template = pygame.font.SysFont(None,80)
    if win == 0:
        text = template.render("Black player is WINNER!!", True, WHITE)
        WIN.blit(text, (90,1065))
    
    if win == 1:
        text = template.render("White player is WINNER!!", True, WHITE)
        WIN.blit(text, (90,1065))


#プロモーションの情報を表示
def draw_promotion_massege(x, y):

    template = pygame.font.SysFont(None,50)

    player_allowed_pro = board[y][x][0]

    if player_allowed_pro == 0:
        text = template.render("Black player may Promotion the pawn", True, WHITE)
        WIN.blit(text, (90,1050))

    if player_allowed_pro == 1:
        text = template.render("White player may Promotion the pawn", True, WHITE)
        WIN.blit(text, (90,1050))

    for i in range(4):
        x_ren = 88+116*i+10*i
        pygame.draw.rect(WIN, ORANGE, (x_ren, 1095, 116, 40))
    text = template.render(" Rook   Knight  Bishop Queen  <- select and click", True, WHITE)
    WIN.blit(text, (90,1095))


#キャスリングの情報を表示
def draw_castling_massege(castling):

    template = pygame.font.SysFont(None,50)
    
    if castling == 1:
        text = template.render("Black player may QueenSideCastling", True, WHITE)
        WIN.blit(text, (90,1050))
        pygame.draw.rect(WIN, ORANGE, (88, 1095, 190, 40))
        text = template.render("QueenSide             <- select and click", True, WHITE)
        WIN.blit(text, (90,1095))

    if castling == 2:
        text = template.render("Black player may KingSideCastling", True, WHITE)
        WIN.blit(text, (90,1050))
        pygame.draw.rect(WIN, ORANGE, (300, 1095, 163, 40))
        text = template.render("                       KingSide  <- select and click", True, WHITE)
        WIN.blit(text, (90,1095))

    if castling == 3:
        text = template.render("Black player may BothSidesCastling", True, WHITE)
        WIN.blit(text, (90,1050))
        pygame.draw.rect(WIN, ORANGE, (88, 1095, 190, 40))
        pygame.draw.rect(WIN, ORANGE, (300, 1095, 163, 40))
        text = template.render("QueenSide   KingSide  <- select and click", True, WHITE)
        WIN.blit(text, (90,1095))

    if castling == -1:
        text = template.render("White player may QueenSideCastling", True, WHITE)
        WIN.blit(text, (90,1050))
        pygame.draw.rect(WIN, ORANGE, (88, 1095, 190, 40))
        text = template.render("QueenSide             <- select and click", True, WHITE)
        WIN.blit(text, (90,1095))
    
    if castling == -2:
        text = template.render("White player may KingSideCastling", True, WHITE)
        WIN.blit(text, (90,1050))
        pygame.draw.rect(WIN, ORANGE, (300, 1095, 163, 40))
        text = template.render("                       KingSide  <- select and click", True, WHITE)
        WIN.blit(text, (90,1095))

    if castling == -3:
        text = template.render("White player may BothSidesCastling", True, WHITE)
        WIN.blit(text, (90,1050))
        pygame.draw.rect(WIN, ORANGE, (88, 1095, 190, 40))
        pygame.draw.rect(WIN, ORANGE, (300, 1095, 163, 40))
        text = template.render("QueenSide   KingSide  <- select and click", True, WHITE)
        WIN.blit(text, (90,1095))









#クリックされた座標が盤面上（８☓８）のどの領域にあるのか取得する
def get_position(x_raw, y_raw):
    print("get_position")

    for i in range(8):
        for j in range(8):
            x_ren = 100*(j+1)+10*j
            y_ren = 100*(i+1)+10*i
            if x_raw >= x_ren and x_ren+100 >= x_raw and y_raw >= y_ren and y_ren+100 >= y_raw:
                return j, i

    return -1, -1

#クリックされた座標が選択肢のどの領域にあるのか取得する
def get_choice_promotion(x_raw, y_raw):
    print("get_choice_promotion")

    for i in range(4):
        x_ren = 88+116*i+10*i
        if x_raw >= x_ren and x_ren+116 >= x_raw and y_raw >= 1095 and 1135 >= y_raw:
            return i+1

    return -1

#クリックされた座標が選択肢のどの領域にあるのか取得する
def get_choice_castling(x_raw, y_raw):
    print("get_choice_castling")

    if x_raw >= 88 and 88+190 >= x_raw and y_raw >= 1095 and 1135 >= y_raw:
        return 0
    
    if x_raw >= 300 and 300+163 >= x_raw and y_raw >= 1095 and 1135 >= y_raw:
        return 1

    return -1
    
#座標をもとに駒の種類を取得する
def get_type_piece(x, y):
    print("get_type_piece")

    type_piece = board[y][x][1]

    return type_piece


#引数が盤面内（配列外にアクセスしない）かを判断する
def judge_collision(x, y):
    print("judge_collision")
    
    if 0 <= x and x <= 7 and 0 <= y and y <= 7:
        return 0
    else:
        return 1


#どの駒が存在するか取得する
def get_existence(x, y):
    print("get_existence")

    if board[y][x][0] == 0:
        return 0
    elif board[y][x][0] == 1:
        return 1
    else:
        return -1


#select_boardをもとに選択された駒の可動範囲を判断する
def judge_movable_position(player, x, y):
    print("judge_movable_position")
    
    init_position()

    if board[y][x][0] == -1 or board[y][x][0] != player : return False
    
    if board[y][x][0] == player:
        select_position[y][x] = 1
        movable_position[y][x] = 2
        type_piece = get_type_piece(x, y)

        search_position(player, type_piece, x, y)

    return True



#選ばれている駒の可動範囲を検索する
def search_position(player, type_piece, x, y):
    print("seach_position")

    if type_piece == 0:
        search_pawn(player, x, y)   
    if type_piece == 1:
        search_rook(player, x, y)
    if type_piece == 2:
        search_knight(player, x, y)
    if type_piece == 3:
        search_bishop(player, x, y)
    if type_piece == 4:
        search_queen(player, x, y)
    if type_piece == 5:
        search_king(player, x, y)



#ポーンの移動範囲を検索する
def search_pawn(player, x_now, y_now):
    print("search_pawn")
    
    if player == 0:

        #初期位置のとき２マス進める
        if y_now == 1 and board[2][x_now][0] == -1 and board[3][x_now][0] == -1:
            movable_position[3][x_now] = 1
        
        #駒が存在しないとき1マス進める
        x_next = x_now
        y_next = y_now + 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == -1:
            movable_position[y_next][x_next] = 1
        
        #敵の駒があるとき進める
        x_next = x_now + 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == 1:
            movable_position[y_next][x_next] = 1

        #敵の駒があるとき進める
        x_next = x_now - 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == 1:
            movable_position[y_next][x_next] = 1
    
    else:
        #初期位置のとき２マス進める
        if y_now == 6 and board[5][x_now][0] == -1 and board[4][x_now][0] == -1:
            movable_position[4][x_now] = 1
        
        #駒が存在しないとき1マス進める
        x_next = x_now
        y_next = y_now - 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == -1:
            movable_position[y_next][x_next] = 1
        
        #敵の駒があるとき進める
        x_next = x_now + 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == 0:
            movable_position[y_next][x_next] = 1

        #敵の駒があるとき進める
        x_next = x_now - 1
        if judge_collision(x_next, y_next) == 0 and get_existence(x_next, y_next) == 0:
            movable_position[y_next][x_next] = 1



def judge_movable_black(x, y):

    if judge_collision(x, y) == 0 and get_existence(x, y) != 0:
        movable_position[y][x] = 1
        return get_existence(x, y) != 1
    
    return False

def judge_movable_white(x, y):

    if judge_collision(x, y) == 0 and get_existence(x, y) != 1:
        movable_position[y][x] = 1
        return get_existence(x, y) != 0
    
    return False



#ルークの移動範囲を検索する
def search_rook(player, x_now, y_now):
    
    if player == 0:

        for i in range(4):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next -= 1
                if i == 1: y_next += 1
                if i == 2: x_next += 1
                if i == 3: x_next -= 1
                OK = judge_movable_black(x_next, y_next)

    else:

        for i in range(4):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next -= 1
                if i == 1: y_next += 1
                if i == 2: x_next += 1
                if i == 3: x_next -= 1
                OK = judge_movable_white(x_next, y_next)


#ナイトの移動範囲を検索する
def search_knight(player, x_now, y_now):
    
    if player == 0:

        for i in range(4):
            for j in range(2):
                x_next = x_now
                y_next = y_now
                if i == 0 and j == 0: y_next, x_next = y_next+2, x_next+1
                if i == 0 and j == 1: y_next, x_next = y_next+1, x_next+2
                if i == 1 and j == 0: y_next, x_next = y_next+2, x_next-1
                if i == 1 and j == 1: y_next, x_next = y_next+1, x_next-2
                if i == 2 and j == 0: y_next, x_next = y_next-2, x_next-1
                if i == 2 and j == 1: y_next, x_next = y_next-1, x_next-2
                if i == 3 and j == 0: y_next, x_next = y_next-2, x_next+1
                if i == 3 and j == 1: y_next, x_next = y_next-1, x_next+2
                judge_movable_black(x_next, y_next)
    else:
        
        for i in range(4):
            for j in range(2):
                x_next = x_now
                y_next = y_now
                if i == 0 and j == 0: y_next, x_next = y_next+2, x_next+1
                if i == 0 and j == 1: y_next, x_next = y_next+1, x_next+2
                if i == 1 and j == 0: y_next, x_next = y_next+2, x_next-1
                if i == 1 and j == 1: y_next, x_next = y_next+1, x_next-2
                if i == 2 and j == 0: y_next, x_next = y_next-2, x_next-1
                if i == 2 and j == 1: y_next, x_next = y_next-1, x_next-2
                if i == 3 and j == 0: y_next, x_next = y_next-2, x_next+1
                if i == 3 and j == 1: y_next, x_next = y_next-1, x_next+2
                judge_movable_white(x_next, y_next)

#ビショップの移動範囲を検索する
def search_bishop(player, x_now, y_now):
    
    if player == 0:

        for i in range(4):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next, x_next = y_next+1, x_next+1
                if i == 1: y_next, x_next = y_next-1, x_next-1
                if i == 2: y_next, x_next = y_next+1, x_next-1
                if i == 3: y_next, x_next = y_next-1, x_next+1
                OK = judge_movable_black(x_next, y_next)
    
    else:

        for i in range(4):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next, x_next = y_next+1, x_next+1
                if i == 1: y_next, x_next = y_next-1, x_next-1
                if i == 2: y_next, x_next = y_next+1, x_next-1
                if i == 3: y_next, x_next = y_next-1, x_next+1
                OK = judge_movable_white(x_next, y_next)


#クイーンの移動範囲を検索する
def search_queen(player, x_now, y_now):
    
    if player == 0:

        for i in range(8):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next -= 1
                if i == 1: y_next += 1
                if i == 2: x_next += 1
                if i == 3: x_next -= 1
                if i == 4: y_next, x_next = y_next+1, x_next+1
                if i == 5: y_next, x_next = y_next-1, x_next-1
                if i == 6: y_next, x_next = y_next+1, x_next-1
                if i == 7: y_next, x_next = y_next-1, x_next+1
                OK = judge_movable_black(x_next, y_next)
    else:

        for i in range(8):
            x_next = x_now
            y_next = y_now
            OK = True
            while(OK):
                OK = False
                if i == 0: y_next -= 1
                if i == 1: y_next += 1
                if i == 2: x_next += 1
                if i == 3: x_next -= 1
                if i == 4: y_next, x_next = y_next+1, x_next+1
                if i == 5: y_next, x_next = y_next-1, x_next-1
                if i == 6: y_next, x_next = y_next+1, x_next-1
                if i == 7: y_next, x_next = y_next-1, x_next+1
                OK = judge_movable_white(x_next, y_next)


#キングの移動範囲を検索する
def search_king(player, x_now, y_now):

    if player == 0:

        for i in range(8):
            x_next = x_now
            y_next = y_now
            if i == 0: y_next -= 1
            if i == 1: y_next += 1
            if i == 2: x_next += 1
            if i == 3: x_next -= 1
            if i == 4: y_next, x_next = y_next+1, x_next+1
            if i == 5: y_next, x_next = y_next-1, x_next-1
            if i == 6: y_next, x_next = y_next+1, x_next-1
            if i == 7: y_next, x_next = y_next-1, x_next+1
            OK = judge_movable_black(x_next, y_next)
    else:
        for i in range(8):
            x_next = x_now
            y_next = y_now
            if i == 0: y_next -= 1
            if i == 1: y_next += 1
            if i == 2: x_next += 1
            if i == 3: x_next -= 1
            if i == 4: y_next, x_next = y_next+1, x_next+1
            if i == 5: y_next, x_next = y_next-1, x_next-1
            if i == 6: y_next, x_next = y_next+1, x_next-1
            if i == 7: y_next, x_next = y_next-1, x_next+1
            OK = judge_movable_white(x_next, y_next)



#select_positionをもとにクリックされた盤面上（８☓８）座標を取得する
def get_coordinate():
    print("get_coordinate")

    for i in range(8):
        for j in range(8):
            if select_position[i][j] == 1:
                x_coordinate = j
                y_coordinate = i
    
    return (x_coordinate, y_coordinate)



def move(player, x, y):
    print("move")

    global B_KING_MOVED
    global B_QUEENSIDE_ROOK_MOVED
    global B_KINGSIDE_ROOK_MOVED
    global W_KING_MOVED
    global W_QUEENSIDE_ROOK_MOVED
    global W_KINGSIDE_ROOK_MOVED

    if movable_position[y][x] == -1 or movable_position[y][x] == 2:#空白か同じ座標の場合
        return player

    x_old, y_old = get_coordinate()

    if y_old == 0 and x_old == 4:
        B_KING_MOVED = True
    if y_old == 0 and x_old == 0:
        B_QUEENSIDE_ROOK_MOVED = True
    if y_old == 0 and x_old == 7:
        B_KINGSIDE_ROOK_MOVED = True
    if y_old == 7 and x_old == 4:
        W_KING_MOVED = True
    if y_old == 7 and x_old == 0:
        W_QUEENSIDE_ROOK_MOVED = True
    if y_old == 7 and x_old == 7:
        W_KINGSIDE_ROOK_MOVED = True
        

    board[y][x][0] = board[y_old][x_old][0]
    board[y][x][1] = board[y_old][x_old][1]

    board[y_old][x_old][0] = -1

    return (player+1)%2



def judge_promotion():

    y = 0
    for x in range(8):
        if board[y][x][1] == 0 and board[y][x][0] == 1:
            return True
    
    y = 7
    for x in range(8):
        if board[y][x][1] == 0 and board[y][x][0] == 0:
            return True
    
    return False


def do_promotion(selected_piece, x, y):
    print("do_promotion")
    board[y][x][1] = selected_piece

    return False


def judge_castling(player, x, y):
    print("judge_castling")
    b_queenside = 0
    b_kingside = 0
    w_queenside = 0
    w_kingside = 0

    if player == 0:
        if board[y][x][1] == 5 and player == board[y][x][0]:
            if B_KING_MOVED == False and B_QUEENSIDE_ROOK_MOVED == False and board[y][x-1][0] == -1 and board[y][x-2][0] == -1 and board[y][x-3][0] == -1:
                b_queenside = 1
            if B_KING_MOVED == False and B_KINGSIDE_ROOK_MOVED == False and board[y][x+1][0] == -1 and board[y][x+2][0] == -1:
                b_kingside = 1
    if player == 1:
        if board[y][x][1] == 5 and player == board[y][x][0]:
            if W_KING_MOVED == False and W_QUEENSIDE_ROOK_MOVED == False and board[y][x-1][0] == -1 and board[y][x-2][0] == -1 and board[y][x-3][0] == -1:
                w_queenside = 1
            if W_KING_MOVED == False and W_KINGSIDE_ROOK_MOVED == False and board[y][x+1][0] == -1 and board[y][x+2][0] == -1:
                w_kingside = 1
    
    if b_queenside == 1 and b_kingside == 1:
        return 3
    if b_kingside == 1:
        return 2
    if b_queenside == 1:
        return 1
    if w_queenside == 1 and w_kingside == 1:
        return -3
    if w_kingside == 1:
        return -2
    if w_queenside == 1:
        return -1

    return 0

def do_castling(selected_castling, player, x, y):
    print("do_castling")

    global B_KING_MOVED
    global W_KING_MOVED

    init_position()

    if board[y][x][0] == 0:
        B_KING_MOVED = True
    else:
        W_KING_MOVED = True

    if selected_castling == 0:
        board[y][x-2][1] = board[y][x][1]
        board[y][x-2][0] = board[y][x][0]
        board[y][x-1][1] = board[y][x-4][1]
        board[y][x-1][0] = board[y][x-4][0]

        board[y][x][0], board[y][x-4][0] = -1, -1

    if selected_castling == 1:
        board[y][x+2][1] = board[y][x][1]
        board[y][x+2][0] = board[y][x][0]
        board[y][x+1][1] = board[y][x+3][1]
        board[y][x+1][0] = board[y][x+3][0]

        board[y][x][0], board[y][x+3][0] = -1, -1

    return (player+1)%2, False


    
def judge_game():

    b_win = False
    w_win = False

    for i in range(8):
        for j in range(8):
            if board[i][j][1] == 5 and board[i][j][0] == 0:
                b_win = True
            if board[i][j][1] == 5 and board[i][j][0] == 1:
                w_win = True
    
    if b_win == True and w_win == True:
        return True, -1
    elif b_win == False:
        return False, 1
    else:
        return False, 0


#配列の初期化
def init_position():
    for i in range(8):
            for j in range(8):
                movable_position[i][j] = -1
                select_position[i][j] = -1

#盤面情報の初期化
def init_board():
    print("init_board")

    board[0][0] = [0,1]
    board[0][1] = [0,2]
    board[0][2] = [0,3]
    board[0][3] = [0,4]
    board[0][4] = [0,5]
    board[0][5] = [0,3]
    board[0][6] = [0,2]
    board[0][7] = [0,1]

    for x in range(8):
        board[1][x] = [0,0]

    board[7][0] = [1,1]
    board[7][1] = [1,2]
    board[7][2] = [1,3]
    board[7][3] = [1,4]
    board[7][4] = [1,5]
    board[7][5] = [1,3]
    board[7][6] = [1,2]
    board[7][7] = [1,1]
    
    for x in range(8):
        board[6][x] = [1,0]


def main():
    run = True
    first = True
    ending = False
    select = False
    promotion = False
    castling = 0
    win = -1
    player = 0
    x, y = 0, 0
    init_board()

    while run:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                if select == True: select = False 

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                first = False
                x_raw, y_raw = event.pos

                if castling != 0:
                    selected_castling = get_choice_castling(x_raw, y_raw)
                    castling = 0
                    if selected_castling != -1:
                        player, select= do_castling(selected_castling, player, x, y)

                if promotion == True:
                    selected_piece = get_choice_promotion(x_raw,y_raw)
                    if selected_piece == -1:continue
                    promotion = do_promotion(selected_piece, x, y)
                else: 
                    x, y = get_position(x_raw,y_raw)
                    if x == -1:continue

                    if not select:
                        select = judge_movable_position(player, x, y)
                        castling = judge_castling(player, x, y)
                    else:
                        player = move(player, x, y)
                        select = False
                        run, win= judge_game()
                        promotion = judge_promotion()
                        if run == False: ending = True
                        init_position()
                    
        draw_board()
        draw_system_massege(player, first, promotion, castling, x, y)
        pygame.display.update()


    while ending:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = False
        draw_board()
        draw_ending_message(win)
        pygame.display.update()


if __name__ == '__main__':
    main()