from collections import defaultdict

file = open("./input/01.in").read().strip()

left, right = [], []
l_counts, r_counts = defaultdict(int), defaultdict(int)

for line in file.split("\n"):
    l, r = map(int, line.split())
    left.append(l)
    right.append(r)
    l_counts[l] += 1
    r_counts[r] += 1

left.sort()
right.sort()

one = sum(abs(l - r) for l, r in zip(left, right))
two = sum(k * v * r_counts[k] for k, v in l_counts.items())

print(f"Part one: {one}")
print(f"Part one: {two}")
