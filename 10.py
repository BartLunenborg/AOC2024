SEEN, START, END = True, 0, 9

file = open("./input/10.in").read().strip()
GRID = [[int(n) for n in line] for line in file.split("\n")]
X, Y = len(GRID[0]), len(GRID)
POINTS, MEMO = {(x, y) for x in range(X) for y in range(Y)}, [[(0, not SEEN) for _ in range(X)] for _ in range(Y)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
def trail_score_one(x, y, nines, seen, slope=0):
    if (x, y) not in POINTS or GRID[y][x] != slope or (x, y) in seen:
        return nines
    seen.add((x, y))
    if slope == END:
        nines.add((x, y))
        return nines
    for i in range(4):
        trail_score_one(x + dx[i], y + dy[i], nines, seen, slope + 1)
    return nines

def trail_score_two(x, y, slope=0):
    if (x, y) not in POINTS or GRID[y][x] != slope:
        return 0
    if MEMO[y][x][1] == SEEN:
        return MEMO[y][x][0]
    if slope == END:
        return 1
    total = sum(trail_score_two(x + dx[i], y + dy[i], slope + 1) for i in range(4))
    MEMO[y][x] = (total, SEEN)
    return total

one = sum(len(trail_score_one(x, y, set(), set())) for y in range(Y) for x in range(X) if GRID[y][x] == START)
two = sum(trail_score_two(x, y) for y in range(Y) for x in range(X) if GRID[y][x] == START)

print(f"Part one: {one}")
print(f"Part two: {two}")
