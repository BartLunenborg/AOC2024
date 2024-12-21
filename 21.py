MAX = 1 << 31 - 1

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
    shortest_strings, shortest_length = [], 10
    Q = [(start, [], "")]
    
    while Q:
        (x, y), path, string = Q.pop(0)
        if (x, y) == end:
            if len(string) < shortest_length:
                shortest_length = len(string)
                shortest_strings = [string + "A"]
            elif len(string) == shortest_length:
                shortest_strings.append(string + "A")
            continue

        if len(string) > shortest_length:
            continue
        
        for i, (dx, dy) in enumerate(moves):
            nx, ny = x + dx, y + dy
            
            if (x, y) in points and (nx, ny) not in path:
                new_path = path + [(nx, ny)]
                new_string = string + move2char[i]
                
                if (nx, ny) == end:
                    if len(new_string) < shortest_length:
                        shortest_length = len(new_string)
                        shortest_strings = [new_string + "A"]
                    elif len(new_string) == shortest_length:
                        shortest_strings.append(new_string + "A")
                else:
                    Q.append(((nx, ny), new_path, new_string))
    
    return shortest_strings

def translate(xs):
    ys, y_min = [], MAX
    for x in xs:
        string = [find_path(a, b, movedir) for a, b in zip("A" + x, x)]
        y_min = min(y_min, len(string))
        ys.append(string)
    ys = [y for y in ys if len(y) == y_min]
    return ys

def find_sequence(code):
    a = [find_path(a, b, numdir) for a, b in zip("A" + code, code)]
    a = [translate(tuple(xs)) for xs in a]

    complexity = 0
    for xsss in a:
        xss_min = MAX
        for xss in xsss:
            xss_trans = [translate(tuple(xs)) for xs in xss]
            xss_min = min(xss_min, sum(min(sum(len(y[0]) for y in ys) for ys in yss) for yss in xss_trans))
        complexity += xss_min

    return complexity

codes = [line.strip() for line in open("./input/21.in").read().strip().split("\n")]

sequences = [find_sequence(code) for code in codes]
one = sum(int(code[:3]) * sequence for code, sequence in zip(codes, sequences))
print(f"Part one: {one}")
