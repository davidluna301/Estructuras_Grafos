import networkx as nx

def build_graph(edges):
    G = nx.Graph()
    for edge in edges:
        G.add_edge(*edge)
    return G
