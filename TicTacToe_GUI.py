import pygame
import random
pygame.init()

WIDTH, HEIGHT = 300, 370
BLOCKSIZE = 100
STATUS_RECT = pygame.Rect(0, 300, 300, 70)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (127, 255, 212)
RED = (255, 0, 0)
VALUE_FONT = pygame.font.SysFont('comicsans', 80)
WELCOME_FONT = pygame.font.SysFont('comicsans', 30)
WINNER_FONT = pygame.font.SysFont('comicsans', 80)
DRAW_FONT = pygame.font.SysFont('comicsans', 50)
global clicked
clicked = None

global board
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

def draw_board(turn):
    WIN.fill(BLUE)
    pygame.draw.rect(WIN, BLACK, STATUS_RECT)
    pygame.display.set_caption("TIC TAC TOE")
    for i in range(1,3):
        pygame.draw.line(WIN, BLACK, (0, BLOCKSIZE * i), (WIDTH, BLOCKSIZE * i), 4)
        pygame.draw.line(WIN, BLACK, (BLOCKSIZE * i, 0), (BLOCKSIZE * i, HEIGHT-70), 4)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '':
                text = VALUE_FONT.render(str(board[i][j]), 1, BLACK)
                WIN.blit(text, (BLOCKSIZE * i + BLOCKSIZE // 2 - text.get_width() // 2,
                                BLOCKSIZE * j + BLOCKSIZE // 2 - text.get_height() // 2))
    print_player(turn)
    pygame.display.update()

def player_choice():
    choice = None
    while not choice:
        WIN.fill(BLUE)
        text = WELCOME_FONT.render('Player 1 Choose: X or O', 1, BLACK)
        WIN.blit(text, (BLOCKSIZE * 1 + BLOCKSIZE // 2 - text.get_width() // 2,
                        BLOCKSIZE * 1 + BLOCKSIZE // 2 - text.get_height() // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    choice = ('X', 'O')
                if event.key == pygame.K_o:
                    choice = ('O', 'X')
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
    return choice

def click(pos):
    if pos[0] < WIDTH and pos[1] < HEIGHT - 70:
        x = pos[0] // BLOCKSIZE
        y = pos[1] // BLOCKSIZE
        return (int(x), int(y))
    return None

def check_result(mark):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == mark != '':
            x1, y1, x2, y2 = BLOCKSIZE * row + BLOCKSIZE//2, row, BLOCKSIZE * row + BLOCKSIZE//2, HEIGHT - 70
            return mark, x1, y1, x2, y2
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark != '':
            x1, y1, x2, y2 = col, BLOCKSIZE * col + BLOCKSIZE // 2, WIDTH, BLOCKSIZE * col + BLOCKSIZE // 2
            return mark, x1, y1, x2, y2
    if board[0][0] == board[1][1] == board[2][2] == mark != '':
        x1, y1, x2, y2 = 0, 0, 300, 300
        return mark, x1, y1, x2, y2
    if board[0][2] == board[1][1] == board[2][0] == mark != []:
        x1, y1, x2, y2 = 0, 300, 300, 0
        return mark, x1, y1, x2, y2
    return None, None, None, None, None

def winner(mark, x1, y1, x2, y2):
    pygame.draw.rect(WIN, BLACK, STATUS_RECT)
    text = WINNER_FONT.render(str(mark) + ' WINS!', 1, WHITE)
    WIN.blit(text, (WIDTH//2 - text.get_width()//2, 335 - text.get_height()//2))
    pygame.draw.line(WIN, RED, (x1, y1), (x2, y2), 10)
    pygame.display.update()
    pygame.time.delay(5000)

def get_input(player, choice):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            global clicked
            clicked = click(pos)
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if clicked:
            if player == 'Player1':
                if board[clicked[0]][clicked[1]] == '':
                    board[clicked[0]][clicked[1]] = choice[0]
                    clicked = None
                    return True
                else:
                    continue
            else:
                if board[clicked[0]][clicked[1]] == '':
                    board[clicked[0]][clicked[1]] = choice[1]
                    clicked = None
                    return True
                else:
                    continue
    return False

def print_player(player):
    text = WELCOME_FONT.render(str(player) + "'s Turn", 1, WHITE)
    WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 335 - text.get_height() // 2))
    pygame.display.update()

def check_empty():
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '':
                return True
    return False

def draw():
    pygame.draw.rect(WIN, BLACK, STATUS_RECT)
    text = DRAW_FONT.render("IT'S A DRAW!", 1, WHITE)
    WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 335 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)

def play_again():
    choice = None
    while not choice:
        WIN.fill(BLUE)
        text = WELCOME_FONT.render('Do you want to play again?', 1, BLACK)
        WIN.blit(text, (BLOCKSIZE * 1 + BLOCKSIZE // 2 - text.get_width() // 2,
                        BLOCKSIZE * 1 + BLOCKSIZE // 2 - text.get_height() // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    choice = True
                    global board
                    board = [['', '', ''],
                             ['', '', ''],
                             ['', '', '']]
                    main()
                if event.key == pygame.K_n:
                    run = False
                    game_on = False
                    pygame.quit()
                    choice = False
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
    return choice

def game(player, choice, player_choice):
    while not get_input(player, choice):
        draw_board(player)
        mark, x1, y1, x2, y2 = check_result(player_choice)
        if mark:
            winner(mark, x1, y1, x2, y2)
            play_again()
            break
        if not check_empty():
            draw()
            play_again()
            break

def main():
    run = True
    choice = None
    turn = 'Player 1'
    row, col, key = None, None, None
    mark = None
    game_on = True

    while run:
        while not choice:
            choice = player_choice()
        draw_board(turn)

        while game_on:
            if turn == 'Player 1':
                game('Player1', choice, choice[1])
                turn = 'Player 2'
            else:
                game('Player2', choice, choice[0])
                turn = 'Player 1'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
main()
