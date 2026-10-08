from maze_to_graph import maze_to_graph, maze

graph = maze_to_graph(maze)

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
        
    visited.add(start)
    path = path + [start]
    
    if start == goal:
        return path
        
    # Unpack neighbor coordinate and ignore step cost using _
    for neighbor, _ in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result:
                return result
    return None

if __name__ == "__main__":
    start = (0, 0)  # Starting point 'S'
    goal = (4, 5)   # Goal point 'G'
    
    path = dfs(graph, start, goal)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
        