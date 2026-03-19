import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    
    parent = {}
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]
        
        for neighbor, cost in graph[current]:
            new_cost = g_cost[current] + cost
            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current
    return None

# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {'A': 3, 'B': 1, 'C': 1, 'D': 0}

path = a_star(graph, 'A', 'D', heuristic)
print("Shortest Path:", path)
