from infrastructure.file_loader import load_maze_data
from infrastructure.graph_builder import build_graph
from domain.pathfinder import find_path
from presentation.plotter import plot_maze

def main():
    file_path = "data/maze_data.txt"
    edges = load_maze_data(file_path)
    graph = build_graph(edges)
    
    start = (0, 0)
    goal = (4, 4)
    
    path = find_path(graph, start, goal)
    print("Path found:", path)
    
    plot_maze(graph, path)

if __name__ == "__main__":
    main()
