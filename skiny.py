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

    #Rozszerzam liste do 15 miejsc
    nazwy_skinow = [
        "Skin 1", "Skin 2", "Skin 3", "Skin 4", "Skin 5",
        "Skin 6", "Skin 7", "Skin 8", "Skin 9", "Skin 10",
        "Skin 11", "Skin 12", "Skin 13", "Skin 14", "Skin 15"
    ]

    SZEROKOSC_BOXA = 130
    WYSOKOSC_BOXA = 60
    ODSTEP_X = 15
    ODSTEP_Y = 25
    START_X = (ustawienia.OKNO_SZEROKOSC - (5 * SZEROKOSC_BOXA + 4 * ODSTEP_X)) // 2
    START_Y = 170

    przyciski_skinow = []
    for i, nazwa in enumerate(nazwy_skinow):
        kolumna = i % 5
        wiersz = i // 5
        x = START_X + kolumna * (SZEROKOSC_BOXA + ODSTEP_X)
        y = START_Y + wiersz * (WYSOKOSC_BOXA + ODSTEP_Y)
        przyciski_skinow.append({"rect": pygame.Rect(x, y, SZEROKOSC_BOXA, WYSOKOSC_BOXA), "nazwa": nazwa})

    przycisk_powrot = pygame.Rect(300, 500, 200, 50)

    while True:
        pozycja_myszki = pygame.mouse.get_pos()
        screen.fill(ustawienia.CZERN_TLA)

        tekst_tytulu = czcionka_tytulu.render("Wybór skinów", True, ustawienia.BIEL)
        X_tytulu = (ustawienia.OKNO_SZEROKOSC // 2) - (tekst_tytulu.get_width() // 2)
        screen.blit(tekst_tytulu, (X_tytulu, 90))

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
        screen.blit(napis_powrot, (przycisk_powrot.centerx - napis_powrot.get_width() // 2,
                                   przycisk_powrot.centery - napis_powrot.get_height() // 2))

        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if zdarzenie.type == pygame.MOUSEBUTTONDOWN and zdarzenie.button == 1:
                for p in przyciski_skinow:
                    if p["rect"].collidepoint(pozycja_myszki):
                        aktualny_skin = p["nazwa"]
                        print(f"Zmieniono skin na: {aktualny_skin}")

                        if aktualny_skin == "Skin 1":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/cross_black.png"
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/circle_black.png"
                        elif aktualny_skin == "Skin 2":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/cross_red.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/circle_red.png" 
                        elif aktualny_skin == "Skin 3":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/cross_green.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/circle_green.png"  
                        elif aktualny_skin == "Skin 4":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/cross_yellow.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/circle_yellow.png"  
                        elif aktualny_skin == "Skin 5":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/cross_blue.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/circle_blue.png"  
                        elif aktualny_skin == "Skin 6":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/heart_black.png"
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/ninja_black.png"
                        elif aktualny_skin == "Skin 7":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/heart_red.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/ninja_red.png" 
                        elif aktualny_skin == "Skin 8":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/heart_green.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/ninja_green.png"  
                        elif aktualny_skin == "Skin 9":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/heart_yellow.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/ninja_yellow.png"  
                        elif aktualny_skin == "Skin 10":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/heart_blue.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/ninja_blue.png"
                        elif aktualny_skin == "Skin 11":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/star_black.png"
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/triangle_black.png"
                        elif aktualny_skin == "Skin 12":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/star_red.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/triangle_red.png" 
                        elif aktualny_skin == "Skin 13":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/star_green.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/triangle_green.png"  
                        elif aktualny_skin == "Skin 14":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/star_yellow.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/triangle_yellow.png"  
                        elif aktualny_skin == "Skin 15":
                                ustawienia.AKTUALNY_SKIN_X = "assets/skiny/star_blue.png"   
                                ustawienia.AKTUALNY_SKIN_O = "assets/skiny/triangle_blue.png" 
                
                if przycisk_powrot.collidepoint(pozycja_myszki):
                    return {"action": "BACK", "skin": aktualny_skin}

        pygame.display.flip()
        clock.tick(60)
