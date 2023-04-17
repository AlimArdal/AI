from queue import PriorityQueue

graph = {
    'S': [('A', 2), ('B', 3), ('D', 5)],
    'A': [('S', 2), ('C', 4)],
    'B': [('S', 3), ('D', 4)],
    'C': [('A', 4), ('D', 1), ('G', 2)],
    'D': [('S', 5), ('B', 5), ('C', 1), ('G', 5)],
}

heuristics = {
    'A': 2,
    'B': 5,
    'C': 2,
    'D': 1,
    'G': 0
}

def a_star(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, [start]))
    while not queue.empty():
        (cost, path) = queue.get()
        node = path[-1]
        if node not in visited:
            visited.add(node)
            print(f"Visited: {node}")
            if node == goal:
                return path
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_cost = cost + weight + heuristics[neighbor]
                    new_path = path + [neighbor]
                    queue.put((new_cost, new_path))

print("\n---------------------------------------------------------------------------------")
print("Visited nodes with A* algorithm:")
path = a_star(graph, 'S', 'G')
print(path)
print("\n---------------------------------------------------------------------------------")