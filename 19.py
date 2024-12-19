from functools import cache  # cache OP again

@cache
def ways_to_make(t):
    return 1 if t == "" else sum(ways_to_make(t.removeprefix(p)) for p in ps if t.startswith(p))

ls = [l.strip() for l in open("./input/19.in").read().strip().split("\n")]
i = ls.index("")  # ps = patterns, ts = targets
ps, ts = [p.strip() for l in ls[:i] for p in l.split(",")], [t for t in ls[i+1:]]

ts_ways = [ways_to_make(t) for t in ts]
one = ts_ways.count(0)
two = sum(ts_ways)

print(f"Part one: {one}")
print(f"Part two: {two}")
