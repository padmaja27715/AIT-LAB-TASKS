def dfs_file_system(graph, folder, visited=None):
    # 1. Initialize visited set on the first root call
    if visited is None:
        visited = set()

    # 2. Mark current folder as visited and print it
    visited.add(folder)
    print(folder)

    # 3. Recursively visit each unvisited subfolder
    for subfolder in graph.get(folder, []):
        if subfolder not in visited:
            dfs_file_system(graph, subfolder, visited)


# --- Same Example File System Graph ---
file_system = {
    "Root": ["Documents", "Pictures", "System"],
    "Documents": ["Work", "Personal"],
    "Pictures": ["Vacation.jpg"],
    "System": ["Logs"],
    "Work": [],
    "Personal": [],
    "Vacation.jpg": [],
    "Logs": []
}

# Run DFS starting from "Root"
dfs_file_system(file_system, "Root")
