import pygame
import sys
import os
import ustawienia
import menu_gry
import skiny
import rozgrywka
import menu_statystyk

os.chdir(os.path.dirname(os.path.abspath(__file__))) #Dzieki temu program nie szuka grafik w folderze C:\Users\USER, tylko w dobrym

pygame.init()

ekran = pygame.display.set_mode((ustawienia.OKNO_SZEROKOSC, ustawienia.OKNO_WYSOKOSC))
pygame.display.set_caption("Tic-Tac-Toe")

#Wczytuje logo gry
try:
    logo_raw = pygame.image.load("logo.png").convert()
    logo_raw.set_colorkey((255, 255, 255))
    WIELKOSC_LOGO = 180
    logo_image = pygame.transform.smoothscale(logo_raw, (WIELKOSC_LOGO, WIELKOSC_LOGO))
except pygame.error:
    logo_image = None

czcionka_przyciskow = pygame.font.SysFont("Arial", 26, bold=True)
czcionka_nazwy_gry = pygame.font.SysFont("Arial", 38, bold=True)

przycisk_bot = pygame.Rect(250, 300, 300, 50)
przycisk_skiny = pygame.Rect(250, 370, 300, 50)
przycisk_multi = pygame.Rect(250, 440, 300, 50)
przycisk_stats = pygame.Rect(250, 510, 300, 50)

przyciski = [
    {"rect": przycisk_bot, "tekst": "Gra z komputerem"},
    {"rect": przycisk_skiny, "tekst": "Wybór skinów"},
    {"rect": przycisk_multi, "tekst": "Gra wieloosobowa"},
    {"rect": przycisk_stats, "tekst": "Statystyki"}
]

def main_menu():
    while True:
        pozycja_myszki = pygame.mouse.get_pos()
        
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
                for p in przyciski:
                    if p["rect"].collidepoint(pozycja_myszki):
                        print(f"Kliknięto: {p['tekst']}")

                        if p["tekst"] == "Gra z komputerem":
                            wynik = menu_gry.run_game_setup_menu(ekran, is_singleplayer=True)
                            if wynik["action"] == "START":
                                print(f"Przekazuję do silnika gry tryb BOT. Dane: {wynik}")
                                rozgrywka.run_game_loop(ekran, size=wynik["size"], difficulty=wynik["difficulty"], is_timed=wynik.get("timed", False))

                        elif p["tekst"] == "Gra wieloosobowa":
                            wynik = menu_gry.run_game_setup_menu(ekran, is_singleplayer=False)
                            if wynik["action"] == "START":
                                print(f"Przekazuję do silnika gry tryb MULTI. Dane: {wynik}")

                        elif p["tekst"] == "Wybór skinów":
                            wynik_skinow = skiny.run_skins_menu(ekran)
                            print(f"Powrót do menu. Aktywny skin w systemie: {wynik_skinow['skin']}")

                        elif p["tekst"] == "Statystyki":
                            menu_statystyk.run_stats_menu(ekran)
    
        ekran.fill(ustawienia.CZERN_TLA)

        #Rysowanie loga
        if logo_image:
            X_logo = (ustawienia.OKNO_SZEROKOSC // 2) - (logo_image.get_width() // 2)
            Y_logo = 15
            ekran.blit(logo_image, (X_logo, Y_logo))

        tekst_nazwy = czcionka_nazwy_gry.render("TIC-TAC-TOE", True, ustawienia.BIEL)
        X_nazwy = (ustawienia.OKNO_SZEROKOSC // 2) - (tekst_nazwy.get_width() // 2)
        Y_nazwy = 210
        
        ekran.blit(tekst_nazwy, (X_nazwy, Y_nazwy))

        for p in przyciski:
            kolor_elementu = ustawienia.daj_kolor_przycisku(p["rect"], pozycja_myszki)
            
            pygame.draw.rect(ekran, kolor_elementu, p["rect"], ustawienia.GRUBOŚĆ_RAMKI)

            napis = czcionka_przyciskow.render(p["tekst"], True, kolor_elementu)
            X_tekstu = p["rect"].x + (p["rect"].width // 2) - (napis.get_width() // 2)
            Y_tekstu = p["rect"].y + (p["rect"].height // 2) - (napis.get_height() // 2)
            ekran.blit(napis, (X_tekstu, Y_tekstu))
            
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()