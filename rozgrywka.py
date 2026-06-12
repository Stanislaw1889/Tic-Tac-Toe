import pygame
import sys
import ustawienia
import random  # Tymczasowo używane do prostego ruchu bota

# Algorytm sprawdzajacy wygrana
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
    # Zwraca True, jeśli na planszy nie ma już wolnych miejsc.
    for row in board:
        if None in row:
            return False
    return True


def temporary_mock_bot(board, size):
    # Tymczasowa logika bota
    empty_cells = []
    for r in range(size):
        for c in range(size):
            if board[r][c] is None:
                empty_cells.append((r, c))
    if empty_cells:
        return random.choice(empty_cells)
    return None


def run_game_loop(screen, size, difficulty="Łatwy", is_timed=False):
    clock = pygame.time.Clock()
    
    # Warunek wygranej: dla plansz 3x3 oraz 4x4 szukamy 3 znaków. Dla 5x5 szukamy 4 znaków.
    win_length = 4 if size == 5 else 3
    
    # Inicjalizacja pustej planszy
    board = [[None for _ in range(size)] for _ in range(size)]
    
    # =========================================================================
    # KROK 1: Inicjalizacja listy historii ruchów i przycisków
    # =========================================================================
    move_history = []  # Przechowuje krotki (wiersz, kolumna) kolejnych ruchów
    
    # Przycisk "Cofnij" na środku ekranu, gdy rozgrywka wciąż trwa
    btn_undo_centered = pygame.Rect(250, 530, 300, 45)
    
    # Po zakończeniu gry chcemy pokazać dwa przyciski obok siebie
    btn_undo_gameover = pygame.Rect(200, 530, 190, 45)  # Lewy przycisk
    btn_back_gameover = pygame.Rect(410, 530, 190, 45)  # Prawy przycisk
    
    current_player = "X"  # Gracz ludzki to zawsze "X", komputer to "O"
    winner = None
    game_over = False

    # Zmienne obsługujące licznik czasu
    turn_start_time = None
    LIMIT_CZASU = 5.0  # limit w sekundach

    # Parametry rysowania siatki
    BOARD_DISPLAY_SIZE = 400
    START_X = (ustawienia.OKNO_SZEROKOSC - BOARD_DISPLAY_SIZE) // 2
    START_Y = (ustawienia.OKNO_WYSOKOSC - BOARD_DISPLAY_SIZE) // 2
    CELL_SIZE = BOARD_DISPLAY_SIZE // size

    font_ui = pygame.font.SysFont("Arial", 28, bold=True)
    font_timer = pygame.font.SysFont("Arial", 24, bold=True) # Dodana brakująca czcionka timera
    
    # Wgrywanie i skalowanie plików z grafikami
    target_img_size = int(CELL_SIZE * 0.8)
    
    # ZMIANA: Dynamiczne ładowanie grafik z pliku ustawienia.py
    x_image_raw = pygame.image.load(ustawienia.AKTUALNY_SKIN_X).convert_alpha()
    o_image_raw = pygame.image.load(ustawienia.AKTUALNY_SKIN_O).convert_alpha()
    
    # Skalowanie obrazków do rozmiaru dopasowanego do wybranej planszy (3x3, 4x4 lub 5x5)
    x_image = pygame.transform.smoothscale(x_image_raw, (target_img_size, target_img_size))
    o_image = pygame.transform.smoothscale(o_image_raw, (target_img_size, target_img_size))

    # GŁÓWNA PĘTLA MECZU
    while True:
        screen.fill(ustawienia.CZERN_TLA)
        mouse_pos = pygame.mouse.get_pos()

        # Rysowanie tekstów interfejsu
        title_text = f"Plansza {size}x{size} (Wymagane do wygranej: {win_length})"
        title_surf = font_ui.render(title_text, True, ustawienia.BIEL)
        screen.blit(title_surf, (ustawienia.OKNO_SZEROKOSC // 2 - title_surf.get_width() // 2, 20))

        # =========================================================================
        # KROK 2: Dynamiczne rysowanie przycisków w zależności od stanu gry
        # =========================================================================
        # logika timera
        time_left = LIMIT_CZASU
        if not game_over and is_timed and current_player == "X":
            if turn_start_time is None:
                turn_start_time = pygame.time.get_ticks()
            
            # Obliczanie upływu czasu w sekundach
            elapsed = (pygame.time.get_ticks() - turn_start_time) / 1000.0
            time_left = LIMIT_CZASU - elapsed
            
            if time_left <= 0:
                time_left = 0
                game_over = True
                winner = "O"  # Gracz przekroczył czas -> Komputer wygrywa automatycznie

        if not game_over:
            status_text = "Twój ruch (X)" if current_player == "X" else "Ruch komputera (O)..."
            status_color = ustawienia.ZIELEN if current_player == "X" else list(ustawienia.SZARY_TEKST)
            status_surf = font_ui.render(status_text, True, status_color)
            screen.blit(status_surf, (ustawienia.OKNO_SZEROKOSC // 2 - status_surf.get_width() // 2, 70))

            # Wyświetlanie zegara odliczającego czas
            if is_timed and current_player == "X":
                timer_text = f"Czas: {time_left:.1f}s"
                # Zegar zmienia kolor na czerwony, gdy zostanie mniej niż 2 sekundy
                timer_color = ustawienia.CZERWIEN if time_left < 2.0 else (240, 200, 40)
                timer_surf = font_timer.render(timer_text, True, timer_color)
                screen.blit(timer_surf, (ustawienia.OKNO_SZEROKOSC // 2 - timer_surf.get_width() // 2, 100))
                
            # Rysowanie wyśrodkowanego przycisku "Cofnij ruch" w trakcie gry
            kolor_undo = ustawienia.daj_kolor_przycisku(btn_undo_centered, mouse_pos)
            pygame.draw.rect(screen, kolor_undo, btn_undo_centered, ustawienia.GRUBOŚĆ_RAMKI)
            undo_surf = font_ui.render("Cofnij ruch", True, kolor_undo)
            screen.blit(undo_surf, (btn_undo_centered.centerx - undo_surf.get_width() // 2, btn_undo_centered.centery - undo_surf.get_height() // 2))
        else:
            if winner:
                end_text = "WYGRAŁEŚ!" if winner == "X" else "PRZEGRAŁEŚ! Komputer wygrał."
                end_color = ustawienia.ZIELEN if winner == "X" else ustawienia.CZERWIEN
            else:
                end_text = "REMIS!"
                end_color = ustawienia.SZARY_TEKST
            
            end_surf = font_ui.render(end_text, True, end_color)
            screen.blit(end_surf, (ustawienia.OKNO_SZEROKOSC // 2 - end_surf.get_width() // 2, 65))
            
            # KIEDY KONIEC GRY: Rysujemy dwa przyciski obok siebie
            # 1. Przycisk ponownej szansy / cofnięcia błędu (po lewej)
            kolor_undo = ustawienia.daj_kolor_przycisku(btn_undo_gameover, mouse_pos)
            pygame.draw.rect(screen, kolor_undo, btn_undo_gameover, ustawienia.GRUBOŚĆ_RAMKI)
            undo_surf = font_ui.render("Cofnij błąd", True, kolor_undo)
            screen.blit(undo_surf, (btn_undo_gameover.centerx - undo_surf.get_width() // 2, btn_undo_gameover.centery - undo_surf.get_height() // 2))

            # 2. Przycisk powrotu do menu głównego (po prawej)
            kolor_powrotu = ustawienia.daj_kolor_przycisku(btn_back_gameover, mouse_pos)
            pygame.draw.rect(screen, kolor_powrotu, btn_back_gameover, ustawienia.GRUBOŚĆ_RAMKI)
            back_surf = font_ui.render("Powrót do menu", True, kolor_powrotu)
            screen.blit(back_surf, (btn_back_gameover.centerx - back_surf.get_width() // 2, btn_back_gameover.centery - back_surf.get_height() // 2))

        # Rysowanie siatki planszy gry
        for i in range(1, size):
            pygame.draw.line(screen, ustawienia.ZIELEN, (START_X + i * CELL_SIZE, START_Y), (START_X + i * CELL_SIZE, START_Y + BOARD_DISPLAY_SIZE), 3)
            pygame.draw.line(screen, ustawienia.ZIELEN, (START_X, START_Y + i * CELL_SIZE), (START_X + BOARD_DISPLAY_SIZE, START_Y + i * CELL_SIZE), 3)
        
        # Ramka zewnętrzna wokół planszy
        pygame.draw.rect(screen, ustawienia.ZIELEN, (START_X, START_Y, BOARD_DISPLAY_SIZE, BOARD_DISPLAY_SIZE), 4)

        # Rysowanie skinów
        for r in range(size):
            for c in range(size):
                if board[r][c] is not None:
                    img_to_draw = x_image if board[r][c] == "X" else o_image
                    sym_x = START_X + c * CELL_SIZE + (CELL_SIZE // 2) - (img_to_draw.get_width() // 2)
                    sym_y = START_Y + r * CELL_SIZE + (CELL_SIZE // 2) - (img_to_draw.get_height() // 2)
                    screen.blit(img_to_draw, (sym_x, sym_y))

        # Logika ruchu bota
        if not game_over and current_player == "O":
            pygame.time.wait(400)  # Krótkie opóźnienie (0.4s)
            bot_move = temporary_mock_bot(board, size)
            
            if bot_move:
                r_bota, c_bota = bot_move
                board[r_bota][c_bota] = "O"
                
                # =========================================================================
                # KROK 3: Zapisanie ruchu bota w historii ruchów
                # =========================================================================
                move_history.append((r_bota, c_bota))
                
                winner = check_winner(board, size, win_length)
                if winner or is_board_full(board):
                    game_over = True
                else:
                    current_player = "X"
                    turn_start_time = None  # Reset czasu dla gracza przed jego ruchem

        # Obsługa myszy i okna
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 1. Obsługa powrotu do menu głównego po zakończeniu meczu
                if game_over and btn_back_gameover.collidepoint(mouse_pos):
                    return

                # =========================================================================
                # KROK 4: Obsługa kliknięcia przycisków cofania
                # =========================================================================
                click_undo_running = (not game_over and current_player == "X" and btn_undo_centered.collidepoint(mouse_pos))
                click_undo_gameover = (game_over and btn_undo_gameover.collidepoint(mouse_pos))

                if click_undo_running or click_undo_gameover:
                    if len(move_history) >= 2:
                        # Usunięcie ruchu bota
                        r_b, c_b = move_history.pop()
                        board[r_b][c_b] = None

                        # Usunięcie Twojego ruchu
                        r_p, c_p = move_history.pop()
                        board[r_p][c_p] = None

                        # Resetowanie flag końca gry i przywrócenie tury gracza
                        game_over = False
                        winner = None
                        current_player = "X"
                        turn_start_time = None  # Reset timera po cofnięciu ruchu
                        continue

                # Obsługa normalnego ruchu gracza
                if not game_over and current_player == "X":
                    x_click, y_click = mouse_pos
                    if START_X <= x_click < START_X + BOARD_DISPLAY_SIZE and START_Y <= y_click < START_Y + BOARD_DISPLAY_SIZE:
                        c = (x_click - START_X) // CELL_SIZE
                        r = (y_click - START_Y) // CELL_SIZE

                        if board[r][c] is None:
                            board[r][c] = "X"
                            
                            # Zapisujemy Twój ruch do historii
                            move_history.append((r, c))
                            
                            winner = check_winner(board, size, win_length)
                            if winner or is_board_full(board):
                                game_over = True
                            else:
                                current_player = "O"

        pygame.display.flip()
        clock.tick(60)
