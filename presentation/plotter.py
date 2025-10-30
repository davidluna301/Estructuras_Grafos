import matplotlib.pyplot as plt
import networkx as nx

def plot_maze(graph, path=None):
    pos = {node: node for node in graph.nodes()}  # position by coordinates
    plt.figure(figsize=(8, 8))
    nx.draw(graph, pos, with_labels=True, node_color='lightgray', node_size=500)
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=3)
    
    plt.title("Maze Solution Path")
    plt.show()
