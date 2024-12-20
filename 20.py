from collections import defaultdict
from heapq import heappush, heappop

# Find all points that are within Manhattan distance d from point p
def points_within_dist(p, d):
    ps = set()
    for y in range(p[1] - d, p[1] + d + 1):
        x_max = d - abs(y - p[1])
        for x in range(p[0] - x_max, p[0] + x_max + 1):
            ps.add((x, y))
    return ps

# Finds all costs on the shortest path and returns all these costs as well as the path
def find_path_all_costs(ps, start, end):
    costs, prevs = defaultdict(lambda: 1 << 31 - 1), {}
    costs[start], Q = 0, []
    heappush(Q, (0, start))  # (cost, position=(x, y))
    while Q:
        cost, pos = heappop(Q)
        if cost > costs[pos]:  # Bad path
            continue

        if pos == end:
            if cost < costs[end]:  # New best path
                costs[end] = cost
                prevs[end] = pos
            continue
        
        for next in points_within_dist(pos, 1):
            if next not in ps:  # Wall or outside grid
                continue

            if cost + 1 < costs[next]:  # New best path
                costs[next] = cost + 1
                prevs[next] = pos
                heappush(Q, (cost + 1, next))

    path, prev = {end}, end
    while prev in prevs:  # Follow all previous states until we reached start
        path.add(prevs[prev])
        prev = prevs[prev]

    return costs, path

# Finds the cost of the shortest path from a to b
def cheapest_path(ps, start, end):
    costs = defaultdict(lambda: 1 << 31 - 1)
    costs[start], Q = 0, []
    heappush(Q, (0, start))  # (cost, position=(x, y))
    while Q:
        cost, pos = heappop(Q)
        if cost > costs[pos]:  # Bad path
            continue

        if pos == end:
            if cost < costs[end]:  # New best path
                costs[end] = cost
            continue

        for next in points_within_dist(pos, 1):
            if next not in ps:  # Wall or outside grid
                continue

            if cost + 1 < costs[next]:  # New best path
                costs[next] = cost + 1
                heappush(Q, (cost + 1, next))

    return costs[end]

# Manhattan distance from a to b
dist = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

def cheaty_paths(ps, start, end):
    # Cheapest costs and path without cheating, solved from end to start for later calculations
    costs, path = find_path_all_costs(ps, end, start)

    one, two = 0, 0
    for p in path:
        for m in points_within_dist(p, 20):  # We will check if taking a cheat results in time saved
            if m not in ps:  # Outside grid or a wall
                continue

            if m in path:
                cheat_cost = costs[m]
            else:
                cheat_cost = cheapest_path(ps, m, end)

            cheat_dist = dist(m, p)  # How many 'picoseconds' we cheated
            save = costs[p] - (cheat_cost + cheat_dist)
            if save >= 100:
                one += 1 if cheat_dist == 2 else 0
                two += 1

    return one, two

lines = [line.strip() for line in open("./input/20.in").read().strip().split("\n")]
start, end, points = (0, 0), (0, 0), set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == ".":
            points.add((x, y))
        elif c == "S":
            points.add((x, y))
            start = (x, y)
        elif c == "E":
            points.add((x, y))
            end = ((x, y))

one, two = cheaty_paths(points, start, end)

print(f"Part one: {one}")
print(f"Part two: {two}")
