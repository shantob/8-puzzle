from collections import deque
# deque হলো একটি বিশেষ ধরণের লিস্ট যা থেকে খুব দ্রুত ডাটা বের করা যায়। 
# এটি BFS অ্যালগরিদমে Queue হিসেবে ব্যবহার করা হয়েছে।

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
# এটি আমাদের টার্গেট। আমরা চাই পাজলটি এভাবে সাজানো থাকুক। ০ মানে খালি ঘর।



def get_neighbors(state):
    neighbors = []
    idx = state.index(0)  # খালি ঘর (০) এর পজিশন খুঁজে বের করে।
    row, col = divmod(idx, 3) # ইনডেক্সকে ৩x৩ গ্রিডের রো এবং কলামে ভাগ করে।

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # উপরে, নিচে, বামে, ডানে মুভ।

    for dr, dc in moves:
        r, c = row + dr, col + dc # নতুন সম্ভাব্য রো এবং কলাম।
        if 0 <= r < 3 and 0 <= c < 3: # চেক করে মুভটি গ্রিডের ভেতরে আছে কি না।
            new_idx = r * 3 + c # গ্রিড পজিশনকে আবার ইনডেক্সে রূপান্তর।
            new_state = list(state)
            # খালি ঘর (০) এবং পাশের সংখ্যার মধ্যে জায়গা অদলবদল (Swap) করে।
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state)) # নতুন অবস্থাটি লিস্টে যোগ করে।
    return neighbors




    def solve_bfs(start_state):
    # কিউতে (Queue) বর্তমান অবস্থা এবং আসার পথ (path) জমা রাখা হয়।
    queue = deque([(start_state, [])])
    visited = {start_state} # আগে যে অবস্থাগুলো চেক করা হয়েছে তা মনে রাখে।

    while queue:
        current_state, path = queue.popleft() # কিউ থেকে প্রথম অবস্থাটি নেয়।

        if current_state == GOAL_STATE: # যদি লক্ষ্যের সাথে মিলে যায়।
            return path + [current_state] # পুরো পথটি রিটার্ন করে।

        for neighbor in get_neighbors(current_state): # আশেপাশের সব মুভ চেক করে।
            if neighbor not in visited: # যদি এই মুভটি আগে চেক করা না হয়।
                visited.add(neighbor)
                queue.append((neighbor, path + [current_state])) # কিউতে যোগ করে।
    return None # সমাধান না পাওয়া গেলে।


    def print_grid(state):
    # ৯টি সংখ্যার লিস্টকে ৩টি করে লাইনে প্রিন্ট করে যাতে ৩x৩ গ্রিড দেখায়।
    for i in range(0, 9, 3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
    print("-" * 6)




    print("Enter your 8-puzzle row by row (use 0 for blank space):")
user_input = []
try:
    for i in range(3):
        row = input(f"Row {i+1}: ").strip() # ইউজারের কাছ থেকে প্রতি লাইন ইনপুট নেয়।
        if len(row) > 3: # যদি স্পেস দিয়ে লিখে।
            user_input.extend([int(x) for x in row.split()])
        else: # যদি সরাসরি লিখে যেমন '238'
            user_input.extend([int(x) for x in row])

    start_node = tuple(user_input) # ইনপুটকে টাপল-এ রূপান্তর করে।

    print("\nSearching for solution...\n")
    solution_path = solve_bfs(start_node) # সমাধান খোঁজা শুরু।

    if solution_path:
        print(f"Success! Found solution in {len(solution_path)-1} moves.\n")
        for step_count, state in enumerate(solution_path):
            print(f"Step {step_count}:") # প্রতিটি ধাপের সিরিয়াল দেখায়।
            print_grid(state) # সেই ধাপের গ্রিড প্রিন্ট করে।
    else:
        print("No solution exists for this input.")
except Exception as e:
    print("Invalid Input! Please enter numbers from 0-8 correctly.")


    
