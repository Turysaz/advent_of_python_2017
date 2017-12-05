
f = open("day1.txt")
chars = f.readlines()[0][:-1]
f.close()


def get_neighbour(line, index, step):
    l = len(line)

    i_new = index + step

    if i_new >= l:
        i_new -= l

    return line[i_new]
        

s = 0

i = 0
l = len(chars)
step = l / 2

while i < l:
    c = chars[i]

    cnext = get_neighbour(chars, i, step)

    if c == cnext:
        s += int(c)
    
    i += 1

print(s)
        
