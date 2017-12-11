
f = open("../input.txt")
instr = f.read().strip().split(',')
f.close()

def get_steps(pos):
    x,y = abs(pos[0]), abs(pos[1])
    y -= x * 0.5
    return x+y

x,y = 0,0
maxdist = 0
for i in instr:
    if i[0] == 'n': y += 1.0/len(i) #reciprocal: .5 if len==2, 1 if len == 1
    if i[0] == 's': y -= 1.0/len(i)
    if len(i) == 1: continue
    if i[1] == 'e': x += 1
    if i[1] == 'w': x -= 1
    maxdist = max(maxdist, get_steps((x,y)))
print(maxdist)
