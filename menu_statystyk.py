import pygame
import sys
import ustawienia
import ranking1


def run_stats_menu(screen):
    clock = pygame.time.Clock()
    czcionka_tytulu = pygame.font.SysFont("Arial", 36, bold=True)
    czcionka_zakladek = pygame.font.SysFont("Arial", 22, bold=True)
    czcionka_danych = pygame.font.SysFont("Arial", 26, bold=True)

    aktywny_poziom = "Łatwy"  # Domyślnie wybrana zakładka

    # Pozycje trzech zakładek (przycisków) obok siebie
    zakladki = {
        "Łatwy": pygame.Rect(150, 140, 150, 45),
        "Średni": pygame.Rect(325, 140, 150, 45),
        "Trudny": pygame.Rect(500, 140, 150, 45)
    }

    btn_powrot = pygame.Rect(250, 490, 300, 45)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(ustawienia.CZERN_TLA)

        # Tytuł okna
        tytul_surf = czcionka_tytulu.render("STATYSTYKI PROFILU", True, ustawienia.BIEL)
        screen.blit(tytul_surf, (ustawienia.OKNO_SZEROKOSC // 2 - tytul_surf.get_width() // 2, 45))

        # Pobieramy świeże statystyki z pliku JSON
        ranking = ranking1.wczytaj_ranking()

        # Rysowanie 3 zakładek poziomów trudności
        for poziom, rect in zakladki.items():
            if poziom == aktywny_poziom:
                kolor = ustawienia.CZERWIEN  # Aktywna zakładka podświetla się na czerwono
            else:
                kolor = ustawienia.daj_kolor_przycisku(rect, mouse_pos)

            pygame.draw.rect(screen, kolor, rect, ustawienia.GRUBOŚĆ_RAMKI)
            txt = czcionka_zakladek.render(poziom, True, kolor)
            screen.blit(txt, (rect.centerx - txt.get_width() // 2, rect.centery - txt.get_height() // 2))

        # Duża główna ramka na dane statystyczne
        ramka_dane = pygame.Rect(150, 210, 500, 240)
        pygame.draw.rect(screen, ustawienia.ZIELEN, ramka_dane, ustawienia.GRUBOŚĆ_RAMKI)

        # Pobieranie liczb dla aktualnie klikniętej zakładki
        stats = ranking.get(aktywny_poziom, {"wygrane": 0, "przegrane": 0, "remisy": 0})
        w = stats["wygrane"]
        p = stats["przegrane"]
        r = stats["remisy"]
        razem = w + p + r
        win_rate = (w / razem * 100) if razem > 0 else 0.0

        # Renderowanie wskaźników tekstowych
        txt_w = czcionka_danych.render(f"Wygrane (X): {w}", True, ustawienia.ZIELEN)
        txt_p = czcionka_danych.render(f"Przegrane (O): {p}", True, ustawienia.CZERWIEN)
        txt_r = czcionka_danych.render(f"Remisy: {r}", True, ustawienia.BIEL)
        txt_razem = czcionka_danych.render(f"Wszystkie gry: {razem}", True, ustawienia.SZARY_TEKST)
        txt_rate = czcionka_danych.render(f"Skuteczność: {win_rate:.1f}%", True, (240, 200, 40))

        # Pozycjonowanie tekstów w ramce (lewa kolumna i prawa kolumna)
        screen.blit(txt_w, (190, 250))
        screen.blit(txt_p, (190, 300))
        screen.blit(txt_r, (190, 350))
        screen.blit(txt_razem, (440, 250))
        screen.blit(txt_rate, (440, 300))

        # Przycisk powrotu do Menu Głównego
        kolor_powrotu = ustawienia.daj_kolor_przycisku(btn_powrot, mouse_pos)
        pygame.draw.rect(screen, kolor_powrotu, btn_powrot, ustawienia.GRUBOŚĆ_RAMKI)
        txt_powrot = czcionka_danych.render("Powrót do menu", True, kolor_powrotu)
        screen.blit(txt_powrot, (btn_powrot.centerx - txt_powrot.get_width() // 2,
                                 btn_powrot.centery - txt_powrot.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_powrot.collidepoint(mouse_pos):
                    return  # Wyjście z menu statystyk i powrót

                # Przełączanie zakładek po kliknięciu
                for poziom, rect in zakladki.items():
                    if rect.collidepoint(mouse_pos):
                        aktywny_poziom = poziom

        pygame.display.flip()
        clock.tick(60)