# Leaf node values (example game tree)
values = [3, 5, 6, 9, 1, 2, 0, -1]

def alphabeta(depth, index, alpha, beta, isMax, path):
    
    # If leaf node reached
    if depth == 3:
        return values[index], path + [values[index]]

    if isMax:
        best_value = -float('inf')
        best_path = []

        # Left child
        val1, path1 = alphabeta(depth+1, index*2, alpha, beta, False, path + ["L"])
        if val1 > best_value:
            best_value = val1
            best_path = path1
        alpha = max(alpha, best_value)

        # Pruning condition
        if beta <= alpha:
            return best_value, best_path

        # Right child
        val2, path2 = alphabeta(depth+1, index*2+1, alpha, beta, False, path + ["R"])
        if val2 > best_value:
            best_value = val2
            best_path = path2
        alpha = max(alpha, best_value)

        return best_value, best_path

    else:
        best_value = float('inf')
        best_path = []

        # Left child
        val1, path1 = alphabeta(depth+1, index*2, alpha, beta, True, path + ["L"])
        if val1 < best_value:
            best_value = val1
            best_path = path1
        beta = min(beta, best_value)

        # Pruning condition
        if beta <= alpha:
            return best_value, best_path

        # Right child
        val2, path2 = alphabeta(depth+1, index*2+1, alpha, beta, True, path + ["R"])
        if val2 < best_value:
            best_value = val2
            best_path = path2
        beta = min(beta, best_value)

        return best_value, best_path


optimal_value, optimal_path = alphabeta(0, 0, -float('inf'), float('inf'), True, [])

print("Optimal Value:", optimal_value)
print("Optimal Path:", optimal_path)
