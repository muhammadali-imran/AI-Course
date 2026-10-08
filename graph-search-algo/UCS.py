import heapq
from maze_to_graph import maze_to_graph, maze

graph = maze_to_graph(maze)

def ucs(graph, start, goal):
    # graph: {node: [(neighbor, cost), ...]}
    frontier = [(0, start, [start])]
    visited = {}
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node == goal:
            return path, cost
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        for neighbor, step_cost in graph.get(node, []):
            heapq.heappush(frontier, (cost + step_cost, neighbor, path + [neighbor]))
    return None, float("inf")

if __name__ == "__main__":
    start = (0, 0)  # Starting point 'S'
    goal = (4, 5)   # Goal point 'G'
    path, cost = ucs(graph, start, goal)
    if path:
        print("Path found:", path)
        print("Total cost:", cost)
    else:
        print("No path found.")
        