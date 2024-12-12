from collections import defaultdict

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
def __split(p, ps, area, seen):
    if p in ps and p not in seen:
        seen.add(p)
        area.add(p)
        for i in range(4):
            __split((p[0] + dx[i], p[1] + dy[i]), ps, area, seen)

def split(ps):
    seen, splits = set(), []
    for p in ps:
        if p not in seen:
            area = set()
            __split(p, ps, area, seen)
            splits.append(area)
    return splits

# Count corners
cs = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
def num_sides(ps):
    corners = 0
    for p in ps:
        for i in range(4):
            j = (i - 1) % 4
            a, b = (p[0] + dx[i], p[1] + dy[i]), (p[0] + dx[j], p[1] + dy[j])
            if a not in ps and b not in ps:
                corners += 1  # outer corner
            elif a in ps and b in ps and (p[0] + cs[i][0], p[1] + cs[i][1]) not in ps:
                corners += 1  # inner corner
    return corners

areas = defaultdict(list)
for y, line in enumerate(open("./input/12.in").read().strip().split("\n")):
    for x, c in enumerate(line):
        areas[c].append((x, y))

one, two = 0, 0
perimiter = lambda area: sum(sum((a[0] + dx[i], a[1] + dy[i]) not in area for i in range(4)) for a in area)
for points in areas.values():
    for area in split(points):
        l = len(area)
        one += l * perimiter(area)
        two += l * num_sides(area)


print(f"Part one: {one}")
print(f"Part two: {two}")
