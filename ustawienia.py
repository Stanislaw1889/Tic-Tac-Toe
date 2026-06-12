#WYMIARY OKNA GRY
OKNO_SZEROKOSC = 800
OKNO_WYSOKOSC = 600

# GLOWNE KOLORY MENU

CZERN_TLA = (15, 15, 18) # tlo menu
ZIELEN = (20, 160, 90)    # kolor ramek do przyciskow i tekstow w tych przyciskach
CZERWIEN = (220, 40, 60)  # kolor aktywnego elementu (gdy najedziemy na niego myszka)
BIEL = (255, 255, 255)   # Np. do tytulow
SZARY_TEKST = (100, 100, 100)  # Do mniej ważnych

# --- PARAMETRY INTERFEJSU ---
GRUBOŚĆ_RAMKI = 2       # Standardowa grubość obwódki przycisków
ODSTĘP_PRZYCISKÓW = 20  # Odstep pionowy miedzy przyciskami ktory zachowuje w menu glownym
                        # Jesli uznacie ze bedzie Wam pasowal inny odstep to nie trzymajcie sie tej wartosci

def daj_kolor_przycisku(przycisk_rect, pozycja_myszki):
    if przycisk_rect.collidepoint(pozycja_myszki):
        return CZERWIEN
    else:
        return ZIELEN
      

#Funkcja sprawdza czy kursor jest na przycisku, jeśli tak to czerwony, nie to zielony

# Wgrywanie i skalowanie plików z grafikami
    target_img_size = int(CELL_SIZE * 0.8)
    
    # Ładowanie grafik z obsługą przezroczystości (.convert_alpha())
    x_image_raw = pygame.image.load("x_skin.png").convert_alpha()
    o_image_raw = pygame.image.load("o_skin.png").convert_alpha()
