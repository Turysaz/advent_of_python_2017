
f = open("../input.txt")
instructions = [int(num[:-1]) for num in f.readlines()]
f.close()

#instructions = [0,3,0,1,-3]

count = 0
pc = 0

while  pc >= 0 and pc < len(instructions):
    count += 1
    pc_old = pc
    pc += instructions[pc]
    if instructions[pc_old] > 2: instructions[pc_old] -= 1
    else: instructions[pc_old] += 1

print(count)
