def is_valid(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, assignment={}):
    if len(assignment) == len(graph):
        return assignment
    
    unassigned = [node for node in graph if node not in assignment][0]
    
    for color in colors:
        if is_valid(unassigned, color, assignment, graph):
            assignment[unassigned] = color
            result = map_coloring(graph, colors, assignment)
            if result:
                return result
            del assignment[unassigned]
    return None

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

colors = ['Red', 'Green', 'Blue']

solution = map_coloring(graph, colors)
print("Color Assignment:", solution)
