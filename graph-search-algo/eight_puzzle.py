from collections import deque

# State representation: 1D tuple of length 9 (0 represents the blank space)
INITIAL_STATE = (2, 8, 3,
                 1, 6, 4,
                 7, 0, 5)

GOAL_STATE    = (1, 2, 3,
                 8, 0, 4,
                 7, 6, 5)

def get_neighbors(state):
    """Generates all valid next states by moving the blank tile (0)."""
    neighbors = []
    zero_idx = state.index(0)
    row, col = zero_idx // 3, zero_idx % 3

    # Legal movements: (row_offset, col_offset)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero_idx = nr * 3 + nc
            # Convert tuple to list to swap elements
            state_list = list(state)
            state_list[zero_idx], state_list[new_zero_idx] = state_list[new_zero_idx], state_list[zero_idx]
            neighbors.append(tuple(state_list))

    return neighbors

def solve_8_puzzle_bfs(start_state, goal_state):
    """Solves 8-puzzle using BFS and returns the shortest sequence of states."""
    queue = deque([[start_state]])
    visited = {start_state}

    while queue:
        path = queue.popleft()
        current_state = path[-1]

        if current_state == goal_state:
            return path

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None

def print_grid(state):
    """Pretty prints a single 3x3 state."""
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else "_" for x in state[i:i+3]]
        print(" ".join(row))

if __name__ == "__main__":
    path = solve_8_puzzle_bfs(INITIAL_STATE, GOAL_STATE)

    if path:
        print(f"Goal reached in {len(path) - 1} moves!\n")
        for step, state in enumerate(path):
            print(f"Step {step}:")
            print_grid(state)
            print()
    else:
        print("No solution found.")
