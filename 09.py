nums = open("./input/09.in").read().strip()
SEEN, NOT_SEEN, EMPTY, = True, False, -1

def move_one(disk):
    front, back = 0, len(disk) - 1
    while front < back:
        while disk[front] != EMPTY:
            front += 1
        while disk[back] == EMPTY:
            back -= 1
        if front < back:
            disk[front], disk[back] = disk[back], disk[front]
    return disk

def __move_two(disk, old_i):
    n, new_i = disk[old_i][1], 1
    while new_i < old_i and (disk[new_i][0] != EMPTY or disk[new_i][1] < n):
        new_i += 1
    if new_i < old_i:
        if disk[new_i][1] > n:
            disk.insert(new_i + 1, (EMPTY, disk[new_i][1] - n, NOT_SEEN))
            old_i += 1
        disk[new_i], disk[old_i] = (disk[old_i][0], n, SEEN), (EMPTY, n, NOT_SEEN)
    else:
        disk[old_i] = (disk[old_i][0], n, SEEN)

def move_two(disk):
    i = len(disk) - 1
    for _ in range(len(disk) // 2):
        while disk[i][0] == EMPTY or disk[i][2] == SEEN:
            i -= 1
        __move_two(disk, i)
    return disk

disk = [(i//2, int(c), NOT_SEEN) if i % 2 == 0 else (EMPTY, int(c), NOT_SEEN) for i, c in enumerate(nums)]
one = sum(i * n for i, n in enumerate(move_one([a for a, b, _ in disk for _ in range(b)])) if n != EMPTY)
two = sum(i * n for i, n in enumerate([a for a, b, _ in move_two(disk) for _ in range(b)]) if n != EMPTY)

print(f"Part one: {one}")
print(f"Part two: {two}")
