def solve_4_queens():
    def is_safe(row, col, board):
        for i in range(row):
            # Check column and diagonals
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row, board, solutions):
        if row == 4:
            solutions.append(board[:])
            return
        
        for col in range(4):
            if is_safe(row, col, board):
                board[row] = col
                backtrack(row + 1, board, solutions)
                board[row] = -1  # Backtrack

    solutions = []
    backtrack(0, [-1] * 4, solutions)
    return solutions

# Run the solver and format the output
solutions = solve_4_queens()

print(f"Total valid solutions found: {len(solutions)}\n")
for idx, sol in enumerate(solutions, 1):
    print(f"Solution {idx} (Column positions per row): {sol}")
    print("Board Representation:")
    for row in range(4):
        line = ""
        for col in range(4):
            if sol[row] == col:
                line += " Q "
            else:
                line += " . "
        print(line)
    print("-" * 20)
