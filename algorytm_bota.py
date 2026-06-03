# Algorytm Minimax
def minimax(b, depth, is_maximizing)
    if check_winner(b, 'O') return 10 - depth  # Bot ('O') preferuje szybszą wygraną
    if check_winner(b, 'X') return depth - 10  # Gracz ('X')
    if is_board_full(b) return 0

    if is_maximizing
        best_score = -math.inf
        for i in range(9)
            if b[i] == ' '
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else
        best_score = math.inf
        for i in range(9)
            if b[i] == ' '
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score