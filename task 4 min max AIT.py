def check(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for x,y,z in wins:
        if b[x] == b[y] == b[z] and b[x]: return b[x]
    return 'Tie' if None not in b else None

def minimax(b, is_max, alpha, beta):
    w = check(b)
    if w: return 1 if w == 'O' else (-1 if w == 'X' else 0)
    
    if is_max:
        val = -99
        for i in range(9):
            if not b[i]:
                b[i] = 'O'
                val = max(val, minimax(b, False, alpha, beta))
                b[i] = None
                alpha = max(alpha, val)
                if beta <= alpha: break
        return val
    else:
        val = 99
        for i in range(9):
            if not b[i]:
                b[i] = 'X'
                val = min(val, minimax(b, True, alpha, beta))
                b[i] = None
                beta = min(beta, val)
                if beta <= alpha: break
        return val

# Example usage
board = [None,None,None, None,'X',None, None,None,None]
best_move = max([i for i in range(9) if not board[i]], 
                key=lambda i: (board.__setitem__(i, 'O'), val := minimax(board, False, -99, 99), board.__setitem__(i, None), val)[3])
print("Best move for O:", best_move)
