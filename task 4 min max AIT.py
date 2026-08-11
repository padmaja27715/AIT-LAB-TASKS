# Tic-Tac-Toe with Minimax and Alpha-Beta Pruning

def print_board(board):
    for i in range(0, 9, 3):
        row = [str(c) if c is not None else ' ' for c in board[i:i+3]]
        print(" | ".join(row))
        if i < 6:
            print("-" * 9)

def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] is not None:
            return board[a]
    if None not in board:
        return 'Tie'
    return None

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif winner == 'Tie':
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] is None:
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = None
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] is None:
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = None
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board):
    best_val = -float('inf')
    best_move = -1
    for i in range(9):
        if board[i] is None:
            board[i] = 'O'
            move_val = minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = None
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

# --- Demonstration / Output Simulation ---
if __name__ == "__main__":
    # Example board configuration where X made the first move at the center
    # Indices: 0 1 2 / 3 4 5 / 6 7 8
    initial_board = [
        None, None, None,
        None, 'X',  None,
        None, None, None
    ]
    
    print("Initial Board (X played center):")
    print_board(initial_board)
    
    best_move = find_best_move(initial_board)
    print(f"\nOptimal move calculated for AI (O): Index {best_move} (Corner)")
    
    initial_board[best_move] = 'O'
    print("\nBoard after AI's optimal move:")
    print_board(initial_board)
