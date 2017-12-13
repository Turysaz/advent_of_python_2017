
f = open("../input/day13.txt")
lines = [[int(x[0]), int(x[1])] for x in [l.split(": ") for l in f.readlines()]]
f.close()

#lines = [[0, 3],[1, 2],[4, 4],[6, 4]] #debug

ranges = {}
for layer in lines:
    ranges.update({layer[0]:layer[1]})

def simulate(ranges, delay = 0):
    positions, directions = {}, {}
    for x in ranges:
        positions.update({x:0})
        directions.update({x:1})

    pack_pos, severity = -delay, 0
    while pack_pos < max(ranges)+1:
        if pack_pos in positions:
            if positions[pack_pos] == 0:
                return False

        for i in positions:
            positions[i] += directions[i]
            if positions[i] == 0 or positions[i] == ranges[i]-1:
                directions[i] *= -1

        pack_pos += 1

    return True

i = 0
while True:
    print(i)
    if simulate(ranges, i) :
        print("\n" + str(i))
        break
    i+=1