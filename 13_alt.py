ADD = 10000000000000

def button(button):
    l, r = button.split(",")
    return (int(l.split("+")[1]), int(r.split("+")[1]))

def prize(prize):
    l, r = prize.split(",")
    return (int(l.split("=")[1]), int(r.split("=")[1]))

# Use Cramer's rule to solve, assuming the determinant is never 0. See chapter 9.8 of:
# https://math.libretexts.org/Bookshelves/Precalculus/Precalculus_1e_(OpenStax)/09%3A_Systems_of_Equations_and_Inequalities
def solve(m, add=0):
    x, y = m[2][0] + add, m[2][1] + add
    a_x, a_y, b_x, b_y = m[0][0], m[0][1], m[1][0], m[1][1]

    det = a_x * b_y - b_x * a_y
    det_x, det_y = x * b_y - y * b_x,  a_x * y - a_y * x
    a, b = det_x / det, det_y / det

    return int(3 * a + b) if a == int(a) and b == int(b) else 0

file = open("./input/13.in").read().strip().split("\n")
lines = [line.strip() for line in file if line.strip() != ""]
machines = [(button(lines[i]), button(lines[i+1]), prize(lines[i+2])) for i in range(0, len(lines), 3)]
one, two = sum(solve(m) for m in machines), sum(solve(m, ADD) for m in machines)

print(f"Part one: {one}")
print(f"Part two: {two}")
