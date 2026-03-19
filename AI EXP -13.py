# Leaf node values (game tree values)
values = [3, 5, 2, 9, 12, 5, 23, 23]

def minimax(depth, index, isMax, path):
    
    # If leaf node reached
    if depth == 3:
        return values[index], path + [values[index]]

    if isMax:
        best_value = -float('inf')
        best_path = []

        # Left child
        val1, path1 = minimax(depth+1, index*2, False, path + ["L"])
        # Right child
        val2, path2 = minimax(depth+1, index*2+1, False, path + ["R"])

        if val1 > val2:
            best_value = val1
            best_path = path1
        else:
            best_value = val2
            best_path = path2

        return best_value, best_path

    else:
        best_value = float('inf')
        best_path = []

        # Left child
        val1, path1 = minimax(depth+1, index*2, True, path + ["L"])
        # Right child
        val2, path2 = minimax(depth+1, index*2+1, True, path + ["R"])

        if val1 < val2:
            best_value = val1
            best_path = path1
        else:
            best_value = val2
            best_path = path2

        return best_value, best_path


optimal_value, optimal_path = minimax(0, 0, True, [])

print("Optimal Value:", optimal_value)
print("Optimal Path:", optimal_path)
