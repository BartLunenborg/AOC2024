from functools import cache

numdir = {
    "A": (2, 3),
    "0": (1, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
}

movedir = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}

moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
move2char = {0: ">", 1: "^", 2: "<", 3: "v"}

def find_path(a, b, dir):
    start, end, points = dir[a], dir[b], dir.values()
    shortest_strings, shortest_length = [], 1 << 31 - 1
    Q = [(start, [], "")]
    
    while Q:
        (x, y), path, string = Q.pop(0)
        l = len(string)
        if l > shortest_length:
            continue

        if (x, y) == end:
            if l < shortest_length:
                shortest_length = l
                shortest_strings = [string + "A"]
            elif l == shortest_length:
                shortest_strings.append(string + "A")
            continue

        for i, (dx, dy) in enumerate(moves):
            nx, ny = x + dx, y + dy
            if (x, y) in points and (nx, ny) not in path:
                new_path = path + [(nx, ny)]
                new_string = string + move2char[i]
                Q.append(((nx, ny), new_path, new_string))
    
    return shortest_strings

priority = {'<': 1, '^': 2, 'v': 3, '>': 4, 'A': 5}
@cache
def string_priority(s):
    return [priority[char] for char in s]

@cache
def string_turns(s):
    return sum(1 for a, b in zip(s, s[1:]) if a != b)

# How to go about picking the best string was given to me as a hint.
# First we pick the string with the fewest turns: '<vv<' over '<^>v'
# If there is a tie we prioritize '<' over '^' over '>' over '>'
@cache
def best(options):
    min_turns = min(string_turns(s) for s in options)
    options = [s for s in options if string_turns(s) == min_turns]
    return min(options, key=string_priority)

@cache
def translate(xs):
    return [find_path(a, b, movedir) for a, b in zip("A" + xs, xs)]

@cache
def __code_len(x, robots):
    if robots == 0:
        return len(x)
    xs = [best(tuple(y)) for y in translate(x)]
    return sum(__code_len(x, robots - 1) for x in xs)

def code_len(code, robots):
    xs = [best(tuple(x)) for x in [find_path(a, b, numdir) for a, b in zip("A" + code, code)]]
    return sum(__code_len(x, robots) for x in xs)

codes = [line.strip() for line in open("./input/21.in").read().strip().split("\n")]

sequences = [code_len(code, 2) for code in codes]
one = sum(int(code[:3]) * sequence for code, sequence in zip(codes, sequences))

sequences = [code_len(code, 25) for code in codes]
two = sum(int(code[:3]) * sequence for code, sequence in zip(codes, sequences))

print(f"Part one: {one}")
print(f"Part two: {two}")
