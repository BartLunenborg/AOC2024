from copy import deepcopy

file = open("./input/06.in").read().strip()
map = [[c for c in line] for line in file.split("\n")]

# max of x and y; 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT
X, Y = len(map[0]), len(map)
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

# get x and y of '^' and mark as visited
x_0, y_0 = next((x, y) for y, row in enumerate(map) for x, c in enumerate(row) if c == "^")
map[y_0][x_0] = "X"

# Draws the path of guard, returns map and whether the path has a loop
def draw_path(map, d=0):  # Our direction 'd' always start looking UP
    memo = {(x_0, y_0, d)}
    x, y = x_0 + dx[d], y_0 + dy[d]
    while 0 <= x < X and 0 <= y < Y:  # We remain inside the grid
        if (x, y, d) in memo:  # We are in a loop
            return map, True
        if map[y][x] == "#":  # We encounter an obstacle
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

# Not super fast, but it works
two = sum(path_has_loop(x, y) for y, row in enumerate(path_map) for x, c in enumerate(row) if c == "X" and (x, y) != (x_0, y_0))

print(f"Part one: {one}")
print(f"Part two: {two}")
