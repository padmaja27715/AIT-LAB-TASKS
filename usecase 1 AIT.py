import heapq

# Map representation: Graph with actual distances (edge weights)
graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("C", 1), ("D", 5)],
    "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
    "D": [("B", 5), ("C", 8), ("E", 2)],
    "E": [("C", 10), ("D", 2)],
}

# Heuristic values (estimated distance to Goal 'E')
heuristic = {"A": 7, "B": 6, "C": 5, "D": 2, "E": 0}


def a_star(start, goal):
    # Priority Queue stores: (f_score, current_cost, current_node, path)
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f_score, g_score, current, path = heapq.heappop(queue)

        if current == goal:
            return path, g_score

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_g = g_score + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float("inf")


# Run A* Algorithm from 'A' to 'E'
path, total_cost = a_star("A", "E")
print(f"Optimal Path: {' -> '.join(path)}")
print(f"Total Distance: {total_cost}")
