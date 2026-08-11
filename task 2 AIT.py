def hill_climbing(grid):
  rows = len(grid)
  cols = len(grid[0])

  # Start from the bottom-left corner (Row 4, Column 0)
  current_r, current_c = rows - 1, 0
  path = [(current_r, current_c, grid[current_r][current_c])]

  while True:
    current_val = grid[current_r][current_c]
    best_r, best_c = current_r, current_c
    max_val = current_val

    # Define possible movements: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
      nr, nc = current_r + dr, current_c + dc
      # Check boundary conditions
      if 0 <= nr < rows and 0 <= nc < cols:
        if grid[nr][nc] > max_val:
          max_val = grid[nr][nc]
          best_r, best_c = nr, nc

    # If no better neighbor is found, stop climbing
    if best_r == current_r and best_c == current_c:
      break

    # Move to the best neighbor
    current_r, current_c = best_r, best_c
    path.append((current_r, current_c, grid[current_r][current_c]))

  return path


# Sample 5x5 Elevation Grid
elevation_grid = [
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10],
    [3, 6, 9, 12, 15],
    [4, 8, 12, 16, 20],
    [5, 10, 15, 20, 25],
]

# Run the algorithm
robot_path = hill_climbing(elevation_grid)

print("--- Robot Hill Climbing Simulation ---")
for step, (r, c, val) in enumerate(robot_path):
  print(f"Step {step}: Position ({r}, {c}) -> Elevation: {val}")

final_peak = robot_path[-1]
print(
    f"\nReached Peak at Position ({final_peak[0]}, {final_peak[1]}) with"
    f" Elevation {final_peak[2]}"
)
