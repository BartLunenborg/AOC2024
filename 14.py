from math import prod

X, Y = 101, 103  # Stated in problem

def parse_line(line):
    l, r = line.split()  # ['p=x,y', 'v=x,y']
    ll, lr = l.split(",")  # ['p=x', 'y']
    rl, rr = r.split(",")  # ['v=x', 'y']
    return ((int(ll.split("=")[1]), int(lr)), (int(rl.split("=")[1]), int(rr)))  # ((x_p, y_p), (x_v, y_v))

def sim_bots(bots):
    for i, bot in enumerate(bots):
        bots[i] = (((bot[0][0] + bot[1][0]) % X, (bot[0][1] + bot[1][1]) % Y), bot[1])

# The Christmas tree only seems to appear when no bots overlap (not my initial way to find the tree)
def overlap(bots, num_bots):
    return len({(bot[0][0], bot[0][1]) for bot in bots}) != num_bots

file = open("./input/14.in").read().strip()
bots = [parse_line(line) for line in file.split("\n")]

for _ in range(100):
    sim_bots(bots)

corners = 4 * [0]  # top-left, top-right, bottom-right, bottom-left
mid_x, mid_y = X // 2, Y // 2
for b in bots:
    if b[0][0] != mid_x and b[0][1] != mid_y:
        corners[(b[0][0] > mid_x) + 2 * (b[0][1] > mid_y)] += 1
one = prod(corners)

two = 100  # We continue where part one left off
num_bots = len(bots)
while overlap(bots, num_bots):
    sim_bots(bots)
    two += 1
print("\n".join("".join("*" if (x, y) in {(bot[0][0], bot[0][1]) for bot in bots} else " " for x in range(X)) for y in range(Y)))

print(f"Part one: {one}")
print(f"Part two: {two}")
