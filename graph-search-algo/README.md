# GRAPH SEARCH ALGORITHM

## Objective

To implement the three fundamental uninformed search algorithms — Breadth-First Search, Depth-First Search and Uniform-Cost Search — and apply them to solve a maze/grid path-finding problem and the 8-puzzle.

## Theory

Uninformed (blind) search algorithms use only the information available in the problem definition — they have no additional knowledge about how close a state is to the goal beyond the search-tree structure itself. A search problem is defined by a search space, a start state, a goal test, a set of actions/transition model, and (for cost-sensitive search) a path cost function.

Algorithm | Frontier data structure | Expansion order | Complete? | Optimal?
BFS | Queue (FIFO) | Shallowest node first | Yes | Yes (unit costs)
DFS | Stack (LIFO) | Deepest node first | Yes (finite space) | No
UCS | Priority queue by g(n) | Lowest cumulative path cost first | Yes | Yes

In UCS, the goal test is applied when a node is selected for expansion (popped from the priority queue), not when it is generated, because the first-generated goal node may not lie on the optimal-cost path
