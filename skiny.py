import pygame
import sys
import ustawienia

aktualny_skin = "Standard"

def run_skins_menu(screen):
    global aktualny_skin
    clock = pygame.time.Clock()
    
    czcionka_tytulu = pygame.font.SysFont("Arial", 38, bold=True)
    czcionka_skinow = pygame.font.SysFont("Arial", 20, bold=True)
    czcionka_powrotu = pygame.font.SysFont("Arial", 24, bold=True)

    nazwy_skinow = [
        "Standard", "kolko_i_krzyzyk", "3", "4", "5",
        "6", "7", "8", "9", "10"
    ]

    SZEROKOSC_BOXA = 130
    WYSOKOSC_BOXA = 65
    ODSTEP_X = 15
    ODSTEP_Y = 35
    START_X = (ustawienia.OKNO_SZEROKOSC - (5 * SZEROKOSC_BOXA + 4 * ODSTEP_X)) // 2
    START_Y = 220

    przyciski_skinow = []
    for i, nazwa in enumerate(nazwy_skinow):
        kolumna = i % 5
        wiersz = i // 5
        x = START_X + kolumna * (SZEROKOSC_BOXA + ODSTEP_X)
        y = START_Y + wiersz * (WYSOKOSC_BOXA + ODSTEP_Y)
        przyciski_skinow.append({"rect": pygame.Rect(x, y, SZEROKOSC_BOXA, WYSOKOSC_BOXA), "nazwa": nazwa})

    przycisk_powrot = pygame.Rect(300, 480, 200, 50)

    while True:
        pozycja_myszki = pygame.mouse.get_pos()
        screen.fill(ustawienia.CZERN_TLA)

        tekst_tytulu = czcionka_tytulu.render("Wybór skinów", True, ustawienia.BIEL)
        X_tytulu = (ustawienia.OKNO_SZEROKOSC // 2) - (tekst_tytulu.get_width() // 2)
        screen.blit(tekst_tytulu, (X_tytulu, 100))

        for p in przyciski_skinow:
            if p["nazwa"] == aktualny_skin:
                kolor_ramki = ustawienia.ZIELEN
                pygame.draw.rect(screen, kolor_ramki, p["rect"])
                kolor_tekstu = ustawienia.CZERN_TLA
            else:
                kolor_ramki = (0, 255, 0) if p["rect"].collidepoint(pozycja_myszki) else (0, 120, 50)
                pygame.draw.rect(screen, kolor_ramki, p["rect"], ustawienia.GRUBOŚĆ_RAMKI)
                kolor_tekstu = ustawienia.BIEL

            napis = czcionka_skinow.render(p["nazwa"], True, kolor_tekstu)
            X_tekstu = p["rect"].x + (p["rect"].width // 2) - (napis.get_width() // 2)
            Y_tekstu = p["rect"].y + (p["rect"].height // 2) - (napis.get_height() // 2)
            screen.blit(napis, (X_tekstu, Y_tekstu))

        kolor_powrotu = (150, 150, 150) if przycisk_powrot.collidepoint(pozycja_myszki) else (100, 100, 100)
        pygame.draw.rect(screen, kolor_powrotu, przycisk_powrot, ustawienia.GRUBOŚĆ_RAMKI)
        napis_powrot = czcionka_powrotu.render("Powrót", True, kolor_powrotu)
        screen.blit(napis_powrot, (przycisk_powrot.x + (przycisk_powrot.width // 2) - (napis_powrot.get_width() // 2),
                                    przycisk_powrot.y + (przycisk_powrot.height // 2) - (napis_powrot.get_height() // 2)))

        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
                for p in przyciski_skinow:
                    if p["rect"].collidepoint(pozycja_myszki):
                        aktualny_skin = p["nazwa"]
                        print(f"Zmieniono skin na: {aktualny_skin}")

                        if aktualny_skin == "Standard":
                                ustawienia.AKTUALNY_SKIN_X = "x_skin.png"
                                ustawienia.AKTUALNY_SKIN_O = "o_skin.png"
                        elif aktualny_skin == "kolko_i_krzyzyk":
                                ustawienia.AKTUALNY_SKIN_X = "cross.png"   
                                ustawienia.AKTUALNY_SKIN_O = "circle.png"  
                
                if przycisk_powrot.collidepoint(pozycja_myszki):
                    return {"action": "BACK", "skin": aktualny_skin}

        pygame.display.flip()
        clock.tick(60)
