import pygame
import sys
import ustawienia

#Algorytm sprawdzajacy wygrana
def check_winner(board, size, win_length):
    for r in range(size):
        for c in range(size):
            symbol = board[r][c]
            if symbol is None:
                continue
            
            # Sprawdzanie w poziomie
            if c + win_length <= size:
                if all(board[r][c + i] == symbol for i in range(win_length)):
                    return symbol
            
            # Sprawdzanie w pionie w dół
            if r + win_length <= size:
                if all(board[r + i][c] == symbol for i in range(win_length)):
                    return symbol
            
            # Sprawdzanie po przekątnej w dół i w prawo
            if r + win_length <= size and c + win_length <= size:
                if all(board[r + i][c + i] == symbol for i in range(win_length)):
                    return symbol
            
            # Sprawdzanie po przekątnej w dół i w lewo
            if r + win_length <= size and c - win_length >= -1:
                if all(board[r + i][c - i] == symbol for i in range(win_length)):
                    return symbol
                    
    return None