import heapq
# Grid (0 = free, 1 = blocked)
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]
start = (0, 0)
goal = (3, 3)
# Heuristic (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def astar():
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_cost = {start: 0}
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        x, y = current
        # neighbors (up, down, left, right)
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        for nx, ny in neighbors:
            if 0 <= nx < 4 and 0 <= ny < 4 and grid[nx][ny] == 0:
                new_g = g_cost[current] + 1
                if (nx, ny) not in g_cost or new_g < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_g
                    f = new_g + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (f, (nx, ny)))
                    came_from[(nx, ny)] = current
    return None
# Run
path = astar()
print("Shortest Path:", path)

#Output
#Shortest Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (3, 3)]
