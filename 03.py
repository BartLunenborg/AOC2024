import re
def calc_matches(line):
    sum = 0
    for m in re.findall(r'mul\(\d\d?\d?,\d\d?\d?\)', line):
        a, b = m.split(",")
        sum += int(a[4:]) * int(b[:-1])
    return sum

line = open("./input/03.in").read().strip().replace("\n", "")

one = calc_matches(line)

line = re.sub(r'don\'t\(\).*?do\(\)', "", line)
line = re.sub(r'don\'t\(\).*?$', "", line)
two = calc_matches(line)

print(f"Part one: {one}")
print(f"Part two: {two}")
