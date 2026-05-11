from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited_dfs = set()

def dfs(node):
    if node not in visited_dfs:
        print(node, end=" ")
        visited_dfs.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

def bfs(start):
    visited_bfs = set()
    queue = deque([start])
    visited_bfs.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited_bfs:
                visited_bfs.add(neighbor)
                queue.append(neighbor)

print("DFS Traversal:")
dfs('A')
print("\nBFS Traversal:")
bfs('A')

#Output
#PS C:\Users\user> & C:/Users/user/anaconda3/python.exe e:/AI/P1.py
#DFS Traversal:
#A B D E F C 
#BFS Traversal:
##A B C D E F
