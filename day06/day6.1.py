
f = open("input.txt")
banks = [int(x) for x in f.read().split()]
f.close()

#banks = [0,2,7,0]

count = 0
seen = {}

while True:
    cconfig = "".join([str(i) for i in banks])
    if cconfig in seen:
        print(count - seen[cconfig])
        break
    seen.update({cconfig:count})
    count += 1
    highest = max(banks)
    h_index = banks.index(highest)
    banks[h_index] = 0
    while highest > 0:
        h_index += 1
        if h_index == len(banks): h_index = 0
        banks[h_index] += 1
        highest -= 1
