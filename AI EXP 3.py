from collections import deque
A = 4
B = 3
goal = (2, 0)

def water_jug():
    visited = set()
    queue = deque([(0, 0, [])])

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        path = path + [(x, y)]

        # ✅ Stop only when (2,0) reached
        if (x, y) == goal:
            return path

        states = [
            (A, y),  # Fill A
            (x, B),  # Fill B
            (0, y),  # Empty A
            (x, 0),  # Empty B
            (x - min(x, B - y), y + min(x, B - y)),  # A -> B
            (x + min(y, A - x), y - min(y, A - x))   # B -> A
        ]

        for s in states:
            queue.append((s[0], s[1], path))

solution = water_jug()

print("Steps to reach (2,0):\n")
for step in solution:
    print(step)
