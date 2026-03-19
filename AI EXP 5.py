from collections import deque

def is_valid(state):
    M_left, C_left, _ = state
    M_right = 3 - M_left
    C_right = 3 - C_left

    if M_left < 0 or C_left < 0 or M_left > 3 or C_left > 3:
        return False

    if M_left > 0 and C_left > M_left:
        return False

    if M_right > 0 and C_right > M_right:
        return False

    return True


def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        (M_left, C_left, boat), path = queue.popleft()

        if (M_left, C_left, boat) == goal:
            return path

        for M_move, C_move in moves:
            if boat == 1:
                new_state = (M_left - M_move, C_left - C_move, 0)
            else:
                new_state = (M_left + M_move, C_left + C_move, 1)

            if is_valid(new_state) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None


solution = bfs()

if solution:
    print("Solution Found!\n")
    for step in solution:
        M_left, C_left, boat = step
        side = "Left" if boat == 1 else "Right"
        print("Missionaries Left:", M_left,
              "Cannibals Left:", C_left,
              "Boat on:", side)
else:
    print("No solution found.")
