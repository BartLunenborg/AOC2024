from z3 import Optimize, Ints, sat
TWO = 10000000000000

def button(button):
    l, r = button.split(",")
    return (int(l.split("+")[1]), int(r.split("+")[1]))

def prize(prize):
    l, r = prize.split(",")
    return (int(l.split("=")[1]), int(r.split("=")[1]))

def find_min(machines):
    total = 0
    for m in machines:
        x, y = Ints('x y')
        o = Optimize()
        o.add(m[0][0] * x + m[1][0] * y == m[2][0])  # x direction
        o.add(m[0][1] * x + m[1][1] * y == m[2][1])  # y direction
        cost = 3 * x + y
        o.minimize(cost)
        if o.check() == sat:
            total += o.model()[x].as_long() * 3 + o.model()[y].as_long()
    return total

file = open("./input/13.in").read().strip().split("\n")
lines = [line.strip() for line in file if line.strip() != ""]
machines = [(button(lines[i]), button(lines[i+1]), prize(lines[i+2])) for i in range(0, len(lines), 3)]

one = find_min(machines)
two = find_min([(m[0], m[1], (m[2][0] + TWO, m[2][1] + TWO)) for m in machines])

print(f"Part one: {one}")
print(f"Part two: {two}")
