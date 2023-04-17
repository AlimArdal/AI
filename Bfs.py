graph = {
  'S' : ['A','B','D'],
  'A' : ['C'],
  'B' : ['D'],
  'C' : ['D','G'],
  'D' : ['G'],
  'G' : []
}

def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

print("\n---------------------------------------------------------------------------------\n")
path = bfs(graph, 'S', 'G')
print('Shortest path with BFS algorithm: ')
print(path)
print("\n---------------------------------------------------------------------------------")