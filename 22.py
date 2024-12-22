from collections import defaultdict

two_dict = defaultdict(int)

def next_num(num):
    num = num ^ num * 64 % 16777216
    num = num ^ num // 32 % 16777216
    return num ^ num * 2048 % 16777216

def sim(num):
    nums = [num]
    for i in range(2000):
        nums.append(next_num(nums[i]))

    seen = set()
    changes = [b % 10 - a % 10 for a, b in zip(nums, nums[1:])]
    for i in range(2001 - 4):
        change = tuple(changes[i:i+4])
        if change not in seen:
            seen.add(change)
            two_dict[change] += nums[i+4] % 10

    return nums[2000]

one = sum(sim(num) for num in [int(num) for num in open("input/22.in").read().strip().split("\n")])
two = max(v for v in two_dict.values())

print(f"Part one: {one}")
print(f"Part two: {two}")
