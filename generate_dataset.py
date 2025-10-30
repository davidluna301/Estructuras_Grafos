# generate_dataset.py
import random
import os

def generate_connected_maze(file_path="data/maze_data.txt", size=10, extra_edges=20):
    """
    Generates a guaranteed solvable maze dataset.
    Ensures there is a path from (0,0) to (size-1,size-1).
    Output format: (x1,y1)-(x2,y2)
    """
    # Create list of all cells
    cells = [(x, y) for x in range(size) for y in range(size)]
    
    # Possible moves (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visited = set()
    edges = []
    
    def neighbors(cell):
        x, y = cell
        result = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                result.append((nx, ny))
        random.shuffle(result)
        return result
    
    # Recursive DFS to ensure full connectivity (a spanning tree)
    def dfs(cell):
        visited.add(cell)
        for nb in neighbors(cell):
            if nb not in visited:
                edges.append((cell, nb))
                dfs(nb)
    
    # Start DFS from top-left cell
    dfs((0, 0))
    
    # Add some extra random edges to make multiple possible paths
    for _ in range(extra_edges):
        a, b = random.sample(cells, 2)
        if abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 and (a, b) not in edges and (b, a) not in edges:
            edges.append((a, b))
    
    # Ensure folder exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write to file
    with open(file_path, "w") as file:
        for (x1, y1), (x2, y2) in edges:
            file.write(f"({x1},{y1})-({x2},{y2})\n")
    
    print(f"✅ Connected maze generated: {len(edges)} edges, size={size}x{size}")
    print(f"📄 Saved to {file_path}")
    print("🔗 Guaranteed path exists between (0,0) and", (size-1, size-1))

if __name__ == "__main__":
    generate_connected_maze()
