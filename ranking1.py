import json
import os

PLIK_RANKINGU = "ranking.json"

def wczytaj_ranking():
    #Wczytuje ranking z pliku. Jeśli plik nie istnieje, zwraca pusty słownik
    domyslny_ranking = {
        "Łatwy": {"wygrane": 0, "przegrane": 0, "remisy": 0},
        "Średni": {"wygrane": 0, "przegrane": 0, "remisy": 0},
        "Trudny": {"wygrane": 0, "przegrane": 0, "remisy": 0}
    }
    if not os.path.exists(PLIK_RANKINGU):
        return domyslny_ranking
    
    try:
        with open(PLIK_RANKINGU, "r", encoding="utf-8") as f:
            dane = json.load(f)
            # Upewniamy się, że w pliku są wszystkie poziomy trudności
            for poziom in domyslny_ranking:
                if poziom not in dane:
                    dane[poziom] = domyslny_ranking[poziom]
            return dane
    except Exception:
        return domyslny_ranking
    except Exception:
        return {}  # W razie błędu pliku, zwracamy pusty ranking

def zapisz_ranking(ranking):
    """Zapisuje aktualny ranking do pliku JSON."""
    with open(PLIK_RANKINGU, "w", encoding="utf-8") as f:
        json.dump(ranking, f, indent=4, ensure_ascii=False)


def dodaj_wynik(poziom, rezultat):
    """rezultat może przyjąć wartość: 'wygrane', 'przegrane' lub 'remisy'"""
    if poziom not in ["Łatwy", "Średni", "Trudny"]:
        return  # Ignorujemy zapis, jeśli to np. mecz multiplayer

    ranking = wczytaj_ranking()
    ranking[poziom][rezultat] += 1
    zapisz_ranking(ranking)