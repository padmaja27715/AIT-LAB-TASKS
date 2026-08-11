from collections import deque

def bfs_file_system(graph, root):
    queue = deque([root])  # 1. Initialize queue with root
    visited = set([root])  # 2. Track visited folders to avoid duplicates
    
    level = 0
    while queue:
        level_size = len(queue)  # Number of folders at current level
        print(f"Level {level}:", end=" ")
        
        # Process all folders belonging to the current level
        for _ in range(level_size):
            folder = queue.popleft()
            print(folder, end="  ")
            
            # Enqueue all unvisited subfolders
            for neighbor in graph.get(folder, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        print()  # New line for next level
        level += 1

# --- Example Usage ---
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

bfs_file_system(file_system, "Root")
