from collections import defaultdict
from heapq import heappush, heappop
X, Y, KB = 70, 70, 1024

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
def solve_maze(points, start=(0, 0), end=(X, Y)):
    prevs, costs = {}, defaultdict(lambda: 1 << 31 - 1)
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

        for i in range(4):
            next = (pos[0] + dx[i], pos[1] + dy[i])
            if next not in points:  # Wall or outside grid
                continue

            if cost + 1 < costs[next]:  # New best path
                costs[next] = cost + 1
                prevs[next] = pos
                heappush(Q, (cost + 1, next))

    path, prev = set(), end
    while prev in prevs:  # Follow all previous states until we reached start
        path.add(prevs[prev])
        prev = prevs[prev]

    return costs[end], path

points = {(x, y) for y in range(Y+1) for x in range(X+1)}
input = [(int(x), int(y)) for line in open("./input/18.in").read().strip().split("\n") for x, y in [line.strip().split(",")]]

for byte in input[:KB]:
    points.remove(byte)
one, path = solve_maze(points)

two = KB  # Continue where part one ended
while path:
    two += 1
    points.remove(input[two])
    if input[two] in path:
        cost, path = solve_maze(points)
two = f"{input[two][0]},{input[two][1]}"

print(f"Part one: {one}")
print(f"Part two: {two}")
