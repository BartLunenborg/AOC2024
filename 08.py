from collections import defaultdict

file = open("./input/08.in").read().strip()
grid = {(x, y): c for y, line in enumerate(file.split("\n")) for x, c in enumerate(line)}

antennas = defaultdict(list)
for k, v in grid.items():
    if v != ".":
        antennas[v].append((k[0], k[1]))

sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
add = lambda a, b: (a[0] + b[0], a[1] + b[1])
delta = lambda a, b: (b[0] - a[0], b[1] - a[1])

one, two = set(), set()
for v in antennas.values():
    for i, a in enumerate(v):
        two.add(a)
        for b in v[i+1:]:
            d = delta(a, b)
            p_0, p_1 = sub(a, d), add(b, d)
            one.update(p for p in [p_0, p_1] if p in grid)
            while p_0 in grid:
                two.add(p_0)
                p_0 = sub(p_0, d)
            while p_1 in grid:
                two.add(p_1)
                p_1 = add(p_1, d)

print(f"Part one: {len(one)}")
print(f"Part two: {len(two)}")
