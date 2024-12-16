from heapq import heappush, heappop
from collections import defaultdict

def find_start_end(grid):
    start, end = (0, 0), (0, 0)
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "S":  # Start
                start = (x, y, 0)
            if c == "E":  # End
                end= (x, y)
    return start, end

# For any (x, y, d), the 3 next states are (x+1, y+1, d) or (x, y, d±1). I.e. move forward or turn right/left.
def moves(state):
    x, y, d = state[0], state[1], state[2]
    return [(x + dx[d], y + dy[d], d), (x, y, (d + 1) % 4), (x, y, (d - 1) % 4)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
def solve_maze(grid):
    start, end = find_start_end(grid)
    prevs, costs = defaultdict(set), defaultdict(lambda: 2**31 - 1)
    costs[start], Q = 0, []
    heappush(Q, (0, start))  # (cost, state=(x, y, direction))
    while Q:
        cost, state = heappop(Q)
        if cost > costs[state]:  # Bad path
            continue

        if grid[state[1]][state[0]] == "E":  # Reached end
            if cost < costs[end]:  # New best path
                costs[end] = cost
                prevs[end] = {state}
            elif cost == costs[end]:  # Alternative best path
                prevs[end].add(state)
            continue

        for next in moves(state):
            if grid[next[1]][next[0]] == "#":  # Wall
                continue

            # if state[2] != next[2] we turned 90 degrees, else we moved forward
            next_cost = cost + 1000 if state[2] != next[2] else cost + 1
            if next_cost < costs[next]:  # New best path
                costs[next] = next_cost
                prevs[next] = {state}
                heappush(Q, (next_cost, next))
            elif next_cost == costs[next]:  # Alternative best path
                prevs[next].add(state)

    best_paths_tiles, queue = set(), prevs[end]
    while queue:  # Follow all previous states until we reach start
        next = set()
        for state in queue:
            best_paths_tiles.add((state[0], state[1]))
            next |= prevs[state]
        queue = next

    return costs[end], len(best_paths_tiles)

grid = [[c for c in line] for line in open("input/16.in").read().strip().split("\n")]
one, two = solve_maze(grid)

print(f"Part one: {one}")
print(f"Part two: {two}")
