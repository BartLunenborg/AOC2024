A, B, C, OFFSET = 0, 1, 2, 4
regs = [17323786, 0, 0]
instructions = [2,4,1,1,7,5,1,5,4,1,5,5,0,3,3,0]

def get_val(combo_op):
    if combo_op in [0, 1, 2, 3]:
        return combo_op
    else:
        return regs[combo_op - OFFSET]

def adv(inst, op):  # 0
    regs[A] //= (1 << get_val(op))
    return inst + 2

def bxl(inst, op):  # 1
    regs[B] ^= op
    return inst + 2

def bst(inst, op):  # 2
    regs[B] = get_val(op) % 8
    return inst + 2

def jnz(inst, op):  # 3
    return op if regs[A] != 0 else inst + 2

def bxc(inst, op):  # 4
    regs[B] ^= regs[C]
    return inst + 2

def out(inst, op):  # 5
    global output
    val = get_val(op) % 8
    output += str(val) + ","
    return inst + 2

def bdv(inst, op):  # 6
    regs[B] = regs[A] // (1 << get_val(op))
    return inst + 2

def cdv(inst, op):  # 7
    regs[C] = regs[A] // (1 << get_val(op))
    return inst + 2

def perform_instructions(pointer=0):
    global output
    output = ""
    funcs = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    while pointer < len(instructions):
        func, op = instructions[pointer], instructions[pointer + 1]
        pointer = funcs[func](pointer, op)
    return output[:-1]

one = perform_instructions()

# My instructions written out
def calc(a, b=0, c=0, i=0):
    while a != 0:
        b = a % 8
        b ^= 1
        c = a // (1 << b)
        b ^= 5
        b ^= c
        if b % 8 != instructions[i]:
            if i > 10:  # We had a prefix of instructions of len > 10
                print(i, two)  # For analysing output
            return False
        i += 1
        a //= (1 << 3)
    return True

# For the starting point of two I first looked for a number
# that would produce len(instructions) output and went from there. 
two = 101055168605885
while True:
    if calc(two):
        break
    else:
        # Found through analysing output and comparing how many
        # steps there were between some two large prefixes of instructions.
        # Some trial and error + luck was involved.
        two += 67108864  

print(f"Part one: {one}")
print(f"Part two: {two}")
