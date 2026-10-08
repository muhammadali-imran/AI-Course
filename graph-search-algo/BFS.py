from collections import deque
from maze_to_graph import maze_to_graph, maze

graph = maze_to_graph(maze)

def bfs(graph, start, goal):
    visited = {start}
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
            
        # Unpack neighbor coordinate and ignore step cost using _
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
                
    return None

if __name__ == "__main__":
    start = (0, 0)  # Starting point 'S'
    goal = (4, 5)   # Goal point 'G'
    
    path = bfs(graph, start, goal)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
        