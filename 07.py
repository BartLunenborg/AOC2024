def can_combine_to(target, nums, ops, sum=0):
    return target == sum if not nums else any(can_combine_to(target, nums[1:], ops, op(sum, nums[0])) for op in ops)

lines = (line.split(":") for line in open("./input/07.in").read().strip().split("\n"))
pairs = [(int(target), list(map(int, nums.split()))) for target, nums in lines]

ops_one = [lambda a, b: a + b, lambda a, b: a * b]
ops_two = ops_one + [lambda a, b: int(str(a) + str(b))]

one = sum(target for target, nums in pairs if can_combine_to(target, nums, ops_one))
two = sum(target for target, nums in pairs if can_combine_to(target, nums, ops_two))

print(f"Part one: {one}")
print(f"Part two: {two}")
