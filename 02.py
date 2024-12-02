file = open("./input/02.in").read().strip()

def is_safe(nums):
    decreasing = nums[1] < nums[0]
    for prev, curr in zip(nums, nums[1:]):
        diff = curr - prev
        if not (1 <= abs(diff) <= 3) or not (diff < 0) == decreasing:
            return False
    return True

lines = [list(map(int, line.split())) for line in file.split("\n")]
one = sum(is_safe(nums) for nums in lines)
two = sum(any((is_safe(sub) for sub in (nums[:i]+nums[i+1:] for i in range(len(nums))))) for nums in lines)

print(f"Part one: {one}")
print(f"Part one: {two}")
