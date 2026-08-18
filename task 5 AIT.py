import random

# Distance Matrix: Depot (0) and 4 Passengers (1-4)
dist = [
    [0,  2,  5,  7, 10],
    [2,  0,  8,  3,  6],
    [5,  8,  0,  4,  2],
    [7,  3,  4,  0,  3],
    [10, 6,  2,  3,  0]
]

n = len(dist)
pheromone = [[1.0] * n for _ in range(n)]
best_cost = float('inf')
best_route = []

for _ in range(50):  # 50 Iterations
    paths = []
    for _ in range(10):  # 10 Ants
        path, visited = [0], {0}
        while len(visited) < n:
            curr = path[-1]
            probs = []
            for j in range(n):
                if j in visited or dist[curr][j] == 0:
                    probs.append(0)
                else:
                    probs.append((pheromone[curr][j] ** 1) * ((1.0 / dist[curr][j]) ** 3))
            
            total = sum(probs)
            if total == 0:
                nxt = random.choice([j for j in range(n) if j not in visited])
            else:
                # Weighted random choice without numpy
                r = random.uniform(0, total)
                s = 0
                nxt = 0
                for idx, p in enumerate(probs):
                    s += p
                    if s >= r:
                        nxt = idx
                        break
            path.append(nxt)
            visited.add(nxt)
            
        path.append(0)
        cost = sum(dist[path[i]][path[i+1]] for i in range(n))
        paths.append((path, cost))
        if cost < best_cost:
            best_route, best_cost = path, cost
            
    # Evaporation
    for r_idx in range(n):
        for c_idx in range(n):
            pheromone[r_idx][c_idx] *= 0.9
            
    # Update pheromones for top 3 ants
    paths.sort(key=lambda x: x[1])
    for path, cost in paths[:3]:
        for i in range(n):
            pheromone[path[i]][path[i+1]] += 1.0 / cost

names = ["Depot", "P1", "P2", "P3", "P4"]
print("Route:", " -> ".join(names[i] for i in best_route))
print("Distance:", best_cost)
