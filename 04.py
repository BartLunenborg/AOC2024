file = open("./input/04.in").read().strip()
grid = [[c for c in line] for line in file.split("\n")]

Y = len(grid)
X = len(grid[0])

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def is_at(x, y, d):
    if (x + 3 * dx[d] < 0 or x + 3 * dx[d] >= X or y + 3 * dy[d] < 0 or y + 3 * dy[d] >= Y):
        return False
    return "".join(grid[y + i * dy[d]][x + i * dx[d]] for i in range(4)) == "XMAS"

one = sum( is_at(x, y, d) for y in range(Y) for x in range(X) for d in range(8) if grid[y][x] == "X")

xmas = lambda x, y: grid[y-1][x-1] + grid[y+1][x+1] in ["MS", "SM"] and grid[y-1][x+1] + grid[y+1][x-1] in ["MS", "SM"]
two = sum( xmas(x, y) for y in range(1, Y-1) for x in range(1, X-1) if grid[y][x] == "A")

print(f"Part one: {one}")
print(f"Part one: {two}")
