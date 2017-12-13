f = open("../input/day13.txt")
layers = [[int(x[0]), int(x[1])] for x in [l.split(": ") for l in f.readlines()]]
f.close()

#layers = [
#    [0, 3],
#    [1, 2],
#    [4, 4],
#    [6, 4]
#]

# init firewall
ranges = {}
scanner_pos = []
scanner_dir = []
for x in layers: ranges.update({x[0]:x[1]})
for x in range(max(ranges)+1):
    if x not in ranges:
        ranges.update({x:0})
    scanner_pos.append(0)
    scanner_dir.append(1)

# init package
package_pos = 0
total_severity = 0

while package_pos < len(ranges):
    print(package_pos, scanner_pos)
    if scanner_pos[package_pos] == 0:
        print("MATCH")
        total_severity += package_pos * ranges[package_pos]

    for i in range(len(ranges)):
        scanner_pos[i] += scanner_dir[i]
        if scanner_pos[i] == 0 or scanner_pos[i] == ranges[i]-1:
            scanner_dir[i] *= -1

    package_pos += 1

print(total_severity)
