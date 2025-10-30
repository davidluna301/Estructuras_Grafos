def load_maze_data(file_path: str):
    edges = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # Parse edges of form "(x1,y1)-(x2,y2)"
            part1, part2 = line.split('-')
            x1, y1 = map(int, part1.strip('()').split(','))
            x2, y2 = map(int, part2.strip('()').split(','))
            edges.append(((x1, y1), (x2, y2)))
    return edges
