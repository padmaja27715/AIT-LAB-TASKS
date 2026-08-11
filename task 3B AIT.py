import heapq

class Graph:
    def __init__(self):
        # Adjacency list storing neighboring nodes and edge weights (distances)
        self.edges = {}
        # Straight-line heuristic distances from each node to the Goal (G)
        self.heuristics = {}

    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))

    def set_heuristic(self, node, h_value):
        self.heuristics[node] = h_value

def a_star_search(graph, start, goal):
    # Priority queue stores tuples of: (estimated_total_cost, current_cost, current_node, path)
    # estimated_total_cost = g(n) [cost so far] + h(n) [heuristic]
    pq = [(0 + graph.heuristics[start], 0, start, [start])]
    
    # Keep track of visited nodes to avoid reprocessing
    visited = set()

    while pq:
        estimated_total, current_cost, current_node, path = heapq.heappop(pq)

        # If we reached the goal, return the path and total distance
        if current_node == goal:
            return path, current_cost

        if current_node in visited:
            continue
        visited.add(current_node)

        # Explore neighbors
        for neighbor, weight in graph.edges.get(current_node, []):
            if neighbor in visited:
                continue
            
            new_cost = current_cost + weight
            h_cost = graph.heuristics.get(neighbor, 0)
            estimated_total = new_cost + h_cost
            
            heapq.heappush(pq, (estimated_total, new_cost, neighbor, path + [neighbor]))

    return None, float('inf')

# ==========================================
# Defining the GPS Map (Home = A, College = G)
# ==========================================
road_map = Graph()

# Define road distances (edges) between locations
# Format: road_map.add_edge(From, To, Distance in km)
road_map.add_edge('A', 'B', 4)
road_map.add_edge('A', 'C', 2)
road_map.add_edge('B', 'D', 5)
road_map.add_edge('C', 'D', 8)
road_map.add_edge('C', 'E', 10)
road_map.add_edge('D', 'E', 2)
road_map.add_edge('D', 'F', 6)
road_map.add_edge('E', 'G', 3)
road_map.add_edge('F', 'G', 4)

# Define heuristic values (straight-line estimated distance to Goal 'G')
road_map.set_heuristic('A', 7)
road_map.set_heuristic('B', 6)
road_map.set_heuristic('C', 5)
road_map.set_heuristic('D', 3)
road_map.set_heuristic('E', 2)
road_map.set_heuristic('F', 2)
road_map.set_heuristic('G', 0)

# ==========================================
# Execute the Navigation System
# ==========================================
start_location = 'A'
goal_location = 'G'

optimal_path, total_distance = a_star_search(road_map, start_location, goal_location)

print("--- GPS Navigation System ---")
print(f"Starting Point: Home ({start_location})")
print(f"Destination: College ({goal_location})")
print(f"Shortest Route Found: {' -> '.join(optimal_path)}")
print(f"Total Travel Distance: {total_distance} km")
