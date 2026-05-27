import os

def czysc_ekran():
    """Czyszczenie konsoli w zależności od systemu operacyjnego."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_wyboru_skinow():
    # Kody ANSI dla kolorów (czarne tło, teksty w kolorach)
    RESET = "\033[0m"
    ZIELONY = "\033[1;32m"
    CZERWONY = "\033[1;31m"
    BIALY = "\033[1;37m"
    CZARNY_BG = "\033[40m"  # Wymuszenie czarnego tła

    # Słowniki z dostępnymi opcjami
    symbole = {
        "1": ("Krzyżyk", "X"),
        "2": ("Kółko", "O"),
        "3": ("Gwiazdka", "★"),
        "4": ("Serduszko", "♥"),
        "5": ("Kwiatek", "✿"),
        "6": ("Błyskawica", "⚡"),
        "7": ("Chmurka", "☁")
    }

    kolory = {
        "1": ("Zielony", ZIELONY),
        "2": ("Czerwony", CZERWONY),
        "3": ("Biały", BIALY)
    }

    wybory_graczy = {}

    for gracz in ["Gracz 1", "Gracz 2"]:
        while True:
            czysc_ekran()
            # Nagłówek w kolorach gry
            print(f"{CZARNY_BG}{CZERWONY}=== {ZIELONY}KÓŁKO I KRZYŻYK: WYBÓR SKINU {CZERWONY}==={RESET}")
            print(f"{CZARNY_BG}{BIALY}Wybierasz skin dla: {ZIELONY}{gracz}{RESET}\n")
            
            # Wyświetlanie dostępnych symboli
            print(f"{CZARNY_BG}{BIALY}Dostępne symbole:{RESET}")
            for klucz, (nazwa, znak) in symbole.items():
                print(f"{CZARNY_BG}{ZIELONY}{klucz}. {BIALY}{nazwa} ({znak}){RESET}")
            
            wybor_symbolu = input(f"\n{CZARNY_BG}{BIALY}Wybierz numer symbolu: {RESET}").strip()
            
            if wybor_symbolu not in symbole:
                print(f"{CZARNY_BG}{CZERWONY}Nieprawidłowy wybór! Spróbuj ponownie.{RESET}")
                input("Naciśnij Enter, aby kontynuować...")
                continue

            # Wyświetlanie dostępnych kolorów
            czysc_ekran()
            print(f"{CZARNY_BG}{CZERWONY}=== {ZIELONY}WYBÓR KOLORU {CZERWONY}==={RESET}")
            print(f"{CZARNY_BG}{BIALY}Wybrany symbol: {symbole[wybor_symbolu][1]}{RESET}\n")
            
            print(f"{CZARNY_BG}{BIALY}Dostępne kolory:{RESET}")
            for klucz, (nazwa, kod_koloru) in kolory.items():
                print(f"{CZARNY_BG}{klucz}. {kod_koloru}{nazwa}{RESET}")
                
            wybor_koloru = input(f"\n{CZARNY_BG}{BIALY}Wybierz numer koloru: {RESET}").strip()
            
            if wybor_koloru not in kolory:
                print(f"{CZARNY_BG}{CZERWONY}Nieprawidłowy wybór! Spróbuj ponownie.{RESET}")
                input("Naciśnij Enter, aby kontynuować...")
                continue
            
            # Zapisanie wyboru gracza (nazwa, sformatowany znak z kolorem do wyświetlania)
            nazwa_skina = symbole[wybor_symbolu][0]
            znak_skina = symbole[wybor_symbolu][1]
            kolor_kod = kolory[wybor_color := wybor_koloru][1]
            
            sformatowany_skin = f"{kolor_kod}{znak_skina}{RESET}"
            
            wybory_graczy[gracz] = {
                "nazwa": nazwa_skina,
                "znak": znak_skina,
                "render": sformatowany_skin
            }
            break

    # Podsumowanie wyborów
    czysc_ekran()
    print(f"{CZARNY_BG}{ZIELONY}=== KONFIGURACJA ZAKOŃCZONA ==={RESET}\n")
    print(f"{CZARNY_BG}Gracz 1 gra jako: {wybory_graczy['Gracz 1']['render']}")
    print(f"{CZARNY_BG}Gracz 2 gra jako: {wybory_graczy['Gracz 2']['render']}{RESET}\n")
    
    return wybory_graczy

# Uruchomienie funkcji, aby przetestować działanie
if __name__ == "__main__":
    skiny = menu_wyboru_skinow()
