import pygame
import sys
import ustawienia

#Algorytm sprawdzajacy wygrana
def check_winner(board, size, win_length):
    for r in range(size):
        for c in range(size):
            symbol = board[r][c]
            if symbol is None:
                continue
            
            # Sprawdzanie w poziomie
            if c + win_length <= size:
                if all(board[r][c + i] == symbol for i in range(win_length)):
                    return symbol
            
            # Sprawdzanie w pionie w dół
            if r + win_length <= size:
                if all(board[r + i][c] == symbol for i in range(win_length)):
                    return symbol
            
            # Sprawdzanie po przekątnej w dół i w prawo
            if r + win_length <= size and c + win_length <= size:
                if all(board[r + i][c + i] == symbol for i in range(win_length)):
                    return symbol
            
            # Sprawdzanie po przekątnej w dół i w lewo
            if r + win_length <= size and c - win_length >= -1:
                if all(board[r + i][c - i] == symbol for i in range(win_length)):
                    return symbol
                    
    return None

def is_board_full(board):
    #Zwraca True, jeśli na planszy nie ma już wolnych miejsc.
    for row in board:
        if None in row:
            return False
    return True






def run_game_loop(screen, size, difficulty="Łatwy"):
    clock = pygame.time.Clock()
    
    #Warunek wygranej: dla plansz 3x3 oraz 4x4 szukamy 3 znaków. Dla 5x5 szukamy 4 znaków.
    win_length = 4 if size == 5 else 3
    
    #Inicjalizacja pustej planszy
    board = [[None for _ in range(size)] for _ in range(size)]
    current_player = "X"  # Gracz ludzki to zawsze "X", komputer to "O"
    winner = None
    game_over = False

    #Parametry rysowania siatki
    BOARD_DISPLAY_SIZE = 400
    START_X = (ustawienia.OKNO_SZEROKOSC - BOARD_DISPLAY_SIZE) // 2
    START_Y = (ustawienia.OKNO_WYSOKOSC - BOARD_DISPLAY_SIZE) // 2
    CELL_SIZE = BOARD_DISPLAY_SIZE // size

    font_ui = pygame.font.SysFont("Arial", 28, bold=True)
    font_symbols = pygame.font.SysFont("Arial", int(CELL_SIZE * 0.6), bold=True)
    
    #Przycisk powrotu do menu głównego po zakończeniu gry
    btn_back = pygame.Rect(250, 530, 300, 45)

    #Wgrywanie i skalowanie plików z grafikami
    target_img_size = int(CELL_SIZE * 0.8)
    
    #Ładowanie grafik z obsługą przezroczystości (.convert_alpha())
    x_image_raw = pygame.image.load("x_skin.png").convert_alpha()
    o_image_raw = pygame.image.load("o_skin.png").convert_alpha()
    
    #Skalowanie obrazków do rozmiaru dopasowanego do wybranej planszy (3x3, 4x4 lub 5x5)
    x_image = pygame.transform.smoothscale(x_image_raw, (target_img_size, target_img_size))
    o_image = pygame.transform.smoothscale(o_image_raw, (target_img_size, target_img_size))

    #GŁÓWNA PĘTLA MECZU
