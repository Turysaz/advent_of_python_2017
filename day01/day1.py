
f = open("../input/day01.txt")
lines = f.readlines()[0][:-1]
f.close()


s = 0

i = 0
l = len(lines)

while i < l:
    c = lines[i]

    cnext = None

    if i == l - 1:
        cnext = lines[0]
    else:
        cnext = lines[i+1]

    if c == cnext:
        s += int(c)

    i += 1

print("01/1: " + str(s))
