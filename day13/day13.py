
f = open("../input/day13.txt")
lines = [[int(x[0]), int(x[1])] for x in [l.split(": ") for l in f.readlines()]]
f.close()

lines2 = [
    [0, 3],
    [1, 2],
    [4, 4],
    [6, 4]
]

# init firewall
ranges = {}
positions = {}
directions = {}
for layer in lines:
    ranges.update({layer[0]:layer[1]})
    positions.update({layer[0]:0})
    directions.update({layer[0]:1})

# init package
pack_pos = 0
total_severity = 0

while pack_pos < max(ranges)+1:
    if pack_pos in positions:
        if positions[pack_pos] == 0:
            total_severity += pack_pos * ranges[pack_pos]

    for i in positions:
        positions[i] += directions[i]
        if positions[i] == 0 or positions[i] == ranges[i]-1:
            directions[i] *= -1

    pack_pos += 1


print(total_severity)
