from collections import deque

# The target state we want to achieve
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_neighbors(state):
    """Generates all possible moves from the current state."""
    neighbors = []
    idx = state.index(0)  # Find the empty space (0)
    row, col = divmod(idx, 3)

    # Possible movements: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            new_state = list(state)
            # Swap empty space with the number at the new position
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

def solve_bfs(start_state):
    """Uses Breadth-First Search to find the shortest path to the goal."""
    # Queue stores (current_state, path_to_this_state)
    queue = deque([(start_state, [])])
    visited = {start_state}

    while queue:
        current_state, path = queue.popleft()

        if current_state == GOAL_STATE:
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current_state]))
    return None

def print_grid(state):
    """Prints the puzzle state in a 3x3 format."""
    for i in range(0, 9, 3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
    print("-" * 6)

# --- User Input Section ---
print("Enter your 8-puzzle row by row (use 0 for blank space):")
user_input = []
try:
    for i in range(3):
        # Take input like '238' or '2 3 8'
        row = input(f"Row {i+1}: ").strip()
        # Clean the input to get individual digits
        if len(row) > 3: # If user used spaces
            user_input.extend([int(x) for x in row.split()])
        else: # If user entered numbers together like 238
            user_input.extend([int(x) for x in row])

    start_node = tuple(user_input)

    print("\nSearching for solution...\n")
    solution_path = solve_bfs(start_node)

    if solution_path:
        print(f"Success! Found solution in {len(solution_path)-1} moves.\n")
        print("Path to follow:")
        for step_count, state in enumerate(solution_path):
            print(f"Step {step_count}:")
            print_grid(state)
    else:
        print("No solution exists for this input.")
except Exception as e:
    print("Invalid Input! Please enter numbers from 0-8 correctly.")