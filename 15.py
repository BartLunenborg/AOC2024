FREE, BOX, WALL, ROBOT = ".", "O", "#", "@"
directions = {">": 0, "v": 1, "<": 2, "^": 3}
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

class Box:
    def __init__(self, x, y):
        self.l = (x, y)  # '['
        self.r = (x + 1, y)  # ']'

    def get_dist(self):
        return 100 * self.l[1] + self.l[0]

    def can_move(self, grid, d):
        next_l = grid[self.l[1] + dy[d]][self.l[0] + dx[d]]
        if next_l != FREE and next_l != self:
            if next_l == WALL or not next_l.can_move(grid, d):
                return False

        next_r = grid[self.r[1] + dy[d]][self.r[0] + dx[d]]
        if next_r != FREE and next_r != self:
            if next_r == WALL or not next_r.can_move(grid, d):
                return False

        return True

    def move(self, grid, d):
        grid[self.l[1]][self.l[0]] = FREE
        grid[self.r[1]][self.r[0]] = FREE

        self.l = (self.l[0] + dx[d], self.l[1] + dy[d])
        self.r = (self.r[0] + dx[d], self.r[1] + dy[d])

        next_l, next_r = grid[self.l[1]][self.l[0]], grid[self.r[1]][self.r[0]]
        if next_l != FREE:
            next_l.move(grid, d)
        if next_r != FREE and next_r != next_l:
            next_r.move(grid, d)

        grid[self.l[1]][self.l[0]] = self
        grid[self.r[1]][self.r[0]] = self

def attempt_move(move, grid, x, y):
    d = directions[move]
    xd, yd = x + dx[d], y + dy[d]
    if grid[yd][xd] == FREE:
        grid[y][x], grid[yd][xd] = FREE, ROBOT
        return xd, yd
    elif grid[yd][xd] == BOX:
        xd, yd = xd + dx[d], yd + dy[d]
        while grid[yd][xd] == BOX:
            xd, yd = xd + dx[d], yd + dy[d]
        if grid[yd][xd] != WALL:
            grid[y][x], grid[yd][xd], grid[y + dy[d]][x + dx[d]] = FREE, BOX, ROBOT
            return x + dx[d], y + dy[d]
    elif grid[yd][xd] != WALL and grid[yd][xd].can_move(grid, d):
            grid[yd][xd].move(grid, d)
            grid[y][x], grid[yd][xd] = FREE, ROBOT
            return xd, yd
    return x, y

lines = [line.strip() for line in open("./input/15.in").read().strip().split("\n")]
idx = lines.index("")

grid, grid2 = [], []
x_1, y_1, x_2, y_2 = 0, 0, 0, 0
for y, line in enumerate(lines[:idx]):
    row, row2 = [], []
    for x, c in enumerate(line):
        row.append(c)
        if c == BOX:
            box = Box(2 * x, y)
            row2.extend([box, box])
        elif c == ROBOT:
            row2.extend([ROBOT, FREE])
            x_1, y_1, x_2, y_2 = x, y, 2 * x, y
        else:
            row2.extend([c, c])
    grid.append(row)
    grid2.append(row2)

for move in [c for line in lines[idx:] for c in line]:
    x_1, y_1 = attempt_move(move, grid, x_1, y_1)
    x_2, y_2 = attempt_move(move, grid2, x_2, y_2)

one = sum(100 * y + x for y, row in enumerate(grid) for x, c in enumerate(row) if c == BOX)
two = sum(box.get_dist() for box in {c for row in grid2 for c in row if isinstance(c, Box)})

print(f"Part one: {one}")
print(f"Part two: {two}")
