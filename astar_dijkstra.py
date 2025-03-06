import heapq

def astar(grid, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next in neighbors(grid, current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    return came_from, cost_so_far

def neighbors(grid, node):
    x, y = node
    result = []
    for new_position in [(0, -1), (1, 0), (0, 1), (-1, 0)]:  # left, down, right, up
        x2, y2 = x + new_position[0], y + new_position[1]
        if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] != '#':
            result.append((x2, y2))
    return result

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def print_path(grid, came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    for x, y in path:
        grid[x][y] = '*'

    for row in grid:
        print(''.join(row))

# Labyrinthe de gauche
grid_left = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'c'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', 'x', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

start_left = (6, 2)
goal_left = (0, 9)

came_from_left, cost_so_far_left = astar(grid_left, start_left, goal_left)
print("A* sur le labyrinthe de gauche:")
print_path(grid_left, came_from_left, start_left, goal_left)

def dijkstra(grid, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next in neighbors(grid, current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heapq.heappush(frontier, (new_cost, next))
                came_from[next] = current

    return came_from, cost_so_far

# Labyrinthe de droite
grid_right = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'c'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', 'x', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

start_right = (6, 2)
goal_right = (0, 9)

came_from_right, cost_so_far_right = dijkstra(grid_right, start_right, goal_right)
print("Dijkstra sur le labyrinthe de droite:")
print_path(grid_right, came_from_right, start_right, goal_right)
