import math
# Algorytm Minimax
def minimax(board, size, win_length, depth, is_maximizing, max_depth):
    from rozgrywka import check_winner, is_board_full #Dodanie importu
    winner = check_winner(board, size, win_length)
    if winner == "O":  # Komputer wygrywa
        return 10 - depth
    if winner == "X":  # Gracz wygrywa
        return depth - 10
    if is_board_full(board) or depth >= max_depth:
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for r in range(size):
            for c in range(size):
                if board[r][c] is None:
                    board[r][c] = "O"
                    score = minimax(board, size, win_length, depth + 1, False, max_depth)
                    board[r][c] = None  # Cofnięcie ruchu
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(size):
            for c in range(size):
                if board[r][c] is None:
                    board[r][c] = "X"
                    score = minimax(board, size, win_length, depth + 1, True, max_depth)
                    board[r][c] = None
                    best_score = min(score, best_score)
        return best_score


def smart_bot_move(board, size, win_length, difficulty):
    """
    Inteligentny bot obsługujący poziomy trudności i różne rozmiary plansz.
    """
    import random

    # 1. Poziom Łatwy: zawsze wykonuje losowy ruch
    if difficulty == "Łatwy":
        empty_cells = [(r, c) for r in range(size) for c in range(size) if board[r][c] is None]
        return random.choice(empty_cells) if empty_cells else None

    # Ustalenie bezpiecznej głębokości dla Minimaxa, żeby nie zawiesić gry na 4x4 i 5x5
    # Plansza 3x3: pełne przeszukiwanie (głębokość 9)
    # Plansze 4x4 i 5x5: ograniczona głębokość (2-3 ruchy w przód), dla płynności gry
    if size == 3:
        max_depth = 9
    else:
        max_depth = 2 if difficulty == "Średni" else 3

    # 2. Poziom Średni / Trudny: szukamy najlepszego ruchu algorytmem Minimax
    best_score = float('-inf')
    best_move = None

    # Lista ruchów o identycznym, najlepszym wyniku (żeby bot nie grał zawsze tak samo)
    good_moves = []

    for r in range(size):
        for c in range(size):
            if board[r][c] is None:
                board[r][c] = "O"
                score = minimax(board, size, win_length, 0, False, max_depth)
                board[r][c] = None  # Cofnięcie symulacji

                # Na poziomie średnim dajemy botowi 30% szans na popełnienie drobnego błędu
                if difficulty == "Średni" and random.random() < 0.3:
                    continue

                if score > best_score:
                    best_score = score
                    good_moves = [(r, c)]
                elif score == best_score:
                    good_moves.append((r, c))

    if good_moves:
        return random.choice(good_moves)

    # Fallback (awaryjny losowy ruch, gdyby pętla nic nie wybrała)
    empty_cells = [(r, c) for r in range(size) for c in range(size) if board[r][c] is None]
    return random.choice(empty_cells) if empty_cells else None