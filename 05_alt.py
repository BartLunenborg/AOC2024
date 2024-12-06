from collections import defaultdict
from functools import cmp_to_key

file = open("./input/05.in").read().strip()
lines = [line for line in file.split("\n")]
split = lines.index("")

rules = defaultdict(list)
for line in lines[:split]:
    a, b = map(int, line.split("|"))
    rules[a].append(b)

one, two = 0, 0
good_ordering = lambda before, rules: all(rule not in before for rule in rules)
for line in lines[split+1:]:
    nums = list(map(int, line.split(",")))
    if all(good_ordering(nums[:i], rules[num]) for i, num in enumerate(nums) if num in rules):
        one += nums[len(nums)//2]
    else:
        two += sorted(nums, key=cmp_to_key(lambda a, b: 1 if b in rules[a] else -1))[len(nums)//2]

print(f"Part one: {one}")
print(f"Part two: {two}")
