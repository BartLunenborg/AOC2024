rule_memo = {}
def apply_rules(num):
    if num not in rule_memo:
        num_str = str(num)
        num_str_len = len(num_str)
        if num == 0:
            rule_memo[num] = [1]
        elif num_str_len % 2 == 0:
            rule_memo[num] = [int(num_str[num_str_len//2:]), int(num_str[:num_str_len//2])]
        else:
            rule_memo[num]  = [num * 2024]
    return rule_memo[num]

calc_memo = {}
inputs_to_str = lambda nums, blinks: "".join(str(num) + "_" for num in nums) + f"+{blinks}"
def calc_stones(nums, blinks):
    input_str = inputs_to_str(nums, blinks)
    if input_str not in calc_memo:
        calc_memo[input_str] = len(nums) if blinks == 0 else sum(calc_stones(apply_rules(num), blinks - 1) for num in nums)
    return calc_memo[input_str]

nums = [int(c) for c in open("./input/11.in").read().strip().split()]

one = calc_stones(nums, 25)
two = calc_stones(nums, 75)

print(f"Part one: {one}")
print(f"Part two: {two}")
