# domain/maze.py

import networkx as nx

class Maze:
    """
    Maze domain entity representing a maze as a graph.
    """

    def __init__(self):
        self.graph = nx.Graph()

    def add_connection(self, cell_a, cell_b):
        """
        Adds a bidirectional connection between two cells.
        :param cell_a: tuple (x, y)
        :param cell_b: tuple (x, y)
        """
        self.graph.add_edge(cell_a, cell_b)

    def get_neighbors(self, cell):
        """
        Returns all connected neighbors of a given cell.
        """
        return list(self.graph.neighbors(cell))

    def get_all_cells(self):
        """
        Returns all cells in the maze.
        """
        return list(self.graph.nodes)

    def is_connected(self, start, end):
        """
        Checks if there is a path between start and end.
        """
        return nx.has_path(self.graph, start, end)

    def shortest_path(self, start, end):
        """
        Returns the shortest path between start and end using BFS.
        """
        try:
            return nx.shortest_path(self.graph, source=start, target=end)
        except nx.NetworkXNoPath:
            return []

    def __len__(self):
        return self.graph.number_of_nodes()

    def __repr__(self):
        return f"<Maze nodes={len(self.graph.nodes)} edges={len(self.graph.edges)}>"
