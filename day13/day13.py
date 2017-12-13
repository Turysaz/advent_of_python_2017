
f = open("../input/day13.txt")
lines = [[int(x[0]), int(x[1])] for x in [l.split(": ") for l in f.readlines()]]
f.close()

#lines = [[0, 3],[1, 2],[4, 4],[6, 4]] #debug

ranges = {}
for layer in lines:
    ranges.update({layer[0]:layer[1]})

total = 0
for l in ranges:
    if l % (ranges[l]*2-2) == 0:
        total += l * ranges[l]

print(total)
