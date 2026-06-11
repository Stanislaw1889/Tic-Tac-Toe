import pygame
import sys
import ustawienia
import random  #Tymczasowo używane do prostego ruchu bota

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


def temporary_mock_bot(board, size):
    #Tymczasowa logika bota
    empty_cells = []
    for r in range(size):
        for c in range(size):
            if board[r][c] is None:
                empty_cells.append((r, c))
    if empty_cells:
        return random.choice(empty_cells)
    return None


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
    while True:
        screen.fill(ustawienia.CZERN_TLA)
        mouse_pos = pygame.mouse.get_pos()

        #Rysowanie tekstów interfejsu
        title_text = f"Plansza {size}x{size} (Wymagane do wygranej: {win_length})"
        title_surf = font_ui.render(title_text, True, ustawienia.BIEL)
        screen.blit(title_surf, (ustawienia.OKNO_SZEROKOSC // 2 - title_surf.get_width() // 2, 20))

        if not game_over:
            status_text = "Twój ruch (X)" if current_player == "X" else "Ruch komputera (O)..."
            status_color = ustawienia.ZIELEN if current_player == "X" else list(ustawienia.SZARY_TEKST)
            status_surf = font_ui.render(status_text, True, status_color)
            screen.blit(status_surf, (ustawienia.OKNO_SZEROKOSC // 2 - status_surf.get_width() // 2, 70))
        else:
            if winner:
                end_text = "WYGRAŁEŚ!" if winner == "X" else "PRZEGRAŁEŚ! Komputer wygrał."
                end_color = ustawienia.ZIELEN if winner == "X" else ustawienia.CZERWIEN
            else:
                end_text = "REMIS!"
                end_color = ustawienia.SZARY_TEKST
            
            end_surf = font_ui.render(end_text, True, end_color)
            screen.blit(end_surf, (ustawienia.OKNO_SZEROKOSC // 2 - end_surf.get_width() // 2, 65))
            
            #Rysowanie przycisku "Powrót"
            kolor_powrotu = ustawienia.daj_kolor_przycisku(btn_back, mouse_pos)
            pygame.draw.rect(screen, kolor_powrotu, btn_back, ustawienia.GRUBOŚĆ_RAMKI)
            back_surf = font_ui.render("Powrót do menu", True, kolor_powrotu)
            screen.blit(back_surf, (btn_back.centerx - back_surf.get_width() // 2, btn_back.centery - back_surf.get_height() // 2))

        #Rysowanie siatki planszy gry
        for i in range(1, size):
            pygame.draw.line(screen, ustawienia.ZIELEN, (START_X + i * CELL_SIZE, START_Y), (START_X + i * CELL_SIZE, START_Y + BOARD_DISPLAY_SIZE), 3)
            pygame.draw.line(screen, ustawienia.ZIELEN, (START_X, START_Y + i * CELL_SIZE), (START_X + BOARD_DISPLAY_SIZE, START_Y + i * CELL_SIZE), 3)
        
        # Ramka zewnętrzna wokół planszy
        pygame.draw.rect(screen, ustawienia.ZIELEN, (START_X, START_Y, BOARD_DISPLAY_SIZE, BOARD_DISPLAY_SIZE), 4)

        #Rysowanie skinów
        for r in range(size):
            for c in range(size):
                if board[r][c] is not None:
                    # Wybór odpowiedniego obrazka zależnie od zawartości komórki
                    img_to_draw = x_image if board[r][c] == "X" else o_image
                    
                    # Środkowanie obrazka wewnątrz komórki siatki
                    sym_x = START_X + c * CELL_SIZE + (CELL_SIZE // 2) - (img_to_draw.get_width() // 2)
                    sym_y = START_Y + r * CELL_SIZE + (CELL_SIZE // 2) - (img_to_draw.get_height() // 2)
                    screen.blit(img_to_draw, (sym_x, sym_y))

        #Logika ruchu bota
        if not game_over and current_player == "O":
            pygame.time.wait(400)  #Krótkie opóźnienie (0.4s), aby ruch komputera wyglądał naturalnie
            
            #Tu wpięta będzie właściwa funkcja bota
            #Na ten moment używamy tymczasowego losowego bota:

            bot_move = temporary_mock_bot(board, size)
            
            if bot_move:
                r_bota, c_bota = bot_move
                board[r_bota][c_bota] = "O"
                
                #Sprawdzenie stanów końca gry po ruchu bota
                winner = check_winner(board, size, win_length)
                if winner or is_board_full(board):
                    game_over = True
                else:
                    current_player = "X"  #Powrót do tury gracza ludzkiego

        #Obsługa myszy i okna
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #Jeśli mecz się zakończył i kliknięto przycisk powrotu
                if game_over and btn_back.collidepoint(mouse_pos):
                    return  #Wyjście z pętli gry (powrót do głównego menu)

                #Obsługa ruchu gracza
                if not game_over and current_player == "X":
                    x_click, y_click = mouse_pos
                    #Sprawdzenie czy kliknięcie nastąpiło wewnątrz siatki gry
                    if START_X <= x_click < START_X + BOARD_DISPLAY_SIZE and START_Y <= y_click < START_Y + BOARD_DISPLAY_SIZE:
                        c = (x_click - START_X) // CELL_SIZE
                        r = (y_click - START_Y) // CELL_SIZE

                        #Jeśli wybrane pole jest puste, wykonaj ruch
                        if board[r][c] is None:
                            board[r][c] = "X"
                            
                            #Sprawdzenie stanów końca gry po ruchu gracza
                            winner = check_winner(board, size, win_length)
                            if winner or is_board_full(board):
                                game_over = True
                            else:
                                current_player = "O"  #Przekazanie tury komputerowi

        pygame.display.flip()
        clock.tick(60)