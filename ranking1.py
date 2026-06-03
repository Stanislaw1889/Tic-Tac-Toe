import json
import os

RANKING_FILE = "ranking.json"

def wczytaj_ranking():
    #Wczytuje ranking z pliku. Jeśli plik nie istnieje, zwraca pusty słownik
    if not os.path.exists(RANKING_FILE):
        return {}
    
    try:
        with open(RANKING_FILE, "r", encoding="utf-8") as plik:
            return json.load(plik)
    except Exception:
        return {}  # W razie błędu pliku, zwracamy pusty ranking

def zapisz_ranking(ranking):
    """Zapisuje aktualny ranking do pliku JSON."""
    with open(RANKING_FILE, "w", encoding="utf-8") as plik:
        json.dump(ranking, plik, indent=4, ensure_ascii=False)
