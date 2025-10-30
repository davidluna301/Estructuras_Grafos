# visualize_maze.py
import networkx as nx
import matplotlib.pyplot as plt

def load_maze_data(file_path):
    """
    Load maze edges from file. Format: (x1,y1)-(x2,y2)
    """
    edges = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            part1, part2 = line.split('-')
            x1, y1 = map(int, part1.strip('()').split(','))
            x2, y2 = map(int, part2.strip('()').split(','))
            edges.append(((x1, y1), (x2, y2)))
    return edges

def plot_maze_graph(edges):
    """
    Plots the maze graph.
    """
    G = nx.Graph()
    G.add_edges_from(edges)

    # Positions based on coordinates
    pos = {node: node for node in G.nodes()}

    plt.figure(figsize=(8, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        node_size=400,
        font_size=8,
        width=2,
    )
    plt.title("Maze Graph Visualization")
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    file_path = "data/maze_data.txt"  # Ajusta según tu ruta
    edges = load_maze_data(file_path)
    plot_maze_graph(edges)
