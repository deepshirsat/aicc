import heapq
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
def dijkstra(start):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    while pq:
        current_dist, node = heapq.heappop(pq)
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist
print("Shortest distances:", dijkstra('A'))


#Output
# Shortest distances: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
