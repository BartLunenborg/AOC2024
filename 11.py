from functools import cache  # cache to the rescue! (low-key op)

@cache
def apply_rules(num):
    if num == 0:
        return (1,)
    num_str = str(num)
    length = len(num_str)
    if length % 2 == 0:
        return (int(num_str[length//2:]), int(num_str[:length//2]))
    return (num * 2024,)

@cache
def calc_stones(nums, blinks):
    if blinks == 0:
        return len(nums)
    return sum(calc_stones(apply_rules(num), blinks - 1) for num in nums)

# Parse input as tuple to work with cache
nums = tuple(int(c) for c in open("./input/11.in").read().strip().split())

one = calc_stones(nums, 25)
two = calc_stones(nums, 75)

print(f"Part one: {one}")
print(f"Part two: {two}")
