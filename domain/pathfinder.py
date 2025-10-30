import networkx as nx

def find_path(graph, start, goal):
    try:
        path = nx.shortest_path(graph, source=start, target=goal)
        return path
    except nx.NetworkXNoPath:
        print("No path found.")
        return []
