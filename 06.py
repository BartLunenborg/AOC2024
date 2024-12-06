from copy import deepcopy

file = open("./input/06.in").read().strip()
map = [[c for c in line] for line in file.split("\n")]

# max of x and y
X, Y = len(map[0]), len(map)

# mark x and y of '^' as visited and save coords
start_x, start_y = 0, 0
for y, row in enumerate(map):
    for x, c in enumerate(row):
        if c == "^":
            start_x, start_y = x, y
            map[start_y][start_x] = "X"  # Mark as visited

# 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# Draws the path of guard, returns path and whether the path has a loop
def draw_path(map, d=0):
    memo = {(start_x, start_y, d)}
    x, y = start_x + dx[d], start_y + dy[d]
    while 0 <= x < X and 0 <= y < Y:  # We remain inside the grid
        if (x, y, d) in memo:  # We are in a loop
            return map, True
        if map[y][x] == "#":  # we encounter an obstacle
            x, y = x - dx[d], y - dy[d]
            d = (d + 1) % 4
        else:  # We encounter an empty space
            map[y][x] = "X"
            memo.add((x, y, d))
        x, y = x + dx[d], y + dy[d]
    return map, False

# Check if path has loop after placing '#' at x, y
def path_has_loop(x, y):
    candidate = deepcopy(map)
    candidate[y][x] = "#"
    return draw_path(candidate)[1]

path_map = draw_path(deepcopy(map))[0]
one = sum(c == "X" for row in path_map for c in row)

# Not super fast, but it works (map[y][x] == "X" checks for start position i.e. '^')
two = sum(path_has_loop(x, y) for y, row in enumerate(path_map) for x, c in enumerate(row) if c == "X" and not map[y][x] == "X")

print(f"Part one: {one}")
print(f"Part two: {two}")
