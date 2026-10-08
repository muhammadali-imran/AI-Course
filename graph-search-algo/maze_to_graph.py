maze = [
    "S . . # . .",
    ". # . # . .",
    ". # . . . .",
    ". # # # # .",
    ". . . . # G",
]

def maze_to_graph(maze, default_cost=1):
    rows = [row.split() for row in maze]
    graph = {}
    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if cell == "#":
                continue
            neighbors = []
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(rows) and 0 <= nc < len(rows[0]) and rows[nr][nc] != "#":
                    # Formatted as ((neighbor_row, neighbor_col), cost)
                    neighbors.append(((nr, nc), default_cost))
            graph[(r, c)] = neighbors
    return graph

if __name__ == "__main__":
    graph = maze_to_graph(maze)
    print("Graph representation of the maze (with step costs):")
    
    for node, neighbors in graph.items():
        coords_only = [neighbor for neighbor, _ in neighbors]
        print(f"{node}: {coords_only}")
