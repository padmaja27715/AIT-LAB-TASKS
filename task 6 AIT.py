def is_safe(v, graph, color, c):
    """Check if color 'c' can be assigned to vertex 'v'."""
    return all(color[i] != c for i in range(len(graph)) if graph[v][i])

def solve_3color(graph, color, v=0):
    """Backtracking solver for 3-coloring."""
    if v == len(graph):
        return True
    
    for c in range(1, 4):  # Colors 1, 2, 3
        if is_safe(v, graph, color, c):
            color[v] = c
            if solve_3color(graph, color, v + 1):
                return True
            color[v] = 0  # Backtrack
            
    return False

# --- TEST CASE 1: Cycle Graph C4 (4 buildings in a ring) ---
# Building connections: 0-1, 1-2, 2-3, 3-0
campus_ring = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

color = [0] * 4
if solve_3color(campus_ring, color):
    print("Ring Layout Solution:")
    for building, col in enumerate(color):
        print(f"  Building {building}: Color {col}")
else:
    print("Ring Layout: No solution possible.")

print("-" * 30)

# --- TEST CASE 2: Complete Graph K4 (Every building connects to all others) ---
campus_complete = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

color = [0] * 4
if solve_3color(campus_complete, color):
    print("Complete Layout Solution:", color)
else:
    print("Complete Layout: Cannot color with 3 colors (requires 4).")
