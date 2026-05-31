import pygame
import sys
import os
import ustawienia

pygame.init()

ekran = pygame.display.set_mode((ustawienia.OKNO_SZEROKOSC, ustawienia.OKNO_WYSOKOSC))
pygame.display.set_caption("Tic-Tac-Toe")

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
    
        ekran.fill(ustawienia.CZERN_TLA)

        tekst_nazwy = czcionka_nazwy_gry.render("TIC-TAC-TOE", True, ustawienia.BIEL)
        X_nazwy = (ustawienia.OKNO_SZEROKOSC // 2) - (tekst_nazwy.get_width() // 2)
        Y_nazwy = 120
        
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