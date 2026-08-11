import heapq


class CampusGraph:

  def __init__(self):
    # Adjacency list for campus locations: {node: {neighbor: distance}}
    self.edges = {}
    # Straight-line estimated distance (heuristic) to the Goal (CS Dept)
    self.heuristics = {}

  def add_edge(self, from_node, to_node, cost):
    if from_node not in self.edges:
      self.edges[from_node] = {}
    self.edges[from_node][to_node] = cost

    # Assuming undirected pathways
    if to_node not in self.edges:
      self.edges[to_node] = {}
    self.edges[to_node][from_node] = cost

  def set_heuristic(self, node, h_value):
    self.heuristics[node] = h_value

  def a_star_search(self, start, goal):
    # Priority queue stores tuples of: (f_score, current_node, path_taken, g_score)
    open_set = []
    heapq.heappush(
        open_set, (self.heuristics.get(start, 0), start, [start], 0)
    )

    # Keep track of visited costs to avoid redundant processing
    g_scores = {start: 0}

    while open_set:
      f, current, path, current_g = heapq.heappop(open_set)

      # If we reached the target destination
      if current == goal:
        return path, current_g

      if current not in self.edges:
        continue

      for neighbor, weight in self.edges[current].items():
        tentative_g = current_g + weight

        # If this path to neighbor is better than any previous one
        if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
          g_scores[neighbor] = tentative_g
          f_score = tentative_g + self.heuristics.get(neighbor, 0)
          new_path = path + [neighbor]
          heapq.heappush(open_set, (f_score, neighbor, new_path, tentative_g))

    return None, float("inf")


# --- Setup Campus Map ---
campus = CampusGraph()

# Define paths and distances (in meters) between campus locations
campus.add_edge("Main Gate", "Library", 150)
campus.add_edge("Main Gate", "Admin Block", 200)
campus.add_edge("Library", "Cafeteria", 100)
campus.add_edge("Admin Block", "Cafeteria", 120)
campus.add_edge("Admin Block", "Science Block", 250)
campus.add_edge("Cafeteria", "CS Department", 300)
campus.add_edge("Science Block", "CS Department", 150)

# Define Heuristics (Straight-line distance estimation to Computer Science Dept)
campus.set_heuristic("Main Gate", 400)
campus.set_heuristic("Library", 280)
campus.set_heuristic("Admin Block", 250)
campus.set_heuristic("Cafeteria", 200)
campus.set_heuristic("Science Block", 100)
campus.set_heuristic("CS Department", 0)

# Execute A* Search
start_location = "Main Gate"
goal_location = "CS Department"

optimal_path, total_distance = campus.a_star_search(start_location, goal_location)

print(f"Start Location: {start_location}")
print(f"Goal Location: {goal_location}")
print("----------------------------------------")
print("Optimal Path Found:", " -> ".join(optimal_path))
print(f"Total Walking Distance: {total_distance} meters")
