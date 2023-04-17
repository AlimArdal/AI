graph = {
  'S' : ['A','B','D'],
  'A' : ['C'],
  'B' : ['D'],
  'C' : ['D','G'],
  'D' : ['G'],
  'G' : []
}

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    visited.add(start)
    print(f"Visited: {start}")
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited, path + [neighbor])
            if new_path:
                return new_path

print("\n---------------------------------------------------------------------------------\n")
path = dfs(graph, 'S', 'G')
print('Shortest path with DFS algorithm: ')
print(path)
print("\n---------------------------------------------------------------------------------")