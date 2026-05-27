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
